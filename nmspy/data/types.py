import ctypes.wintypes as wintypes
import types
from ctypes import (
    POINTER,
    _Pointer,
    c_bool,
    c_char,
    c_char_p,
    c_double,
    c_float,
    c_int16,
    c_int32,
    c_int64,
    c_uint8,
    c_uint16,
    c_uint32,
    c_uint64,
    c_void_p,
    cast,
)
from typing import TYPE_CHECKING, Annotated, Generic, Optional, Type, TypeVar

from pymhf.core._internal import BASE_ADDRESS
from pymhf.core.hooking import Structure, function_hook, static_function_hook
from pymhf.core.memutils import find_pattern_in_binary, map_struct
from pymhf.extensions.cpptypes import std
from pymhf.extensions.ctypes import c_char_p64, c_enum16, c_enum32
from pymhf.utils.partial_struct import Field, partial_struct
from pymhf.utils.winapi import get_filepath_from_handle

import nmspy.data.basic_types as basic
import nmspy.data.enums as enums
import nmspy.data.exported_types as nmse

T = TypeVar("T", bound=basic.CTYPES)

# Exported functions


@partial_struct
class cTkSmartResHandle(Structure):
    # This field is technically another type which just contains an int field, so we'll simplify it.
    miInternalHandle: Annotated[int, Field(c_int32, 0x0)]


class cTkTypedSmartResHandle(Structure, Generic[T]):
    _template_type: Type[T]
    mHandle: cTkSmartResHandle
    if TYPE_CHECKING:
        mpPointer: _Pointer[T]

    def __class_getitem__(cls: Type["cTkTypedSmartResHandle"], type_: Type[T]):
        _cls: Type[cTkTypedSmartResHandle[T]] = types.new_class(f"cTkTypedSmartResHandle<{type_}>", (cls,))
        _cls._template_type = type_
        _cls._fields_ = [  # type: ignore
            ("mHandle", cTkSmartResHandle),
            ("mpPointer", POINTER(type_)),
        ]
        return _cls


class cTkRefCntContainer(Structure, Generic[T]):
    mRef: Annotated[int, c_int32]
    _template_type: Type[T]
    if TYPE_CHECKING:
        mPtr: _Pointer[T]

    def __class_getitem__(cls: Type["cTkRefCntContainer"], type_: Type[T]):
        _cls: Type[cTkRefCntContainer[T]] = types.new_class(f"cTkRefCntContainer<{type_}>", (cls,))
        _cls._template_type = type_
        _cls._fields_ = [  # type: ignore
            ("mPtr", POINTER(type_)),
            ("mRef", c_int32),
        ]
        return _cls


class cTkSharedPtr(Structure, Generic[T]):
    _template_type: Type[T]
    if TYPE_CHECKING:
        mRefCntr: _Pointer[cTkRefCntContainer[T]]

    def __class_getitem__(cls: Type["cTkSharedPtr"], type_: Type[T]):
        _cls: Type[cTkSharedPtr[T]] = types.new_class(f"cTkSharedPtr<{type_}>", (cls,))
        _cls._template_type = type_
        _cls._fields_ = [  # type: ignore
            ("mRefCntr", POINTER(type_)),
        ]
        return _cls


@partial_struct
class FIOS2HANDLE(Structure):
    mFH: Annotated[int, Field(c_uint32)]

    @property
    def filename(self) -> str:
        return get_filepath_from_handle(self.mFH)


class XMLNode(Structure):
    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 41 0F B6 E8 48 8B FA")
    def createXMLTopNode(
        self,
        result: "_Pointer[XMLNode]",
        lpszName: c_uint64,
        isDeclaration: Annotated[bool, c_bool],
    ) -> c_uint64:  # XMLNode *
        ...

    @function_hook("40 53 57 41 54 41 56 41 57 48 81 EC")
    def writeToFile(
        self,
        this: "_Pointer[XMLNode]",
        filename: c_char_p64,
        encoding: c_char_p64,
        nFormat: c_uint8,
    ) -> c_uint64:
        # Writes the XMLNode to file. Return value is an integer indicating some status.
        # Return values are 0, 14 and 15.
        ...


@static_function_hook(
    "48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? B8"
)
def MiniDumpFunction(a1: c_uint64, a2: c_uint64, CurrentThreadId: wintypes.DWORD) -> c_uint64: ...


@partial_struct
class cTkResourceDescriptor(Structure):
    maDescriptors: Annotated[basic.TkStd.tk_vector[basic.TkID0x20], 0x0]
    mSeed: Annotated[basic.cTkSeed, 0x10]
    mSecondarySeed: Annotated[basic.cTkSeed, 0x20]


@partial_struct
class cTkResource(Structure):
    _total_size_ = 0x1C0  # ?
    # __vftable: Annotated[c_uint64, Field(c_uint64, 0)]
    # Found in cTkResource::cTkResource and cEgGeometryResource::cEgGeometryResource
    miType: Annotated[c_enum32[enums.ResourceTypes], 0x8]
    msName: Annotated[basic.cTkFixedString[0x100], 0xC]
    mxFlags: Annotated[int, Field(c_int32, 0x10C)]
    mHandle: Annotated[int, Field(c_int32, 0x128)]
    muRefCount: Annotated[int, Field(c_int32, 0x12C)]
    mbNoQuery: Annotated[bool, Field(c_bool, 0x131)]
    mDescriptor: Annotated[cTkResourceDescriptor, 0x188]  # TODO: Test
    muHotRequestNumber: Annotated[int, Field(c_uint16, 0x1B8)]

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? C6 41")
    def cTkResource(
        self,
        this: "_Pointer[cTkResource]",
        liType: Annotated[int, c_int32],
        lsName: _Pointer[basic.cTkFixedString0x100],
        lxFlags: Annotated[int, c_int32],
    ): ...


@partial_struct
class cEgRenderQueueEntry(Structure):
    mRenderSpaceTransform: Annotated[basic.cTkMatrix34, 0x0]


@partial_struct
class cEgRenderQueueBuffer(Structure):
    mpFinalBuffer: Annotated[_Pointer[cEgRenderQueueEntry], 0x0]
    muNumEntries: Annotated[int, Field(c_int32, 0x48)]
    muCapacity: Annotated[int, Field(c_int32, 0x48)]


@partial_struct
class cTkRenderStateCache(Structure):
    pass


@partial_struct
class cEgThreadableRenderCall(Structure):
    @partial_struct
    class cRendererData(Structure):
        _total_size_ = 0x290

    mRendererData: Annotated[cRendererData, 0x10]
    _mpFunctionParams: Annotated[c_void_p, 0x2A0]
    mRenderStateCache: Annotated[cTkRenderStateCache, 0x2B0]

    @property
    def mpFunctionParams(self):
        return cast(self._mpFunctionParams, _Pointer[cEgDrawGeometry])


@partial_struct
class cEgDrawGeometry(Structure):
    # These are found in cEgDrawGeometry::Draw as arguments to cEgRenderer::DrawRenderables
    mNodeType: Annotated[_Pointer[basic.TkID0x10], 0x8]

    @static_function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 81 EC ? ? ? ? 65 48 8B 04 25")
    @staticmethod
    def Draw(
        lpData: _Pointer[cEgThreadableRenderCall],
        # Not sure if the following args are real...
        a2: c_uint64,
        a3: c_uint64,
        a4: c_uint64,
    ): ...


class AK(Structure):
    class SoundEngine(Structure):
        @static_function_hook(exported_name="?RegisterGameObj@SoundEngine@AK@@YA?AW4AKRESULT@@_KPEBD@Z")
        @staticmethod
        def RegisterGameObj(
            in_GameObj: c_uint64,
            in_pszObjName: c_uint64,
        ) -> c_int64: ...

        @static_function_hook(
            exported_name=(
                "?PostEvent@SoundEngine@AK@@YAII_KIP6AXW4AkCallbackType@@PEAUAkCallbackInfo@@@ZPEAXIPEAUAkExt"
                "ernalSourceInfo@@I@Z"
            )
        )
        @staticmethod
        def PostEvent(
            in_ulEventID: Annotated[int, c_uint32],
            in_GameObjID: Annotated[int, c_uint64],
            in_uiFlags: Annotated[int, c_uint32] = 0,
            callback: Annotated[int, c_uint64] = 0,
            in_pCookie: c_void_p = 0,
            in_cExternals: Annotated[int, c_uint32] = 0,
            in_pExternalSources: Annotated[int, c_uint64] = 0,
            in_PlayingID: Annotated[int, c_uint32] = 0,
        ) -> c_uint64: ...


@partial_struct
class cGcNGuiText(Structure):
    # Found in cGcNGuiText::EditElement
    mpTextData: Annotated[
        _Pointer[nmse.cGcNGuiTextData],
        Field(_Pointer[nmse.cGcNGuiTextData], 0x160),
    ]

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 81 EC ? ? ? ? 0F 29 70 ? 0F "
        "29 78 ? 48 8D A8 ? ? ? ? 48 83 E5 ? 48 8B 01 48 8B F9"
    )
    def EditElement(self, this: "_Pointer[cGcNGuiText]"): ...


@partial_struct
class cTkPersonalRNG(Structure):
    mState0: Annotated[int, Field(c_uint32)]
    mState1: Annotated[int, Field(c_uint32)]


@partial_struct
class TkAudioID(Structure):
    mpacName: Annotated[Optional[str], Field(c_char_p)]
    muID: Annotated[int, Field(c_uint32)]
    mbValid: Annotated[bool, Field(c_bool)]


@partial_struct
class cTkAudioManager(Structure):
    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 56 48 83 EC ? 48 8B F1 48 8B C2")
    def Play_attenuated(
        self,
        this: "_Pointer[cTkAudioManager]",
        event: _Pointer[TkAudioID],
        position: c_uint64,
        object: c_int64,
        attenuationScale: Annotated[float, c_float],
    ) -> c_bool: ...

    @function_hook("48 83 EC ? 33 C9 4C 8B D2 89 4C 24 ? 49 8B C0 48 89 4C 24 ? 45 33 C9")
    def Play(
        self,
        this: "_Pointer[cTkAudioManager]",
        event: _Pointer[TkAudioID],
        object: c_int64,
    ) -> c_bool: ...


@partial_struct
class cGcNGuiElement(Structure):
    mpElementData: Annotated[
        _Pointer[nmse.cGcNGuiElementData],
        Field(_Pointer[nmse.cGcNGuiElementData], 0x48),
    ]

    @function_hook("48 83 EC ? 4C 8B 59 ? 4C 8B C9")
    def SetPosition(
        self,
        this: "_Pointer[cGcNGuiElement]",
        lPosition: _Pointer[basic.Vector2f],
        lType: c_uint32,  # cGcNGuiElement::PositionType
    ): ...


@partial_struct
class cGcNGuiLayer(cGcNGuiElement):
    @function_hook(
        "48 83 EC ? 4C 8B 02 4C 8B C9 0F 10 02 49 8B C0 48 B9 ? ? ? ? ? ? ? ? 48 33 42 ? 48 0F AF C1 0F 11 44"
        " 24 ? 48 8B D0 48 C1 EA ? 48 33 D0 49 33 D0 48 0F AF D1 4C 8B C2 49 C1 E8 ? 4C 33 C2 4C 0F AF C1 41 "
        "8B C8 41 0F B7 D0 81 C2 ? ? ? ? C1 E9 ? 8B C2 49 C1 E8 ? C1 E0 ? 81 E1 ? ? ? ? 33 C8 33 D1 41 0F B7 "
        "C8 8B C2 41 C1 E8 ? C1 E8 ? 41 81 E0 ? ? ? ? 03 D0 03 D1 8B C2 C1 E0 ? 44 33 C0 41 33 D0 41 B8 ? ? ?"
        " ? 8B C2 C1 E8 ? 03 D0 8D 04 D5 ? ? ? ? 33 D0 8B C2 C1 E8 ? 03 D0 8B C2 C1 E0 ? 33 D0 8B C2 C1 E8 ? "
        "03 D0 8B C2 C1 E0 ? 33 D0 8B C2 C1 E8 ? 03 C2 48 8D 54 24 ? 69 C0 ? ? ? ? C1 C8 ? 69 C8 ? ? ? ? 83 "
        "F1 ? C1 C9 ? 8D 0C 89 81 C1 ? ? ? ? 48 89 4C 24 ? 49 8B C9 E8 ? ? ? ? 48 83 C4 ? C3 CC CC CC CC CC "
        "CC 0F B6 41"
    )
    def FindTextRecursive(
        self,
        this: "_Pointer[cGcNGuiLayer]",
        lID: c_uint64,
    ) -> c_uint64:  # cGcNGuiElement *
        ...

    @function_hook("40 55 57 41 57 48 83 EC ? 4C 8B 89")
    def FindElementRecursive(
        self,
        this: "_Pointer[cGcNGuiLayer]",
        lID: c_uint64,  # const cTkHashedNGuiElement *
        leType: c_uint32,  # eNGuiGameElementType
    ) -> c_uint64:  # cGcNGuiElement *
        ...

    @function_hook("48 8B C4 53 48 81 EC ? ? ? ? 48 89 78 ? 4C 8B D2")
    def LoadFromMetadata(
        self,
        this: "_Pointer[cGcNGuiLayer]",
        lpacFilename: _Pointer[basic.cTkFixedString[0x80]],
        lbUseCached: Annotated[bool, c_bool],
        a4: Annotated[bool, c_bool],
    ): ...

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 48 89 54 24 ? 57 48 81 EC ? ? ? ? 44 8B 51")
    def AddElement(
        self,
        this: "_Pointer[cGcNGuiLayer]",
        lpElement: "_Pointer[cGcNGuiLayer]",
        lbOnTheEnd: c_int64,
    ): ...

    @function_hook(
        "48 89 5C 24 ? 57 48 83 EC ? 4C 8B 89 ? ? ? ? 41 0F B6 F8 48 8B 0A 49 BA ? ? ? ? ? ? ? ? 48 8B C1 48 "
        "33 42 ? 49 0F AF C2 48 8B D0 48 C1 EA ? 48 33 D0 48 33 D1 49 0F AF D2 4C 8B C2 49 C1 E8 ? 4C 33 C2 "
        "4D 0F AF C2 41 0F B7 D0 41 8B C8 81 C2 ? ? ? ? 49 C1 E8 ? 8B C2 C1 E9 ? C1 E0 ? 81 E1 ? ? ? ? 33 C8 "
        "33 D1 41 0F B7 C8 8B C2 41 C1 E8 ? C1 E8 ? 41 81 E0 ? ? ? ? 03 D0 03 D1 8B C2 C1 E0 ? 44 33 C0 41 33"
        " D0 8B C2 C1 E8 ? 03 D0 8D 04 D5 ? ? ? ? 33 D0 8B C2 C1 E8 ? 03 D0 8B C2 C1 E0 ? 33 D0 8B C2 C1 E8 ?"
        " 03 D0 8B C2 C1 E0 ? 33 D0 8B C2 C1 E8 ? 03 C2 69 C0 ? ? ? ? C1 C8 ? 69 C0 ? ? ? ? 83 F0 ? C1 C8 ? "
        "05 ? ? ? ? 41 83 79 ? ? 8D 04 80 8B D0 7E ? 49 63 49 ? 48 98 48 FF C9 48 23 C8 49 8B 41 ? 48 8B 04 "
        "C8 48 85 C0 74 ? 48 39 50 ? 75 ? 48 3B 50 ? 74 ? 48 8B 40 ? 48 85 C0 75 ? 33 C0 48 8D 0D ? ? ? ? 40 "
        "84 FF 48 0F 45 C1 48 8B 5C 24 ? 48 83 C4 ? 5F C3 48 8B 58 ? 48 85 DB 74 ? 48 8B 13 48 8B CB FF 52 ? "
        "83 F8 ? 75 ? 48 8B C3 48 8B 5C 24 ? 48 83 C4 ? 5F C3 CC CC CC CC CC CC CC 48 89 54 24"
    )
    def GetGraphic(
        self,
        this: "_Pointer[cGcNGuiLayer]",
        lID: _Pointer[basic.TkID0x10],
        lbUseDefault: Annotated[bool, c_bool],
    ) -> c_uint64:  # cGcNGuiGraphic *
        ...


@partial_struct
class cGcNGui(Structure):
    mRoot: Annotated[cGcNGuiLayer, 0x0]


@partial_struct
class cGcShipHUD(Structure):
    # The following offset is found from cGcShipHUD::RenderHeadsUp below the 2nd
    # cGcNGuiLayer::FindElementRecursive call.
    miSelectedPlanet: Annotated[int, Field(c_uint32, 0x23BF0)]
    mbSelectedPlanetPanelVisible: Annotated[bool, Field(c_bool, 0x23C00)]

    # The following offset is found by searching for "UI\\HUD\\SHIP\\MAINSCREEN.MXML"
    # (It's above the below entry.)
    mMainScreenGUI: Annotated[cGcNGui, Field(cGcNGui, offset=0x27478)]
    # The following offset is found by searching for "UI\\HUD\\SHIP\\HEADSUP.MXML"
    mHeadsUpGUI: Annotated[cGcNGui, Field(cGcNGui, offset=0x27A10)]

    # hud_root: Annotated[int, Field(c_ulonglong, 0x27F70)]  # TODO: Fix

    @function_hook("48 89 5C 24 ? 57 41 54 41 55 41 56 41 57 48 81 EC")
    def LoadData(self, this: "_Pointer[cGcShipHUD]"): ...

    @function_hook("40 55 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 4C 8B F9 48 8B 0D ? ? ? ? 48 81 C1")
    def RenderHeadsUp(self, this: "_Pointer[cGcShipHUD]"): ...


class cTkStopwatch(Structure):
    @function_hook("48 83 EC ? 48 8B 11 0F 29 74 24")
    def GetDurationInSeconds(self, this: "_Pointer[cTkStopwatch]") -> c_float: ...


class cGcRealityManager(Structure):
    @function_hook("48 8B C4 48 89 48 ? 55 53 56 57 41 54 41 56 48 8D A8")
    def Construct(self, this: "_Pointer[cGcRealityManager]"): ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B F9 33 ED 48 89 A9")
    def cGcRealityManager(self, this: "_Pointer[cGcRealityManager]"): ...

    @function_hook(
        "48 89 54 24 ? 48 89 4C 24 ? 55 53 41 54 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B DA "
        "4C 8B E1"
    )
    def GenerateProceduralProduct(
        self,
        this: "_Pointer[cGcRealityManager]",
        lProcProdID: _Pointer[basic.TkID[0x10]],
    ) -> c_uint64:  # cGcProductData *
        ...

    @function_hook("4C 89 4C 24 ? 44 88 44 24 ? 48 89 4C 24")
    def GenerateProceduralTechnology(
        self,
        this: "_Pointer[cGcRealityManager]",
        lProcTechID: _Pointer[basic.TkID[0x10]],
        lbExampleForWiki: Annotated[bool, c_bool],
    ) -> c_uint64:  # cGcProductData *
        ...


@partial_struct
class cGcInventoryStore(Structure):
    _total_size_ = 0x248

    mxValidSlots: Annotated[basic.cTkBitArray[c_uint64, 16] * 16, 0x0]
    miWidth: Annotated[int, Field(c_int16, 0x80)]
    miHeight: Annotated[int, Field(c_int16, 0x82)]
    miCapacity: Annotated[int, Field(c_int16, 0x84)]
    mStore: Annotated[basic.TkStd.tk_vector[nmse.cGcInventoryElement], 0x88]
    mStoreHistory: Annotated[basic.TkStd.tk_vector[nmse.cGcInventoryElement], 0x98]
    meStackSizeGroup: Annotated[c_enum16[enums.cGcInventoryStackSizeGroup], 0xB8]
    maSpecialSlots: Annotated[basic.TkStd.tk_vector[nmse.cGcInventorySpecialSlot], 0xC0]
    maBaseStats: Annotated[basic.TkStd.tk_vector[nmse.cGcInventoryBaseStatEntry], 0xD0]
    mLayoutDescriptor: Annotated[nmse.cGcInventoryLayout, 0xE0]
    mbAutoMaxEnabled: Annotated[bool, Field(c_bool, 0xF8)]
    mClass: Annotated[c_enum32[enums.cGcInventoryClass], 0x100]
    mInventoryName: Annotated[basic.cTkFixedString0x100, 0x104]

    @function_hook(
        "48 89 5C 24 ? 57 48 83 EC ? 33 FF 0F 57 C0 0F 11 01 48 8B D9 0F 11 41 ? 0F 11 41 ? 0F 11 41"
    )
    def cGcInventoryStore(self, this: "_Pointer[cGcInventoryStore]"): ...


@partial_struct
class cGcPlayerState(Structure):
    mNameWithTitle: Annotated[basic.cTkFixedString0x100, 0x0]
    mGameStartLocation1: Annotated[nmse.cGcUniverseAddressData, 0x150]
    mGameStartLocation2: Annotated[nmse.cGcUniverseAddressData, 0x168]
    # We can find this in cGcPlayerState::GetPlayerUniverseAddress, which, while not mapped, can be found
    # inside cGcQuickActionMenu::TriggerAction below the string QUICK_MENU_EMERGENCY_WARP_BAN.
    mLocation: Annotated[nmse.cGcUniverseAddressData, 0x180]
    mPrevLocation: Annotated[nmse.cGcUniverseAddressData, 0x198]
    miShield: Annotated[int, Field(c_int32, 0x1B0)]
    miHealth: Annotated[int, Field(c_int32, 0x1B4)]
    miShipHealth: Annotated[int, Field(c_int32, 0x1B8)]
    muUnits: Annotated[int, Field(c_uint32, 0x1BC)]
    muNanites: Annotated[int, Field(c_uint32, 0x1C0)]
    muSpecials: Annotated[int, Field(c_uint32, 0x1C4)]
    # Found in cGcPlayerState::cGcPlayerState
    mInventories: Annotated[cGcInventoryStore * 0x21, 0x218]
    mVehicleInventories: Annotated[cGcInventoryStore * 0x7, 0x4D78]
    mVehicleTechInventories: Annotated[cGcInventoryStore * 0x7, 0x5D70]

    mShipInventories: Annotated[cGcInventoryStore * 0xC, 0x6F00]
    mShipInventoriesCargo: Annotated[cGcInventoryStore * 0xC, 0x8A70]
    mShipInventoriesTechOnly: Annotated[cGcInventoryStore * 0xC, 0xA5D0]

    # Found in cGcPlayerShipOwnership::SpawnNewShip
    miPrimaryShip: Annotated[int, Field(c_uint32, 0xC4F0)]

    # Found in cGcPlayerState::cGcPlayerState above the loop over something 5 times. Around line 220.
    mPhotoModeSettings: Annotated[nmse.cGcPhotoModeSettings, 0xE630]
    maTeleportEndpoints: Annotated[std.vector[nmse.cGcTeleportEndpoint], 0xE680]
    maCustomShipNames: Annotated[basic.cTkFixedString0x20 * 0xC, 0xE903]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 4C 24 ? 57 41 54 41 55 41 56 41 57 48 83 EC ? 45 33 "
        "FF"
    )
    def cGcPlayerState(self, this: "_Pointer[cGcPlayerState]"): ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 44 8B 81 ? ? ? ? 48 8D 2D")
    def AwardUnits(
        self,
        this: "_Pointer[cGcPlayerState]",
        liChange: Annotated[int, c_int32],
    ) -> c_uint64: ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 44 8B 81 ? ? ? ? 48 8D 35")
    def AwardNanites(
        self,
        this: "_Pointer[cGcPlayerState]",
        liChange: Annotated[int, c_int32],
    ) -> c_uint64: ...

    @function_hook("89 54 24 ? 4C 8B DC 48 83 EC")
    def StoreCurrentSystemSpaceStationEndpoint(
        self,
        this: "_Pointer[cGcPlayerState]",
        a2: c_int32,
    ): ...

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 54 41 55 41 56 41 57 48 83 EC ? 48 8B AC 24 ? ? ? ? "
        "48 8B D9 4C 63 F2"
    )
    def GetStatValue(
        self,
        this: "_Pointer[cGcPlayerState]",
        leStat: c_enum32[enums.cGcStatsTypes],
        leLookupType: c_int32,  # ItemLookupType
        leBaseStat: c_enum32[enums.cGcStatsTypes],
        lbIgnoreAdjacencyBonus: Annotated[bool, c_bool],
        lbIgnoreInventoryBonus: Annotated[bool, c_bool],
        lpPrimaryInventory: _Pointer[cGcInventoryStore * 0x21],
        lpTechInventory: _Pointer[cGcInventoryStore],
    ) -> c_float: ...


@partial_struct
class cGcPlayerShipOwnership(Structure):
    @partial_struct
    class sGcShipData(Structure):
        _total_size_ = 0x30

        # Not sure about these...
        # Mapping is found in cGcPlayerShipOwnership::cGcPlayerShipOwnership but they don't seem to line up
        # with old data.
        mPlayerShipNode: Annotated[basic.TkHandle, 0x0]
        mpPlayerShipAttachment: Annotated[c_uint64, 0x8]  # cTkAttachmentPtr
        mPlayerShipSeed: Annotated[basic.cTkSeed, 0x10]  # TODO: Fix - Not sure if the seed is here any more?
        mfUnknown0x20: Annotated[float, Field(c_float, 0x20)]
        mbUnknown0x28: Annotated[bool, Field(c_bool, 0x28)]  # Looks like "is valid/data"

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 54 41 56 41 57 48 83 EC ? 45 33 E4 48 C7 "
        "41"
    )
    def cGcPlayerShipOwnership(self, this: "_Pointer[cGcPlayerShipOwnership]"): ...

    @function_hook("48 89 5C 24 ? 55 56 57 41 54 41 56 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 45")
    def UpdateMeshRefresh(self, this: "_Pointer[cGcPlayerShipOwnership]"): ...

    @function_hook("48 8B C4 55 53 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 80 B9 ? ? ? ? ? 48 8B F1")
    def Update(
        self,
        this: "_Pointer[cGcPlayerShipOwnership]",
        lfTimestep: Annotated[float, c_float],
    ): ...

    @function_hook("44 89 44 24 ? 48 89 54 24 ? 55 56 41 54 41 56 41 57 48 8D 6C 24")
    def SpawnNewShip(
        self,
        this: "_Pointer[cGcPlayerShipOwnership]",
        lMatrix: _Pointer[basic.cTkMatrix34],
        leLandingGearState: c_uint32,  # cGcPlayerShipOwnership::ShipSpawnLandingGearState
        liShipIndex: c_int32,
        lbSpawnShipOverride: c_bool,
    ) -> c_bool: ...

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 48 8B 35 ? ? ? ? 8B DA"
    )
    def DestroyShip(
        self,
        this: "_Pointer[cGcPlayerShipOwnership]",
        liShipIndex: c_int32,
    ) -> c_bool: ...

    @function_hook("83 FA ? 75 ? 48 8B 05 ? ? ? ? 8B 90 ? ? ? ? 48 63 C2 48 8D 14 40 48 03 D2")
    def GetShipComponent(
        self,
        this: "_Pointer[cGcPlayerState]",
        liShipIndex: Annotated[int, c_int32],
    ) -> c_uint64:  # cTkComponent *
        ...

    # Found in cGcPlayerShipOwnership::cGcPlayerShipOwnership
    mShips: Annotated[list[sGcShipData], Field(sGcShipData * 12, 0x60)]
    # Both these found at the top of cGcPlayerShipOwnership::UpdateMeshRefresh
    mbShouldRefreshMesh: Annotated[bool, Field(c_bool, 0xA690)]
    mMeshRefreshState: Annotated[int, Field(c_uint32, 0xA694)]
    mRefreshSwapRes: Annotated[cTkSmartResHandle, 0xA698]


@partial_struct
class cGcPlayerVehicleOwnership(Structure):
    # Found in cGcPlayerVehicleOwnership::cGcPlayerVehicleOwnership
    mbShouldRefreshMesh: Annotated[bool, Field(c_bool, 0x740)]

    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 33 FF 48 C7 41 ? ? ? ? ? 48 89 79 ? 48 B8")
    def cGcPlayerVehicleOwnership(self, this: "_Pointer[cGcPlayerVehicleOwnership]"): ...


class cGcPlayerCreatureOwnership(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 4C 24 ? 57 41 54 41 55 41 56 41 57 48 83 EC ? BB"
    )
    def cGcPlayerCreatureOwnership(self, this: "_Pointer[cGcPlayerCreatureOwnership]"): ...


class cGcPlayerMultitoolOwnership(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 45 33 FF 0F 29 74 24 ? 44 89 39"
    )
    def cGcPlayerMultitoolOwnership(self, this: "_Pointer[cGcPlayerMultitoolOwnership]"): ...


@partial_struct
class cGcPlayerFreighterOwnership(Structure):
    _total_size_ = 0x4A0

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 F6 C7 41 ? ? ? ? ? 48 8D 05")
    def cGcPlayerFreighterOwnership(self, this: "_Pointer[cGcPlayerFreighterOwnership]"): ...


@partial_struct
class cGcPlayerFleetManager(Structure):
    _total_size_ = 0x3FB0

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8D 05 ? ? ? ? C7 41 ? ? ? ? ? 48 89 01 "
        "48 8B D9"
    )
    def cGcPlayerFleetManager(self, this: "_Pointer[cGcPlayerFleetManager]"): ...


@partial_struct
class cGcGalacticVoxelCoordinate(Structure):
    mX: Annotated[int, Field(c_uint16)]
    mZ: Annotated[int, Field(c_uint16)]
    mY: Annotated[int, Field(c_uint16)]
    mbValid: Annotated[bool, Field(c_bool)]


@partial_struct
class sVisitedSystem(Structure):
    mVoxel: Annotated[cGcGalacticVoxelCoordinate, 0x0]
    miSystemIndex: Annotated[int, Field(c_int16, 0x8)]
    miPlanetsVisited: Annotated[int, Field(c_uint16, 0xA)]


@partial_struct
class cGcVisitedSystemsBuffer(Structure):
    mVisitedSystems: Annotated[sVisitedSystem * 0x200, 0x0]
    miCurrentPosition: Annotated[int, Field(c_int32, 0x1800)]
    miVisitedSystemsCount: Annotated[int, Field(c_int32, 0x1804)]

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 81 EC ? ? ? ? 48 8B 32")
    def VisitNewGalacticAddress(
        self,
        this: "_Pointer[cGcVisitedSystemsBuffer]",
        lu64Address: _Pointer[c_uint64],
    ): ...


@partial_struct
class sHashValue(Structure):
    muHashValue: Annotated[int, Field(c_uint16, 0x0)]
    miTimeStamp: Annotated[int, Field(c_int16, 0x2)]


@partial_struct
class cGcNetworkBufferHash(Structure):
    _total_size_ = 0x30
    # cGcNetworkBufferHash_vtbl *__vftable
    kiChunkSize: Annotated[int, Field(c_int32, 0x8)]
    miChunkHashOffset: Annotated[int, Field(c_int32, 0xC)]
    maChunkHashValues: Annotated[basic.TkStd.tk_vector[sHashValue], 0x10]
    mu64Timestamp: Annotated[int, Field(c_uint64, 0x20)]
    mbInitialised: Annotated[bool, Field(c_bool, 0x28)]


@partial_struct
class cGcNetworkSynchronisedBuffer(Structure):
    pass


@partial_struct
class cGcPlayerBasePersistentBuffer(cGcNetworkSynchronisedBuffer):
    @partial_struct
    class PlayerBasePersistentData(Structure):
        mpBuildingEntry: Annotated[
            _Pointer[nmse.cGcBaseBuildingEntry], 0xC0
        ]  # TODO: check offset by looking in memory

    # Found in cGcPlayerBasePersistentBuffer::LoadGalacticAddress
    maBaseBuildingObjects: Annotated[basic.TkStd.tk_vector[PlayerBasePersistentData], 0x30]
    muCurrentAddress: Annotated[int, Field(c_uint64, 0x40)]
    mBaseMatrix: Annotated[basic.cTkPhysRelVec3, 0x50]
    meBaseType: Annotated[c_enum32[enums.cGcPersistentBaseTypes], 0x23C]

    @function_hook("48 8B C4 53 48 83 EC ? 48 89 68 ? 48 8B D9")
    def LoadGalacticAddress(
        self,
        this: "_Pointer[cGcPlayerBasePersistentBuffer]",
        lu64Address: _Pointer[c_uint64],
        luiThisIndex: _Pointer[c_uint64],
    ): ...


class cGcPersistentInteractionBuffer(cGcNetworkSynchronisedBuffer):
    # _total_size_ = 0x190
    # Found in cGcPersistentInteractionBuffer::SaveInteraction
    miLastBufferIndex: Annotated[int, Field(c_int32, 0x30)]
    muCurrentAddress: Annotated[int, Field(c_uint64, 0x38)]
    meType: Annotated[c_enum32[enums.cGcInteractionBufferType], 0x40]
    maBufferData: Annotated[basic.cTkDynamicArray[nmse.cGcInteractionData], 0x50]

    @function_hook("40 53 56 57 41 56 48 81 EC")
    def LoadGalacticAddressBuffers(
        self,
        this: "_Pointer[cGcPersistentInteractionBuffer]",
        lu64Address: _Pointer[c_uint64],
    ): ...

    @function_hook("48 89 5C 24 ? 56 48 83 EC ? 0F 10 22")
    def SaveInteraction(
        self,
        this: "_Pointer[cGcPersistentInteractionBuffer]",
        lPosition: _Pointer[basic.cTkVector3],
        lData: _Pointer[nmse.cGcInteractionData],
        lbReplace: Annotated[bool, c_bool],
        lfRadius: Annotated[float, c_float],
    ): ...


@partial_struct
class cGcPersistentInteractionsManager(Structure):
    # Found in cGcPersistentInteractionsManager::LoadGalacticAddressBuffers
    mDistressSignalBuffer: Annotated[cGcPersistentInteractionBuffer, 0x1C20]
    mCrateBuffer: Annotated[cGcPersistentInteractionBuffer, 0x1DB0]
    mDestructableBuffer: Annotated[cGcPersistentInteractionBuffer, 0x1F40]
    mCostBuffer: Annotated[cGcPersistentInteractionBuffer, 0x20D0]
    mBuildingBuffer: Annotated[cGcPersistentInteractionBuffer, 0x2260]
    mCreatureBuffer: Annotated[cGcPersistentInteractionBuffer, 0x23F0]
    mPersonalBuffer: Annotated[cGcPersistentInteractionBuffer, 0x2580]
    mFireteamSyncBuffer: Annotated[cGcPersistentInteractionBuffer, 0x2710]
    mVisitedSystemsBuffer: Annotated[cGcVisitedSystemsBuffer, 0x1A4A70]

    @function_hook("48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 83 EC ? 4C 8B E9")
    def LoadGalacticAddressBuffers(
        self,
        this: "_Pointer[cGcPersistentInteractionsManager]",
        lu64Address: _Pointer[c_uint64],
    ): ...


@partial_struct
class cGcGameState(Structure):
    # Found in cGcGameState::cGcGameState
    mPlayerState: Annotated[cGcPlayerState, 0xA950]
    mSavedSpawnState: Annotated[nmse.cGcPlayerSpawnStateData, 0xA2AF0]
    mPlayerShipOwnership: Annotated[cGcPlayerShipOwnership, 0xA2BD0]
    mPlayerVehicleOwnership: Annotated[cGcPlayerVehicleOwnership, 0xAD270]
    mPlayerCreatureOwnership: Annotated[cGcPlayerCreatureOwnership, 0xAD9C0]
    mPlayerMultitoolOwnership: Annotated[cGcPlayerMultitoolOwnership, 0x1C7E20]
    mPlayerFreighterOwnership: Annotated[cGcPlayerFreighterOwnership * 4, 0x1CDE60]
    mPlayerFleetManager: Annotated[cGcPlayerFleetManager * 4, 0x1CF0E0]
    mRNG: Annotated[cTkPersonalRNG, 0x1DEFA4]
    # Found passed into cGcPersistentInteractionsManager::LoadGalacticAddressBuffers wherever it is called.
    # Need to subtract the offset of cGcGamestate from the address in the exe which is the pointer to the
    # start of cGcApplication::Data
    mSavedInteractionsManager: Annotated[cGcPersistentInteractionsManager, 0x226EB0]

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? C7 41")
    def cGcGameState(self, this: "_Pointer[cGcGameState]"): ...

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 88 54 24")
    def OnSaveProgressCompleted(
        self,
        this: "_Pointer[cGcGameState]",
        a2: c_uint64,
        lbShowMessage: Annotated[bool, c_bool],
        lbFullSave: Annotated[bool, c_bool],
        leSaveReason: c_int32,
    ): ...

    @function_hook("44 89 44 24 ? 89 54 24 ? 55 53 48 8D AC 24")
    def LoadFromPersistentStorage(
        self,
        this: "_Pointer[cGcGameState]",
        leSlot: Annotated[int, c_uint32],
        a3: c_int32,
        lbNetworkClientLoad: Annotated[bool, c_bool],
    ) -> c_uint64: ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? "
        "? ? F3 0F 10 91"
    )
    def Update(self, this: "_Pointer[cGcGameState]", lfTimeStep: Annotated[float, c_float]): ...


class cTkFSM(Structure):
    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 ED 48 89 51")
    def Construct(
        self,
        this: "_Pointer[cTkFSM]",
        lpOffsetTable: c_uint64,
        lInitialState: c_uint64,
    ): ...

    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 48 8B 05 ? ? ? ? 48 8B D9 0F 29 74 24")
    def Update(self, this: "_Pointer[cTkFSM]"):
        """Run every frame. Depsite `this` being of type `cTkFSM`, it's actually a pointer to the
        `cGcApplication` singleton since it has `cTkFSM` as a subclass."""
        ...

    @function_hook("48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 4C 8B 51 ? 49 8B E8")
    def StateChange(
        self,
        this: "_Pointer[cTkFSM]",
        lNewStateID: c_uint64,
        lpUserData: c_uint64,
        lbForceRestart: Annotated[bool, c_bool],
    ): ...


@partial_struct
class cTkHavokCharacterController(Structure):
    mTargetVelocity: Annotated[basic.cTkVector3, 0xE0]


class cGcPlayerController(Structure): ...


@partial_struct
class cGcPlayer(Structure):
    mRootNode: Annotated[basic.TkHandle, 0xE0]
    mPhysicsController: Annotated[_Pointer[cTkHavokCharacterController], 0x160]
    # Found in cGcPlayer::Prepare
    mbSpawned: Annotated[bool, Field(c_bool, 0x2DA0)]
    mbIsRunning: Annotated[bool, Field(c_bool, 0x2DA2)]
    mbIsAutoWalking: Annotated[bool, Field(c_bool, 0x2DA8)]
    mfJetpackTank: Annotated[float, Field(c_float, 0x3154)]
    # Found Above the cGcPlayer::UpdateGraphics call in cGcPlayer::CheckFallenThroughFloor
    mfAirTimer: Annotated[float, Field(c_float, 0x3190)]
    mfStamina: Annotated[float, Field(c_float, 0x4EF0)]
    mbIsDying: Annotated[bool, Field(c_bool, 0x4FD0)]

    @function_hook("40 55 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 4C 8B F9 48 8B 0D ? ? ? ? 83 B9")
    def CheckFallenThroughFloor(self, this: "_Pointer[cGcPlayer]"): ...

    @function_hook("48 8B C4 4C 89 48 ? 44 89 40 ? 55 56")
    def TakeDamage(
        self,
        this: "_Pointer[cGcPlayer]",
        lfDamageAmount: Annotated[float, c_float],
        leDamageType: c_enum32[enums.cGcDamageType],
        lDamageId: _Pointer[basic.TkID[0x10]],
        lDir: _Pointer[basic.Vector3f],
        lpOwner: c_uint64,  # cGcOwnerConcept *
        laEffectsDamageMultipliers: c_uint64,  # std::vector<cGcCombatEffectDamageMultiplier,TkSTLAllocatorShim<cGcCombatEffectDamageMultiplier,4,-1> > *  # noqa
    ): ...

    @function_hook("40 53 48 81 EC E0 00 00 00 48 8B D9 E8 ?? ?? ?? ?? 83 78 10 05")
    def OnEnteredCockpit(self, this: "_Pointer[cGcPlayer]"): ...

    @function_hook("40 53 48 83 EC 20 48 8B 1D ?? ?? ?? ?? E8 ?? ?? ?? ?? 83 78 10 05 75 ?? 48 8B")
    def GetDominantHand(self, this: "_Pointer[cGcPlayer]") -> c_int64: ...

    @function_hook("48 8B C4 55 53 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 78")
    def Update(self, this: "_Pointer[cGcPlayer]", lfStep: Annotated[float, c_float]): ...

    @function_hook("48 8B C4 48 89 58 ? 48 89 70 ? 57 48 81 EC ? ? ? ? 0F 29 70 ? 0F B6 F2")
    def UpdateGraphics(self, this: "_Pointer[cGcPlayer]", lbSetNode: Annotated[bool, c_bool]): ...

    @function_hook(
        "48 8B C4 55 53 56 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8B F2"
    )
    def Prepare(self, this: "_Pointer[cGcPlayer]", lpController: _Pointer[cGcPlayerController]): ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B FA 48 8B D9 48 8B 15")
    def SetToPosition(
        self,
        this: "_Pointer[cGcPlayer]",
        lPos: _Pointer[basic.cTkBigPos],
        lDir: _Pointer[basic.cTkVector3],
        lVel: _Pointer[basic.cTkVector3],
    ): ...


class cGcPlanetGenerationInputData(nmse.cGcPlanetGenerationInputData):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 0F 57 C0 33 FF 0F 11 01 48 89 7C 24")
    def SetDefaults(self, this: "_Pointer[cGcPlanetGenerationInputData]"): ...


@partial_struct
class cGcTerrainRegionMap(Structure):
    mfCachedRadius: Annotated[float, Field(c_float, 0x30)]
    mMatrix: Annotated[basic.cTkMatrix34, 0xD3490]
    mRootNode: Annotated[basic.TkHandle, 0x9E808]

    @function_hook("48 8B C4 48 89 48 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D 6C 24")
    def Construct(
        self,
        this: "_Pointer[cGcTerrainRegionMap]",
        lRootNode: basic.TkHandle,
        lpGeneratorData: c_uint64,  # cTkVoxelGeneratorData*
        lpBuildingData: c_uint64,  # cGcPlanetBuildingData*
        liRadius: c_int32,
        liBorderRegions: c_int32,
    ): ...


@partial_struct
class cGcDiscoveryData(Structure):
    mUniverseAddress: Annotated[c_uint64, 0x0]
    meType: Annotated[c_enum32[enums.cGcDiscoveryType], 0x40]


@partial_struct
class cGcPlanet(Structure):
    # This is found in cGcSolarSystem::cGcSolarSystem near the call to cGcPlanet::cGcPlanet
    _total_size_ = 0xD9070
    # Most of these found in cGcPlanet::Construct or cGcPlanet::cGcPlanet
    mPlanetDiscoveryData: Annotated[cGcDiscoveryData, 0x8]
    miPlanetIndex: Annotated[int, Field(c_int32, 0x50)]
    mPlanetData: Annotated[nmse.cGcPlanetData, 0x60]
    mPlanetGenerationInputData: Annotated[cGcPlanetGenerationInputData, 0x3A60]
    mRegionMap: Annotated[cGcTerrainRegionMap, 0x3B80]
    mNode: Annotated[basic.TkHandle, 0xD73D8]
    mAtmosphereNode: Annotated[basic.TkHandle, 0xD73DC]
    mRingNode: Annotated[basic.TkHandle, 0xD73E4]
    mPosition: Annotated[basic.Vector3f, 0xD73F0]

    mpEnvProperties: Annotated[_Pointer[nmse.cGcEnvironmentProperties], 0xD9058]
    mpSkyProperties: Annotated[_Pointer[nmse.cGcPlanetSkyProperties], 0xD9060]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 45 33 FF 48 C7 41 ? ? ? ? ? 44 "
        "89 79"
    )
    def cGcPlanet(self, this: "_Pointer[cGcPlanet]"): ...

    @function_hook("48 8B C4 4C 89 40 ? 88 50 ? 55 53")
    def Generate(
        self,
        this: "_Pointer[cGcPlanet]",
        lbLoad: Annotated[bool, c_bool],
        lPosition: _Pointer[basic.Vector3f],
        lSolarSystemDiscoveryData: _Pointer[cGcDiscoveryData],
        lGenerationInputParams: _Pointer[nmse.cGcPlanetGenerationInputData],
    ): ...

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 F6 89 51 ? 89 B1")
    def Construct(self, this: "_Pointer[cGcPlanet]", liIndex: c_int32): ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 56 57 41 56 48 83 EC ? 48 8B D9 8B 89")
    def SetupRegionMap(self, this: "_Pointer[cGcPlanet]"): ...

    @function_hook("48 8B C4 57 48 81 EC ? ? ? ? F3 0F 10 15")
    def UpdateClouds(self, this: "_Pointer[cGcPlanet]", lfTimeStep: Annotated[float, c_float]): ...

    @function_hook("40 53 48 83 EC ? 83 B9 ? ? ? ? ? 48 8B D9 0F 29 74 24")
    def UpdateGravity(
        self,
        this: "_Pointer[cGcPlanet]",
        lfNewGravityMultiplier: Annotated[float, c_float],
    ): ...

    @function_hook("40 55 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 80 3D")
    def UpdateWeather(self, this: "_Pointer[cGcPlanet]", lfTimeStep: Annotated[float, c_float]): ...


@partial_struct
class cGcSolarSystem(Structure):
    # These can be found in cGcSolarSystem::cGcSolarSystem
    mSolarSystemData: Annotated[nmse.cGcSolarSystemData, 0x0]
    maPlanets: Annotated[tuple[cGcPlanet, ...], Field(cGcPlanet * 6, 0x2630)]
    # Found in cGcPlayerState::StoreCurrentSystemSpaceStationEndpoint
    mSpaceStationNode: Annotated[basic.TkHandle, 0x51C068]

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 29 74 24 ? 48 8B F9 48 8B D9")
    def cGcSolarSystem(self, this: "_Pointer[cGcSolarSystem]"): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 48 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? "
        "83 3D"
    )
    def Construct(self, this: "_Pointer[cGcSolarSystem]"): ...

    @function_hook("48 89 5C 24 ? 55 56 57 41 55 41 57 48 8B EC 48 83 EC ? 83 3D")
    def OnLeavePlanetOrbit(self, this: "_Pointer[cGcSolarSystem]", lbAnnounceOSD: Annotated[bool, c_bool]):
        """lbAnnounceOSD not used."""
        ...

    @function_hook("48 8B C4 55 41 54 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 89 58 ? 45 33 E4 44 39 25")
    def OnEnterPlanetOrbit(
        self, this: "_Pointer[cGcSolarSystem]", lbAnnounceOSD: Annotated[bool, c_bool]
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? "
        "4C 8D 3D"
    )
    def Generate(
        self,
        this: "_Pointer[cGcSolarSystem]",
        lbUseSettingsFile: Annotated[bool, c_bool],
        lSeed: _Pointer[basic.GcSeed],
    ): ...

    @function_hook("48 8B C4 55 53 56 41 55 41 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 44 0F 29 40")
    def Update(self, this: "_Pointer[cGcSolarSystem]", lfTimeStep: Annotated[float, c_float]): ...


@partial_struct
class cGcPlayerEnvironment(Structure):
    mPlayerTM: Annotated[basic.cTkMatrix34, Field(basic.cTkMatrix34, 0x0)]
    mUp: Annotated[basic.Vector3f, Field(basic.Vector3f, 0x40)]

    # Found below the call to cTkDynamicGravityControl::GetGravity in cGcPlayerEnvironment::Update
    miNearestPlanetIndex: Annotated[int, Field(c_uint32, 0x2BC)]
    mfDistanceFromPlanet: Annotated[float, Field(c_float, 0x2C0)]
    mfNearestPlanetSealevel: Annotated[float, Field(c_float, 0x2C4)]
    mNearestPlanetPos: Annotated[basic.Vector3f, Field(basic.Vector3f, 0x2D0)]
    mbInsidePlanetAtmosphere: Annotated[bool, Field(c_bool, 0x2EC)]
    meLocation: Annotated[
        enums.EnvironmentLocation.Enum,
        Field(c_enum32[enums.EnvironmentLocation.Enum], 0x458),
    ]
    meLocationStable: Annotated[
        enums.EnvironmentLocation.Enum,
        Field(c_enum32[enums.EnvironmentLocation.Enum], 0x464),
    ]

    @function_hook("48 83 EC ? 80 B9 ? ? ? ? ? C6 04 24")
    def IsOnboardOwnFreighter(self, this: "_Pointer[cGcPlayerEnvironment]") -> c_bool: ...

    @function_hook("8B 81 ? ? ? ? 83 E8 ? 83 F8 ? 0F 96 C0 C3 48 83 EC")
    def IsOnPlanet(self, this: "_Pointer[cGcPlayerEnvironment]") -> c_bool: ...

    @function_hook("48 8B C4 F3 0F 11 48 ? 55 53 41 54")
    def Update(
        self,
        this: "_Pointer[cGcPlayerEnvironment]",
        lfTimeStep: Annotated[float, c_float],
    ): ...


@partial_struct
class cGcEnvironment(Structure):
    # Passed into multiple cGcPlayerEnvironment methods.
    mPlayerEnvironment: Annotated[cGcPlayerEnvironment, 0x8A0]

    @function_hook(
        "48 8B C4 48 89 48 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 "
        "? 4C 8B E9"
    )
    def UpdateRender(self, this: "_Pointer[cGcEnvironment]"):
        # TODO: There could be a few good functions to get which are called in here...
        ...


@partial_struct
class cGcSimulation(Structure):
    # Found in cGcSimulation::Update. Passed into cGcEnvironment::Update.
    mEnvironment: Annotated[cGcEnvironment, 0xAF790]
    # Found in cGcSimulation::Update. Passed into cGcSolarSystem::Update.
    mpSolarSystem: Annotated[_Pointer[cGcSolarSystem], 0x24C670]
    mPlayer: Annotated[cGcPlayer, 0x24DE40]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 0F 29 74 24 ? 48 8B F9 E8 "
        "? ? ? ? 48 8D 8F"
    )
    def cGcSimulation(self, this: "_Pointer[cGcSimulation]"): ...

    @function_hook("48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D 6C 24 ? 48 81 EC ? ? ? ? 45 33 FF")
    def Construct(self, this: "_Pointer[cGcSimulation]"): ...

    @function_hook("48 8B C4 89 50 ? 55 48 8D 6C 24")
    def Update(
        self,
        this: "_Pointer[cGcSimulation]",
        leMode: c_uint32,  # SimulationUpdateMode
        lfTimeStep: Annotated[float, c_float],
    ): ...


@partial_struct
class cGcHUDLayer(Structure):
    # This is unchanged from 4.13
    _total_size_ = 0xB0

    mpData: Annotated[_Pointer[nmse.cGcHUDLayerData], 0xA0]


@partial_struct
class cGcHUDImage(Structure):
    # This is unchanged from 4.13
    _total_size_ = 0xD0

    mpData: Annotated[_Pointer[nmse.cGcHUDImageData], 0x90]
    mColourStart: Annotated[basic.Colour, 0xA0]
    mColourEnd: Annotated[basic.Colour, 0xB0]


@partial_struct
class cGcHUDText(Structure):
    # This is unchanged from 4.13
    _total_size_ = 0x280

    mBuffer: Annotated[basic.cTkFixedWString0x100, 0x0]
    mpData: Annotated[_Pointer[nmse.cGcHUDTextData], 0x270]


@partial_struct
class cGcHUD(Structure):
    # This is unchanged from 4.13
    _total_size_ = 0x20040
    maLayers: Annotated[cGcHUDLayer * 0x80, 0x10]
    miNumLayers: Annotated[int, Field(c_int32, 0x5810)]
    maImages: Annotated[cGcHUDImage * 0x80, 0x5820]
    miNumImages: Annotated[int, Field(c_int32, 0xC020)]
    maTexts: Annotated[cGcHUDText * 0x80, 0xC030]
    miNumTexts: Annotated[int, Field(c_int32, 0x20030)]

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 33 ED 4C 8B F1")
    def cGcHUD(self, this: "_Pointer[cGcHUD]"): ...


@partial_struct
class cGcMarkerPoint(Structure):
    # Size found in the vector allocator in cGcMarkerList::TryAddMarker
    _total_size_ = 0x260
    # Found in cGcMarkerPoint::Reset
    mPosition: Annotated[basic.cTkPhysRelVec3, 0x0]
    mCenterOffset: Annotated[basic.Vector3f, 0x20]
    mCustomName: Annotated[basic.cTkFixedString0x40, 0x38]
    mCustomSubtitle: Annotated[basic.cTkFixedString0x80, 0x78]
    mNode: Annotated[basic.TkHandle, 0x104]
    mModelNode: Annotated[basic.TkHandle, 0x108]
    meBuildingClass: Annotated[
        c_enum32[enums.cGcBuildingClassification],
        Field(c_enum32[enums.cGcBuildingClassification], 0x118),
    ]

    @static_function_hook("40 53 48 83 EC ? 33 C0 0F 57 C0 0F 11 01 48 8B D9")
    @staticmethod
    def cGcMarkerPoint(address: c_uint64):
        """Construct an instance of the cGcMarkerPoint at the provided address"""
        ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 28 05 ? ? ? ? 48 8D 79")
    def Reset(self, this: "_Pointer[cGcMarkerPoint]"): ...


@partial_struct
class cGcHUDMarker(Structure):
    _total_size_ = 0x1610

    mColour: Annotated[basic.Colour, 0x0]
    mData: Annotated[cGcMarkerPoint, 0x10]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 48 8B F1 48 83 C1"
    )
    def cGcHUDMarker(self, this: "_Pointer[cGcHUDMarker]"): ...


@partial_struct
class cGcPlayerHUD(cGcHUD):
    mHelmetGUI: Annotated[cGcNGui, 0x20040]
    mCrosshairGui: Annotated[cGcNGui, 0x20498]
    mHelmetLines: Annotated[cGcNGui, 0x208F0]
    mQuickMenu: Annotated[cGcNGuiLayer, 0x20D50]
    maMarkers: Annotated[cGcHUDMarker * 0x80, 0x20F50]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 0F 29 74 24 ? 48 8B F9 E8 "
        "? ? ? ? 48 8D 9F"
    )
    def cGcPlayerHUD(self, this: "_Pointer[cGcPlayerHUD]"): ...

    @function_hook("48 8B C4 55 57 48 8D 68 ? 48 81 EC ? ? ? ? 48 8B 91")
    def RenderIndicatorPanel(self, this: "_Pointer[cGcPlayerHUD]"): ...

    @function_hook("48 8B C4 48 89 48 ? 55 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 83 B9")
    def RenderWeaponPanel(self, this: "_Pointer[cGcPlayerHUD]"): ...

    @function_hook("40 55 53 56 57 41 54 41 55 41 56 48 8D 6C 24 ? 48 81 EC ? ? ? ? 48 8B F1")
    def RenderCrosshair(self, this: "_Pointer[cGcPlayerHUD]"): ...


class cGcQuickMenu(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 48 8D 79 ? 48 8B E9"
    )
    def cGcQuickMenu(self, this: "_Pointer[cGcQuickMenu]"): ...


@partial_struct
class cGcHUDManager(Structure):
    # Found in cGcHUDManager::cGcHUDManager
    mPlayerHUD: Annotated[cGcPlayerHUD, 0xA0]
    mShipHUD: Annotated[cGcShipHUD, 0xE5CC0]
    mQuickMenu: Annotated[cGcQuickMenu, 0x10E450]
    mChargingInventory: Annotated[cGcInventoryStore, 0x11CDF0]

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 F6 48 8D 59 ? 48 89 71")
    def cGcHUDManager(self, this: "_Pointer[cGcHUDManager]", a2: c_bool): ...


@partial_struct
class cGcPlayerWeapon(Structure):
    mfChargeTime: Annotated[float, Field(c_float, 0x2338)]
    mfHeatTime: Annotated[float, Field(c_float, 0x24E0)]
    maiAmmo: Annotated[list[int], Field(c_int32 * 19, 0x2590)]
    mbCharging: Annotated[bool, Field(c_bool, 0x268E)]

    @function_hook("40 53 48 83 EC ? ? ? ? 48 8B D9 FF 90 ? ? ? ? 84 C0 74 ? 48 8B CB")
    def GetChargeFactor(self, this: "_Pointer[cGcPlayerWeapon]") -> c_float: ...

    @function_hook("48 83 EC ? 48 63 91 ? ? ? ? 8B CA")
    def GetChargeTime(self, this: "_Pointer[cGcPlayerWeapon]") -> c_float: ...


@partial_struct
class cGcApplication(cTkFSM):
    @partial_struct
    class Data(Structure):
        _total_size_ = 0x843B10
        # These are found in cGcApplication::Data::Data
        mRealityManager: Annotated[cGcRealityManager, 0x60]
        mGameState: Annotated[cGcGameState, 0xDB0]
        mSimulation: Annotated[cGcSimulation, 0x3D4D00]
        mHUDManager: Annotated[cGcHUDManager, 0x6286A0]

        @function_hook(
            "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 45 33 FF 48 C7 41 ? ? ? ? "
            "? 4C 89 39"
        )
        def Data(self, this: "_Pointer[cGcApplication.Data]"): ...

    @function_hook("40 53 48 83 EC 20 E8 ? ? ? ? 48 89")
    def Update(self, this: "_Pointer[cGcApplication]"): ...

    @function_hook("48 89 5C 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 45 33 F6 83 3D")
    def Construct(self, this: "_Pointer[cGcApplication]"): ...

    # There are tricky to get...
    # The game mostly sets a lot of the fields of the cGcApplication struct in some kind of "baked" way, we
    # don't see the offsets as with other structs, and instead we need to find the object, and then infer the
    # offset from the offset of the cGcApplication object. We can get this by seeing the value passed in to
    # cTkFSM::Construct in cGcApplication::Construct.
    # These properties can be found in cGcApplication::Construct
    mpData: Annotated[_Pointer[Data], 0x38]
    muPlayerSaveSlot: Annotated[int, Field(c_uint32, 0x40)]
    meGameMode: Annotated[int, Field(c_uint32, 0x44)]  # ePresetGameMode
    mbPaused: Annotated[bool, Field(c_bool, 0xB505)]
    mbMultiplayerActive: Annotated[bool, Field(c_bool, 0xB508)]


class cGcBeamEffect(Structure):
    @function_hook("40 53 48 83 EC ? 8B 41 ? 48 8B D9 A9 ? ? ? ? 76 ? 25 ? ? ? ? 3D ? ? ? ? 74 ? B0")
    def Prepare(self, this: "_Pointer[cGcBeamEffect]"): ...


class cGcLaserBeam(Structure):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 48 83 B9 ? ? ? ? ? 0F B6 FA 48 8B D9 77")
    def Fire(self, this: "_Pointer[cGcLaserBeam]", lbHitOnFirstFrame: Annotated[bool, c_bool]): ...


@partial_struct
class cGcMarkerList(Structure):
    maMarkerObjects: Annotated[std.vector[cGcMarkerPoint], Field(std.vector[cGcMarkerPoint])]

    @function_hook("48 89 5C 24 ? 55 57 41 56 48 83 EC ? 40 32 ED")
    def RemoveMarker(
        self,
        this: "_Pointer[cGcMarkerList]",
        lExampleMarker: _Pointer[cGcMarkerPoint],
    ) -> c_uint64: ...

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 54 41 56 41 57 48 83 EC ? F6 82"
    )
    def TryAddMarker(
        self,
        this: "_Pointer[cGcMarkerList]",
        lPoint: _Pointer[cGcMarkerPoint],
        lbUpdateTime: Annotated[bool, c_bool],
    ) -> c_char: ...


class cGcBaseBuildingManager(Structure):
    @function_hook("4C 8B DC 49 89 5B ? 49 89 6B ? 56 57 41 56 48 81 EC ? ? ? ? 41 0F B7 00")
    def GetBaseRootNode(
        self,
        this: "_Pointer[cGcBaseBuildingManager]",
        result: _Pointer[basic.TkHandle],
        luBaseIndex: c_uint64,  # _WORD *
        lbForceUpdateMatrix: c_bool,
    ) -> c_uint64:  # TkHandle *
        ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 81 EC ? ? ? ? 48 8B E9 49 63 F1")
    def AddHUDMarker(
        self,
        this: "_Pointer[cGcBaseBuildingManager]",
        leType: c_uint32,  # cGcMarkerPoint::eType
        lWorldMatrix: _Pointer[basic.cTkBigPos],
        liColourIndex: c_int32,
        lpacName: _Pointer[basic.cTkFixedString0x40],
    ): ...


class cGcBaseSearch(Structure):
    @static_function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 4C 89 70 ? 55 48 8D 68 ? 48 81 EC ? ? ? ? 66 0F 6F 05"
    )
    @staticmethod
    def FindNearestBaseInCurrentSystem(
        result: c_uint64,  # BaseIndex *
        lWorldPosition: _Pointer[basic.Vector3f],  # cTkVector3 *
        leBaseType: c_int32,  # ePersistentBaseTypes
    ): ...


class cGcBuilding(Structure):
    @function_hook("4C 8B DC 55 49 8D AB ? ? ? ? 48 81 EC ? ? ? ? 48 8B D1")
    def DestroyIntersectingVolcanoes(self, this: c_uint64): ...


@partial_struct
class cGcScanEvent(Structure):
    mMarker: Annotated[cGcMarkerPoint, Field(cGcMarkerPoint, 0x10)]
    mpEvent: Annotated[
        _Pointer[nmse.cGcScanEventData],
        Field(_Pointer[nmse.cGcScanEventData], 0x270),
    ]

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? "
        "? ? 33 F6"
    )
    def Construct(
        self,
        this: "_Pointer[cGcScanEvent]",
        leTable: c_int32,  # eScanTable
        lpEvent: _Pointer[nmse.cGcScanEventData],
        lpBuilding: _Pointer[cGcBuilding],
        lfStartTime: Annotated[float, c_float],
        lbMostImportant: Annotated[bool, c_bool],
        lpMission: c_uint64,  # std::pair<TkID<128>,cTkSeed> *
    ): ...

    @function_hook(
        "48 8B C4 55 53 56 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 33 F6 0F 29 78 ? 48 8B F9"
    )
    def CalculateMarkerPosition(self, this: "_Pointer[cGcScanEvent]"): ...

    @function_hook("4C 8B DC 55 57 49 8D AB ? ? ? ? 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 8B F9")
    def Update(slef, this: "_Pointer[cGcScanEvent]", lfTimeStep: Annotated[float, c_float]): ...

    @function_hook("48 8B C4 55 53 57 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 8B 91")
    def UpdateInteraction(self, this: "_Pointer[cGcScanEvent]"): ...

    @function_hook("4C 8B DC 55 56 49 8D 6B ? 48 81 EC ? ? ? ? 48 8B 81")
    def UpdateSpaceStationLocation(self, this: "_Pointer[cGcScanEvent]"): ...


class cGcApplicationLocalLoadState(Structure):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 80 B9 ? ? ? ? ? 48 8B F9 BB")
    def GetRespawnReason(self, this: "_Pointer[cGcApplicationLocalLoadState]") -> c_int64: ...


class cTkDynamicGravityControl(Structure):
    @partial_struct
    class cTkGravityPoint(Structure):
        _total_size_ = 0x20
        mCenter: Annotated[basic.Vector3f, 0x0]
        mfStrength: Annotated[float, Field(c_float, 0x10)]
        mfFalloffRadiusSqr: Annotated[float, Field(c_float, 0x14)]
        mfMaxStrength: Annotated[float, Field(c_float, 0x18)]

    @partial_struct
    class cTkGravityOBB(Structure):
        _total_size_ = 0xA0
        mUp: Annotated[basic.Vector3f, 0x0]
        mfConstantStrength: Annotated[float, Field(c_float, 0x10)]
        mfFalloffStrength: Annotated[float, Field(c_float, 0x14)]
        mTransformInverse: Annotated[basic.cTkMatrix34, 0x20]
        mUntransformedCentre: Annotated[basic.Vector3f, 0x60]
        mOBB: Annotated[basic.cTkAABB, 0x70]
        mfFalloffRadiusSqr: Annotated[float, Field(c_float, 0x90)]

    maGravityPoints: list["cTkDynamicGravityControl.cTkGravityPoint"]
    miNumGravityPoints: int
    maGravityOBBs: bytes

    @function_hook("33 C0 4C 8D 89 ? ? ? ? 89 81")
    def Construct(self, this: "_Pointer[cTkDynamicGravityControl]"): ...

    @function_hook("0F 28 05 ? ? ? ? 4C 8B C9")
    def cTkDynamicGravityControl(self, this: "_Pointer[cTkDynamicGravityControl]"): ...

    @function_hook("48 8B C4 55 56 57 41 54 41 57 48 81 EC")
    def GetGravity(
        self,
        this: "_Pointer[cTkDynamicGravityControl]",
        result: c_uint64,
        lPos: _Pointer[basic.Vector3f],
    ) -> c_uint64: ...

    @function_hook("48 83 EC ? 48 63 81 ? ? ? ? 0F 29 74 24")
    def UpdateGravityPoint(
        self,
        this: "_Pointer[cTkDynamicGravityControl]",
        lCentre: _Pointer[basic.Vector3f],
        lfRadius: Annotated[float, c_float],
        lfNewStrength: Annotated[float, c_float],
    ): ...


cTkDynamicGravityControl._fields_ = [
    ("maGravityPoints", cTkDynamicGravityControl.cTkGravityPoint * 0x9),
    ("miNumGravityPoints", c_int32),
    ("maGravityOBBs", basic.cTkClassPool[cTkDynamicGravityControl.cTkGravityOBB, 0x40]),
]


class Engine:
    @static_function_hook("40 53 44 8B D1 44 8B C9 41 C1 EA ? 41 81 E1 ? ? ? ? 48 8B DA")
    @staticmethod
    def ShiftAllTransformsForNode(node: basic.TkHandle, lShift: _Pointer[basic.Vector3f]): ...

    @static_function_hook("40 56 48 83 EC ? 44 8B C9")
    @staticmethod
    def GetNodeAbsoluteTransMatrix(
        node: basic.TkHandle,
        absMat: _Pointer[basic.cTkMatrix34],
    ): ...

    @static_function_hook("4C 89 4C 24 ? 48 89 4C 24 ? 55 56 41 57")
    @staticmethod
    def SetUniformArrayDefaultMultipleShaders(
        laShaderRes: c_uint64,
        liNumShaders: c_int32,
        name: c_char_p64,
        lpafData: c_uint64,  # float *
        liNumVectors: c_int32,
    ) -> c_int64: ...

    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 4D 63 F1 49 8B F8"
    )
    @staticmethod
    def SetMaterialUniformArray(
        materialRes: c_uint64,  # TkStrongType<int,TkStrongTypeIDs::TkResHandleID>
        name: c_char_p64,
        lpafData: c_uint64,  # float *
        liNumVectors: c_int32,
    ): ...

    @static_function_hook("48 83 EC ? FF C9")
    @staticmethod
    def SetOption(leParam: c_int32, lfValue: Annotated[float, c_float]) -> c_char: ...

    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 81 EC ? ? ? ? 48 8B BC 24 ? ? ? ? 48 "
        "8B D9 4C 8B 3D"
    )
    @staticmethod
    def AddResource(
        result: _Pointer[cTkSmartResHandle],
        liType: c_int32,
        lpcName: c_char_p64,
        liFlags: c_uint32,
        lAlternateMaterialId: _Pointer[cTkResourceDescriptor],
        unknown: c_uint64,
    ) -> c_uint64:  # cTkSmartResHandle *
        ...

    @static_function_hook(
        "48 89 5C 24 ? 57 48 81 EC ? ? ? ? 44 8B D2 44 8B CA 41 C1 EA ? 41 81 E1 ? ? ? ? 48 8B D9 45 85 D2 "
        "0F 84 ? ? ? ? 41 81 F9 ? ? ? ? 0F 84 ? ? ? ? 8B CA 48 8B 15 ? ? ? ? 81 E1 ? ? ? ? 48 8B 82 ? ? ? ? "
        "48 63 0C 88 48 8B 82 ? ? ? ? 48 8B 3C C8 48 85 FF 74 ? 8B 4F ? 8B C1 25 ? ? ? ? 41 3B C1 75 ? C1 E9 "
        "? 41 3B CA 75 ? 4C 8B CF 48 8D 4C 24 ? BA ? ? ? ? E8 ? ? ? ? 48 8B 0D ? ? ? ? 48 8D 05 ? ? ? ? 4C "
        "8D 4C 24 ? 48 89 44 24 ? 41 B8 ? ? ? ? 48 89 7C 24 ? 48 8B D3 E8 ? ? ? ? 48 8D 4C 24 ? E8 ? ? ? ? "
        "EB ? C7 03 ? ? ? ? 48 8B C3 48 8B 9C 24 ? ? ? ? 48 81 C4 ? ? ? ? 5F C3 CC CC CC CC CC 48 89 5C 24"
    )
    @staticmethod
    def AddGroupNode(
        result: _Pointer[basic.TkHandle], parent: basic.TkHandle, name: c_char_p64
    ) -> c_uint64: ...

    @static_function_hook("48 8B C4 55 53 56 57 41 57 48 8D 68 ? 48 81 EC ? ? ? ? 80 3D")
    def Initialise() -> c_char: ...

    @static_function_hook("48 89 5C 24 ? 57 48 83 EC ? 44 8B D2 44 8B C2")
    @staticmethod
    def GetModelNode(
        result: _Pointer[basic.TkHandle],
        node: basic.TkHandle,
    ) -> c_uint64:  # TkHandle *
        ...

    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 49 63 D8 44 8B CA 44 8B C2 41 C1 E9 ? 41 81 "
        "E0 ? ? ? ? 48 8B F1 45 85 C9 0F 84 ? ? ? ? 41 81 F8 ? ? ? ? 0F 84 ? ? ? ? 8B CA 48 8B 15 ? ? ? ? 81 "
        "E1 ? ? ? ? 48 8B 82 ? ? ? ? 48 63 0C 88 48 8B 82 ? ? ? ? 48 8B 2C C8 48 85 ED 0F 84 ? ? ? ? 8B 4D ? "
        "8B C1 25 ? ? ? ? 41 3B C0 75"
    )
    @staticmethod
    def AddNodes(
        result: _Pointer[basic.TkHandle],
        parent: basic.TkHandle,
        sceneGraphRes: Annotated[int, c_int32],  # TkStrongType<int,TkStrongTypeIDs::TkResHandleID>
    ) -> c_uint64:  # TkHandle *
        ...

    @static_function_hook("44 8B D2 44 8B CA 41 C1 EA ? 41 81 E1 ? ? ? ? 4C 8B C1 45 85 D2 74")
    @staticmethod
    def GetResourceHandleForNode(
        result: _Pointer[c_int32],  # TkStrongType<int,TkStrongTypeIDs::TkResHandleID> *
        lNode: basic.TkHandle,
    ) -> c_uint64:  # TkStrongType<int,TkStrongTypeIDs::TkResHandleID> *
        ...

    @static_function_hook("40 53 48 83 EC ? 33 DB 85 C9")
    @staticmethod
    def GetTexture(
        targetRes: Annotated[int, c_int32],  # TkStrongType<int,TkStrongTypeIDs::TkResHandleID>
    ) -> c_char_p64: ...

    @static_function_hook(
        "44 8B C9 44 8B C1 41 C1 E9 ? 41 81 E0 ? ? ? ? 45 85 C9 74 ? 41 81 F8 ? ? ? ? 74 ? 4C 8B 15 ? ? ? ? "
        "81 E1 ? ? ? ? 4D 8B 9A ? ? ? ? 49 8B 82 ? ? ? ? 49 63 14 8B 48 8B 0C D0 48 85 C9 74 ? 8B 49 ? 8B C1 "
        "25 ? ? ? ? 8B D1 41 3B C0 75 ? C1 E9 ? 41 3B C9 75 ? 49 8B 82"
    )
    @staticmethod
    def GetNodeType(node: basic.TkHandle) -> c_int64: ...

    @static_function_hook(
        "44 8B C9 44 8B C1 41 C1 E9 ? 41 81 E0 ? ? ? ? 45 85 C9 74 ? 41 81 F8 ? ? ? ? 74 ? 4C 8B 15 ? ? ? ? "
        "81 E1 ? ? ? ? 4D 8B 9A ? ? ? ? 49 8B 82 ? ? ? ? 49 63 14 8B 48 8B 0C D0 48 85 C9 74 ? 8B 49 ? 8B C1 "
        "25 ? ? ? ? 8B D1 41 3B C0 75 ? C1 E9 ? 41 3B C9 75 ? 81 E2"
    )
    @staticmethod
    def GetNodeNumChildren(node: basic.TkHandle) -> c_int32: ...

    @static_function_hook(
        "44 8B C9 44 8B C1 41 C1 E9 ? 41 81 E0 ? ? ? ? 45 85 C9 74 ? 41 81 F8 ? ? ? ? 74 ? 48 8B 15 ? ? ? ? "
        "81 E1 ? ? ? ? 48 8B 82 ? ? ? ? 48 63 0C 88 48 8B 82 ? ? ? ? 48 8B 14 C8 48 85 D2 74 ? 8B 4A ? 8B C1 "
        "25 ? ? ? ? 41 3B C0 75 ? C1 E9 ? 41 3B C9 75 ? 48 8B 42 ? 48 85 C0"
    )
    @staticmethod
    def GetNodeName(node: basic.TkHandle) -> c_char_p64: ...


class cEgResource(cTkResource):
    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 56 48 83 EC ? 48 8B 01 41 8B F0")
    def Load(
        self,
        this: "_Pointer[cEgResource]",
        lpacData: c_char_p64,
        liSize: Annotated[int, c_int32],
    ) -> c_char: ...


class cEgTextureResource(cEgResource):
    @function_hook("40 53 57 41 56 48 81 EC ? ? ? ? 45 8B F0")
    def Load(
        self,
        this: "_Pointer[cEgTextureResource]",
        lpcData: c_char_p64,
        liSize: Annotated[int, c_int32],
    ) -> c_char: ...


class GeometryStreaming:
    # @partial_struct
    class cEgGeometryStreamer(Structure):
        _mpGeometry: Annotated[int, Field(c_uint64, 0x10)]  # cEgGeometryResource*

        @property
        def mpGeometry(self):
            if self._mpGeometry:
                return cEgGeometryResource.from_address(self._mpGeometry)

        @partial_struct
        class cBufferData(Structure):
            meState: Annotated[int, Field(c_int32, 0x24)]

        @function_hook("48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 83 79 ? ? 41 0F B6 E8")
        def GetVertexBufferByHash(
            self,
            this: "_Pointer[GeometryStreaming.cEgGeometryStreamer]",
            liNameHash: Annotated[int, c_int32],
            a3: Annotated[bool, c_bool],
        ) -> c_int64: ...

        @function_hook("40 55 53 56 57 41 54 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 4C 8B FA")
        def RequestStream(
            self,
            this: "_Pointer[GeometryStreaming.cEgGeometryStreamer]",
            lpDescriptor: _Pointer[cTkResourceDescriptor],
        ): ...

        @static_function_hook("4C 8B DC 49 89 4B ? 55 57 41 57 48 81 EC ? ? ? ? 48 8B 29")
        @staticmethod
        def OnBufferLoadFinish(lpData: c_void_p): ...

    class cEgStreamRequests(Structure):
        @function_hook("40 56 48 83 EC ? 83 79 ? ? 48 8B F1 0F 29 74 24")
        def ProcessOnlyStreamRequests(
            self,
            this: "_Pointer[GeometryStreaming.cEgStreamRequests]",
            lfTimeout: Annotated[float, c_double],
        ): ...


@partial_struct
class cTkBuffer(Structure):
    _total_size_ = 0x30
    muSize: Annotated[int, Field(c_uint32, 0x0)]
    # 00000008     struct VkBuffer_T *mpD3D12Resource;
    # 00000010     TkDeviceMemory mpDeviceMemory;
    mpBufferData: Annotated[c_void_p, 0x28]


class cTkGraphicsAPI(Structure):
    @static_function_hook("48 89 5C 24 ? 57 48 83 EC ? 48 8B FA 48 8B D9 4D 85 C0")
    @staticmethod
    def GetVertexBufferData(
        lpVertexBuffer: _Pointer[cTkBuffer],
        lpVertexData: c_void_p,
        lpiVertexBufferSize: _Pointer[c_uint32],
    ): ...


@partial_struct
class cTkVertexLayoutRT(Structure):
    # TODO: Assumuming the same as 4.13. This is possibly untrue as the exported version has changed.
    miStride: Annotated[int, Field(c_int32, 0x4)]


@partial_struct
class cEgGeometryResource(cEgResource):
    _total_size_ = 0x770

    # Lots of this found in cEgGeometryResource::CloneOriginalVertDataToIndex and other methods
    muIndexCount: Annotated[int, Field(c_uint32, 0x1F8)]
    muVertexCount: Annotated[int, Field(c_uint32, 0x1FC)]
    muBvVertexCount: Annotated[int, Field(c_uint32, 0x200)]
    mb16BitIndices: Annotated[bool, Field(c_bool, 0x204)]
    mbUnknown0x205: Annotated[bool, Field(c_bool, 0x205)]  # Looks related to cTkGeometryData.ProcGenNodeNames
    # Looks like if the above is False (the default), then maybe cTkGeometryData.ProcGenNodeNames is written
    # to this + 0x350?
    mpIndexData: Annotated[c_void_p, 0x208]
    mpaVertPositionData: Annotated[basic.TkStd.tk_vector[_Pointer[basic.cTkVector3]], 0x220]
    mpaVertStreams: Annotated[
        basic.TkStd.tk_vector[c_void_p], 0x2A0
    ]  # This is actually in a cTkStackVector maybe....
    mMeshVertRStart: Annotated[basic.TkStd.tk_vector[c_int32], 0x2F8]  # maybe?
    mSkinMatOrder: Annotated[basic.TkStd.tk_vector[c_int32], 0x440]
    mVertexLayout: Annotated[cTkVertexLayoutRT, 0x488]  # Maybe?
    mStreamManager: Annotated[GeometryStreaming.cEgGeometryStreamer, 0x5D8]

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 68 ? 48 89 70 ? 48 89 78 ? 41 54 41 56 41 57 48 81 EC ? ? ? ? 49 8B E9"
    )
    def cEgGeometryResource(
        self,
        this: "_Pointer[cEgGeometryResource]",
        lsName: _Pointer[basic.cTkFixedString0x100],
        liFlags: Annotated[int, c_int32],
        lpResourceDescriptor: _Pointer[cTkResourceDescriptor],
    ): ...

    @function_hook("40 53 55 48 83 EC ? 65 48 8B 04 25 ? ? ? ? 48 8B DA")
    def Load(
        self,
        this: "_Pointer[cEgGeometryResource]",
        lpcData: c_char_p64,
        liSize: Annotated[int, c_int32],
    ) -> c_char: ...

    @function_hook("48 89 54 24 ? 55 57 41 57 48 8D AC 24 ? ? ? ? 48 81 EC")
    def CreateVertexInfoForHash(
        self,
        this: "_Pointer[cEgGeometryResource]",
        luHash: _Pointer[basic.cTkVector3],  # Not *technically* the type, I think because the hash is long.
    ): ...

    @function_hook("40 57 48 83 EC ? 83 B9 ? ? ? ? ? 48 8B F9 0F 8F")
    def CloneOriginalVertDataToIndex(
        self,
        this: "_Pointer[cEgGeometryResource]",
        liIndex: Annotated[int, c_int32],
    ): ...

    @function_hook("40 55 53 56 57 41 54 41 56 48 8D 6C 24 ? 48 81 EC ? ? ? ? 48 8B FA")
    def CloneInternal(self, this: "_Pointer[cEgGeometryResource]", lpRhsRes: _Pointer[cTkResource]): ...


class cTkResourceManager(Structure):
    @function_hook("44 89 44 24 ? 55 57 41 54 41 55")
    def AddResource(
        self,
        this: "_Pointer[cTkResourceManager]",
        result: _Pointer[cTkSmartResHandle],
        liType: c_enum32[enums.ResourceTypes],
        lsName: c_char_p64,
        lxFlags: c_uint32,
        lbUserCall: Annotated[bool, c_bool],
        lpResourceDescriptor: _Pointer[cTkResourceDescriptor],
        unknown: c_uint64,
    ) -> c_uint64:  # cTkSmartResHandle *
        ...

    @function_hook("4C 89 4C 24 ? 89 54 24 ? 53 55 48 81 EC")
    def FindResourceA(
        self,
        this: "_Pointer[cTkResourceManager]",
        liType: c_enum32[enums.ResourceTypes],
        lsName: c_char_p64,
        lpResourceDescriptor: _Pointer[cTkResourceDescriptor],
        a5: c_uint32,
        lbIgnoreDefaultFallback: Annotated[bool, c_bool],
        lbIgnoreKilled: Annotated[bool, c_bool],
        a8: Annotated[bool, c_bool],
    ) -> c_uint64:  # cTkSmartResHandle *
        ...


class cGcRewardManager(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 48 8B 3D ? ? ? ? 48 8B F1"
    )
    def GiveGenericReward(
        self,
        this: "_Pointer[cGcRewardManager]",
        lRewardID: _Pointer[basic.cTkFixedString[0x10]],
        lMissionID: _Pointer[basic.cTkFixedString[0x10]],
        lSeed: _Pointer[basic.cTkSeed],
        lbPeek: Annotated[bool, c_bool],
        lbForceShowMessage: Annotated[bool, c_bool],
        liOutMultiProductCount: c_uint64,
        lbForceSilent: Annotated[bool, c_bool],
        lInventoryChoiceOverride: c_int32,
        lbUseMiningModifier: Annotated[bool, c_bool],
    ) -> c_uint64: ...


@partial_struct
class cGcAlienPuzzleOption(Structure):
    _total_size_ = 0xF8
    Name: Annotated[basic.cTkFixedString[0x20], Field(basic.cTkFixedString[0x20], 0x20)]
    Rewards: Annotated[
        list[basic.cTkFixedString[0x10]],
        Field(basic.cTkDynamicArray[basic.cTkFixedString[0x10]], 0xC0),
    ]


@partial_struct
class cGcAlienPuzzleEntry(Structure):
    Id: Annotated[str, Field(basic.cTkFixedString[0x20], 0x0)]
    Options: Annotated[
        list[cGcAlienPuzzleOption],
        Field(basic.cTkDynamicArray[cGcAlienPuzzleOption], 0xD0),
    ]


@partial_struct
class cGcDestructableComponent(Structure):
    # Found in cGcDestructableComponent::Destroy
    mbDestroyed: Annotated[bool, Field(c_bool, 0x150)]

    @function_hook("4C 89 44 24 ? 89 54 24 ? 55 41 55")
    def Destroy(
        self,
        this: "_Pointer[cGcDestructableComponent]",
        leDestroyedBy: c_uint32,  # eDestroyedBy
        lDestroyedByPlayerId: c_uint64,  # const cTkUserIdBase<cTkFixedString<64,char> > *
    ): ...


@partial_struct
class cGcInteractionComponent(Structure):
    mpData: Annotated[_Pointer[nmse.cGcInteractionComponentData], 0x30]

    @function_hook("44 88 4C 24 ? 44 88 44 24 ? 48 89 54 24 ? 53")
    def GiveReward(
        self,
        this: "_Pointer[cGcInteractionComponent]",
        lOption: _Pointer[cGcAlienPuzzleOption],
        lbPeek: Annotated[bool, c_bool],
        lbForceShowMessage: Annotated[bool, c_bool],
        lbForceSilent: Annotated[bool, c_bool],
    ) -> c_uint64: ...

    @function_hook("48 8B 81 ? ? ? ? 48 85 C0 74 ? 48 83 B9 ? ? ? ? ? 75 ? 48 83 B9")
    def GetPuzzle(
        self,
        this: "_Pointer[cGcInteractionComponent]",
    ) -> c_uint64:  # cGcAlienPuzzleEntry *
        ...

    @static_function_hook(
        "4C 8B DC 48 83 EC ? 49 C7 43 ? ? ? ? ? 41 C7 43 ? ? ? ? ? 83 FA ? 75 ? 48 8D 05 ? ? ? ? 45 33 C0 49 "
        "89 43 ? 4D 8D 4B ? 49 8D 43 ? 49 89 43 ? 48 8D 15 ? ? ? ? 49 8D 43 ? 49 89 43 ? E8 ? ? ? ? 48 8B 84 "
        "24 ? ? ? ? 48 83 C4 ? C3 48 8D 84 24 ? ? ? ? 48 89 44 24 ? 48 8D 54 24 ? 48 8D 84 24 ? ? ? ? 48 89 "
        "44 24 ? 0F 28 44 24 ? 66 0F 7F 44 24 ? E8 ? ? ? ? 48 8B 84 24 ? ? ? ? 48 83 C4 ? C3 CC CC CC CC CC "
        "CC CC CC CC CC CC CC CC 48 89 5C 24 ? 57 48 83 EC ? 33 FF"
    )
    @staticmethod
    def FindFirstTypedComponent(
        lNodeHandle: basic.TkHandle,
        lbSameModelOnly: Annotated[bool, c_bool],
    ) -> c_uint64:  # cGcInteractionComponent *
        ...


@partial_struct
class cTkInputPort(Structure):
    mButtons: Annotated[
        basic.cTkBitArray[c_uint64, 512],
        Field(basic.cTkBitArray[c_uint64, 512], 0x108),
    ]
    mButtonsPrev: Annotated[
        basic.cTkBitArray[c_uint64, 512],
        Field(basic.cTkBitArray[c_uint64, 512], 0x148),
    ]

    @function_hook("40 57 48 83 EC ? 48 83 79 ? ? 44 8B CA")
    def SetButton(
        self,
        this: "_Pointer[cTkInputPort]",
        leIndex: c_int32,
    ): ...

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 41 8B D8 8B FA 48 8B F1 45 84 C9")
    def GetButton(
        self,
        this: "_Pointer[cTkInputPort]",
        leIndex: c_int32,
        leValidation: c_int32,
        lbDebugOnly: Annotated[bool, c_bool],
    ) -> c_uint8: ...


@partial_struct
class cGcBinoculars(Structure):
    # This and mpBinocularInfoGui found in cGcBinoculars::UpdateScanBarProgress
    mfScanProgress: Annotated[float, Field(c_float, 0x24)]
    # Found in cGcBinoculars::SetMarker at the top
    mMarkerModel: Annotated[basic.TkHandle, 0x7B0]
    mpBinocularInfoGui: Annotated[_Pointer[cGcNGui], 0x800]

    @function_hook("40 55 41 56 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 80 3D")
    def SetMarker(self, this: "_Pointer[cGcBinoculars]"): ...

    @function_hook("40 53 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 8D 54 24")
    def GetRange(self, this: "_Pointer[cGcBinoculars]") -> c_float: ...

    @function_hook("48 8B C4 55 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 89 70")
    def UpdateTarget(self, this: "_Pointer[cGcBinoculars]", lfTimeStep: Annotated[float, c_float]): ...

    @function_hook("40 53 48 83 EC ? 48 8B 91 ? ? ? ? 48 8B D9 F3 0F 11 49")
    def UpdateScanBarProgress(
        self, this: "_Pointer[cGcBinoculars]", lfScanProgress: Annotated[float, c_float]
    ):
        """Called each frame while scanning to set the cGcBinoculars.mfScanProgress from the lfScanProgress
        argument of this function."""
        ...

    @function_hook(
        "48 8B C4 55 53 56 57 41 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8B F1 48 8B 0D"
    )
    def UpdateRayCasts(
        self,
        this: "_Pointer[cGcBinoculars]",
        lTargetInfo: c_uint64,  # cTkContactPoint *
    ): ...

    @function_hook("48 8B C4 4C 89 48 ? 44 89 40 ? 48 89 48")
    def PopulateDiscoveryInfo(
        self,
        this: "_Pointer[cGcBinoculars]",
        lDiscoveryInfo: c_uint64,  # DiscoveryResolver::DiscoveryInfo *
        lpTargetNode: basic.TkHandle,
        lpTargetAttachment: c_uint64,  # cTkAttachmentPtr
        lbSubmitDiscovery: Annotated[bool, c_bool],
        lbSilent: Annotated[bool, c_bool],
    ): ...


class cTkFSMState(Structure):
    @function_hook(signature="4C 8B 51 ? 4D 8B D8")
    def StateChange(
        self,
        this: "_Pointer[cTkFSMState]",
        lNewStateID: _Pointer[basic.cTkFixedString[0x10]],
        lpUserData: c_void_p,
        lbForceRestart: Annotated[bool, c_bool],
    ): ...


class cGcPlayerNotifications(Structure):
    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 81 EC ? ? ? ? 44 8B 81")
    def AddTimedMessage(
        self,
        this: "_Pointer[cGcPlayerNotifications]",
        lsMessage: _Pointer[basic.cTkFixedString[512]],
        lfDisplayTime: Annotated[float, c_float],
        lColour: _Pointer[basic.Colour],
        liAudioID: c_uint32,
        lIcon: _Pointer[cTkSmartResHandle],
        # Note: The following fields have changed since 4.13... Might need to confirm...
        unknown: c_uint64,
        unknown2: c_uint32,
        lbShowMessageBackground: Annotated[bool, c_bool],
        lbShowIconGlow: Annotated[bool, c_bool],
    ): ...


@partial_struct
class cGcSky(Structure):
    eStormState = enums.eStormState

    # Found in cGcSky::SetSunAngle
    mSunDirection: Annotated[basic.Vector3f, Field(basic.Vector3f, 0x500)]

    @function_hook("40 53 55 56 57 41 56 48 83 EC ? 4C 8B 15")
    def SetStormState(self, this: "_Pointer[cGcSky]", leNewState: c_enum32[eStormState]): ...

    @function_hook("40 53 48 83 EC ? 0F 28 C1 0F 29 7C 24 ? F3 0F 5E 05")
    def SetSunAngle(self, this: "_Pointer[cGcSky]", lfAngle: Annotated[float, c_float]): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 55 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? "
        "48 8B D9"
    )
    def Update(self, this: "_Pointer[cGcSky]", lfTimeStep: Annotated[float, c_float]): ...

    @function_hook("48 8B C4 53 48 81 EC ? ? ? ? 4C 8B 05 ? ? ? ? 48 8B D9")
    def UpdateSunPosition(self, this: "_Pointer[cGcSky]", lfAngle: Annotated[float, c_float]): ...


class sTerrainEditData(Structure):
    mVoxelType: int
    mShape: int
    mCustom1: int
    mCustom2: int

    _fields_ = [
        ("mVoxelType", c_uint8, 3),
        ("mShape", c_uint8, 1),
        ("mCustom1", c_uint8, 3),
        ("mCustom2", c_uint8, 1),
    ]


class cGcTerrainEditorBeam(Structure):
    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? "
        "? ? 48 8B F2"
    )
    def Fire(
        self,
        this: "_Pointer[cGcTerrainEditorBeam]",
        lvTargetPos: _Pointer[basic.cTkPhysRelVec3],
        lpTargetBody: c_uint64,  # cTkRigidBody *
        lpOwnerConcept: c_uint64,  # cGcOwnerConcept *
        leStatType: c_enum32[enums.cGcStatsTypes],
        lbVehicle: Annotated[bool, c_bool],
    ) -> c_char: ...

    @function_hook("48 89 5C 24 ? 48 89 7C 24 ? 55 48 8D 6C 24 ? 48 81 EC ? ? ? ? 0F 28 05 ? ? ? ? 48 8B D9")
    def StartEffect(self, this: "_Pointer[cGcTerrainEditorBeam]"): ...

    @function_hook("4C 89 44 24 18 55 53 56 57 41 54 41 55 41 56 48 8D AC 24 ?? FE FF FF 48")
    def ApplyTerrainEditStroke(
        self,
        this: "_Pointer[cGcTerrainEditorBeam]",
        lEditData: sTerrainEditData,
        lImpact: c_uint64,  # cGcProjectileImpact *
    ) -> c_int64: ...

    @function_hook("48 8B C4 4C 89 40 ? 48 89 48 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8")
    def ApplyTerrainEditFlatten(
        self,
        this: "_Pointer[cGcTerrainEditorBeam]",
        lEditData: sTerrainEditData,
        lImpact: c_uint64,  # cGcProjectileImpact *
    ) -> c_uint64: ...


class cGcLocalPlayerCharacterInterface(Structure):
    @function_hook("40 53 48 83 EC 20 48 8B 1D ?? ?? ?? ?? 48 8D 8B ?? ?? ?? 00 E8 ?? ?? ?? 00")
    def IsJetpacking(self, this: "_Pointer[cGcLocalPlayerCharacterInterface]") -> c_bool: ...


class cGcSpaceshipComponent(Structure):
    @function_hook("48 89 5C 24 18 48 89 54 24 10 57 48 83 EC 70 41 0F B6 F8")
    def Eject(
        self,
        this: "_Pointer[cGcSpaceshipComponent]",
        lpPlayer: _Pointer[cGcPlayer],
        lbAnimate: Annotated[bool, c_bool],
        lbForceDuringCommunicator: Annotated[bool, c_bool],
    ): ...


@partial_struct
class cGcSpaceshipWarp(Structure):
    mePulseDriveState: Annotated[c_enum32[enums.EPulseDriveState], 0xA4]
    mfPulseDriveTimer: Annotated[float, Field(c_float, 0xB4)]
    mfPulseDriveFuelTimer: Annotated[float, Field(c_float, 0xB8)]
    mfPulseDriveTimer: Annotated[float, Field(c_float, 0x1A8)]
    mfPulseDriveFuelTimer: Annotated[float, Field(c_float, 0x1AC)]

    @function_hook("F3 0F 11 4C 24 ? 55 57 41 56 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 80 3D")
    def UpdatePulseDrive(
        self,
        this: "_Pointer[cGcSpaceshipWarp]",
    ): ...

    @function_hook(
        "48 83 EC ? 48 8B 0D ? ? ? ? 41 B9 ? ? ? ? 48 81 C1 ? ? ? ? C7 44 24 ? ? ? ? ? BA ? ? ? ? 45 8D 41 ? "
        "E8 ? ? ? ? 48 85 C0 74 ? 66 0F 6E 40"
    )
    def GetPulseDriveFuelFactor(self, this: "_Pointer[cGcSpaceshipWarp]") -> c_float: ...


@partial_struct
class cGcSpaceshipWeapons(Structure):
    # These can be found in cGcSpaceshipWeapons::GetHeatFactor and cGcSpaceshipWeapons::GetOverheatProgress
    # This enum corresponds to the element in the following 3 arrays by index.
    meWeaponMode: Annotated[c_enum32[enums.cGcShipWeapons], 0xA4]
    mafWeaponHeat: Annotated[list[float], Field(c_float * 7, 0x5FA4)]
    mafWeaponOverheatTimer: Annotated[list[float], Field(c_float * 7, 0x5FC0)]
    mabWeaponOverheated: Annotated[list[bool], Field(c_bool * 7, 0x5FDC)]

    @function_hook("48 63 81 ?? ?? 00 00 80 BC 08 ?? ?? 00 00 00 74 12")
    def GetOverheatProgress(self, this: "_Pointer[cGcSpaceshipWeapons]") -> c_float: ...

    @function_hook("48 8B C4 48 89 70 ? 57 48 81 EC ? ? ? ? 83 79")
    def GetAverageBarrelPos(
        self,
        this: "_Pointer[cGcSpaceshipWeapons]",
        result: _Pointer[basic.cTkPhysRelVec3],
    ) -> c_uint64:  # cTkPhysRelVec3 *
        ...

    @function_hook(
        "40 53 48 83 EC ? 48 8B 41 ? 48 8B D9 0F BF 0D ? ? ? ? 48 8B 50 ? E8 ? ? ? ? 48 85 C0 0F 84"
    )
    def GetCurrentShootPoints(
        self,
        this: "_Pointer[cGcSpaceshipWeapons]",
    ) -> c_uint64:  # cGcShootPoint *
        ...

    @function_hook("48 63 81 ? ? ? ? F3 0F 10 84 81")
    def GetHeatFactor(self, this: "_Pointer[cGcSpaceshipWeapons]") -> c_float: ...


@partial_struct
class cGcPlayerCharacterComponent(Structure):
    mbClonedJetpackMaterials: Annotated[bool, Field(c_bool, 0xCE0)]

    @function_hook("48 8B C4 55 53 56 57 41 56 48 8D 68 A1 48 81 EC 90 00 00")
    def SetDeathState(self, this: c_uint64): ...

    @function_hook("40 55 53 56 57 41 54 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 45 33 F6")
    def Update(
        self,
        this: "_Pointer[cGcPlayerCharacterComponent]",
        lfTimeStep: Annotated[float, c_float],
    ): ...


class cGcTextChatInput(Structure):
    @function_hook("40 55 53 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 80 3A")
    def ParseTextForCommands(
        self,
        this: "_Pointer[cGcTextChatInput]",
        lMessageText: _Pointer[basic.cTkFixedString[0x3FF]],
    ): ...


class cGcTextChatManager(Structure):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 48 8D 91 ? ? ? ? 33 FF")
    def Construct(self, this: "_Pointer[cGcTextChatManager]"): ...

    @function_hook("40 53 48 81 EC ? ? ? ? F3 0F 10 05")
    def Say(
        self,
        this: "_Pointer[cGcTextChatManager]",
        lsMessageBody: _Pointer[basic.cTkFixedString[0x3FF]],
        lbSystemMessage: Annotated[bool, c_bool],
    ): ...


class cGcNotificationSequenceStartEvent(Structure):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 48 8B 81 ? ? ? ? 48 8D 91 ? ? ? ? 44 8B 81")
    def DeepInterstellarSearch(self, this: "_Pointer[cGcNotificationSequenceStartEvent]") -> c_char: ...


class PlanetGenerationQuery(Structure): ...


class cGcScanEventSolarSystemLookup(Structure): ...


class cGcScanEventManager(Structure):
    @static_function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 8B B1 ? ? ? ? 48 8B DA")
    @staticmethod
    def PassesPlanetInfoChecks(
        lPlanet: _Pointer[PlanetGenerationQuery],
        lSolarSystemLookup: _Pointer[cGcScanEventSolarSystemLookup],
        lbAbandonedSystemInteraction: Annotated[bool, c_bool],
        leBuildingClass: c_uint32,  # eBuildingClass
        lbIsAbandonedOrEmptySystem: Annotated[bool, c_bool],
    ) -> c_bool: ...


class cGcPlanetGenerator(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? "
        "? ? ? 4D 8B F8 C6 85"
    )
    def Generate(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lPlanetData: _Pointer[nmse.cGcPlanetData],
        lGenerationData: _Pointer[nmse.cGcPlanetGenerationInputData],
        lpPlanet: _Pointer[cGcPlanet],
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 50 ? 48 89 48 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 "
        "EC ? ? ? ? 4C 63 B2"
    )
    def GenerateCreatureRoles(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lPlanetData: _Pointer[nmse.cGcPlanetData],
        lUA: c_uint64,
    ): ...

    @function_hook(
        "48 8B C4 48 89 50 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 "
        "? 33 F6"
    )
    def GenerateCreatureInfo(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lPlanetData: _Pointer[nmse.cGcPlanetData],
        lRole: _Pointer[nmse.cGcCreatureRoleData],
    ): ...

    @function_hook(
        "4C 89 4C 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? "
        "B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B 0D"
    )
    def GenerateQueryInfo(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lQueryData: _Pointer[PlanetGenerationQuery],
        lGenerationData: _Pointer[nmse.cGcPlanetGenerationInputData],
        lUA: c_uint64,
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 68 ? 48 89 70 ? 4C 89 48 ? 57 41 54 41 55 41 56 41 57 48 81 EC ? ? ? ? 4C "
        "8B E1"
    )
    def FillCreatureSpawnDataFromDescription(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lRole: _Pointer[nmse.cGcCreatureRoleData],
        lSpawnData: _Pointer[nmse.cGcCreatureSpawnData],
        lPlanetData: _Pointer[nmse.cGcPlanetData],
    ): ...


class cGcGalaxyAttributesAtAddress(Structure): ...


class cGcSolarSystemGenerator(Structure):
    class GenerationData(Structure): ...

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? "
        "E8 ? ? ? ? 48 2B E0 33 F6"
    )
    def GenerateQueryInfo(
        self,
        this: "_Pointer[cGcSolarSystemGenerator]",
        lSeed: _Pointer[basic.cTkSeed],
        lAttributes: _Pointer[cGcGalaxyAttributesAtAddress],
        lData: "_Pointer[cGcSolarSystemGenerator.GenerationData]",
    ): ...


class cGcDiscoveryPageData(Structure): ...


class cGcFrontendTextInput(Structure): ...


class cGcFrontendModelRenderer(Structure): ...


class cGcFrontendPageDiscovery(Structure):
    @function_hook(
        "4C 89 4C 24 ? 4C 89 44 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D "
        "AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B 99"
    )
    def DoDiscoveryView(
        self,
        this: "_Pointer[cGcFrontendPageDiscovery]",
        lPageData: _Pointer[cGcDiscoveryPageData],
        lFrontEndTextInput: _Pointer[cGcFrontendTextInput],
        lFronteEndModelRenderer: _Pointer[cGcFrontendModelRenderer],
    ): ...

    @static_function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 56 41 57 48 8D 6C 24 ? 48 81 EC ? ? ? ? 48 8D 05 ? "
        "? ? ? 41 8B F9"
    )
    @staticmethod
    def GetDiscoveryHintString(
        result: _Pointer[basic.cTkFixedString[0x40]],
        leTileType: c_uint32,  # eTileType
        leCreatureType: c_enum32[enums.cGcCreatureTypes],
        leRarity: c_enum32[enums.cGcRarity],
        leActiveTime: c_enum32[enums.cGcCreatureActiveTime],
        leHemisphere: c_enum32[enums.cGcCreatureHemiSphere],
    ): ...


class cGcFrontendPage(Structure): ...


class cGcFrontendPagePortalRunes(Structure):
    @static_function_hook("48 8B C4 44 88 48 20 44 88 40 18 48 89 50 10 55 53 56 57 41 54")
    @staticmethod
    def CheckUAIsValid(
        lTargetUA: c_uint64,
        lModifiedUA: "_Pointer[cGcGalacticVoxelCoordinate]",
        lbDeterministicRandom: Annotated[bool, c_bool],
        a4: Annotated[bool, c_bool],
    ) -> c_bool: ...

    @function_hook("48 89 54 24 ? 48 89 4C 24 ? 55 53 57 41 54 41 55 41 57")
    def DoInteraction(
        self,
        this: "_Pointer[cGcFrontendPagePortalRunes]",
        lpPage: _Pointer[cGcFrontendPage],
    ): ...


class cGcGalaxyVoxelAttributesData(nmse.cGcGalaxyVoxelAttributesData):
    @function_hook("33 C0 0F 57 C0 0F 11 01 0F 11 41 ? 0F 11 41 ? 48 89 41 ? 48 89 41 ? 48 89 41 ? 48 89 41")
    def SetDefaults(self, this: "_Pointer[cGcGalaxyVoxelAttributesData]"): ...


class cGcGalaxyStarAttributesData(nmse.cGcGalaxyStarAttributesData):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 ED 48 8D B9 ? ? ? ? 48 89 6C 24"
    )
    def SetDefaults(self, this: "_Pointer[cGcGalaxyStarAttributesData]"): ...


class cGcGalaxyAttributeGenerator(Structure):
    @static_function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F BF 41")
    @staticmethod
    def ClassifyVoxel(
        lCoordinate: _Pointer[cGcGalacticVoxelCoordinate],
        lOutput: _Pointer[cGcGalaxyVoxelAttributesData],
    ): ...

    @static_function_hook("48 89 54 24 ? 55 53 56 57 41 54 41 55 41 57 48 8B EC 48 83 EC ? 48 8B F9")
    @staticmethod
    def ClassifyStarSystem(lUA: c_uint64, lOutput: _Pointer[cGcGalaxyStarAttributesData]): ...


class cGcGalaxyVoxelData(Structure): ...


class cGcGalaxyVoxelGenerator(nmse.cGcGalaxyStarAttributesData):
    @static_function_hook("48 8B C4 4C 89 40 ? 48 89 48 ? 55 53 56 57 41 56 48 8D A8")
    @staticmethod
    def Populate(
        lu64UniverseAddress: c_uint64,
        lVoxelData: _Pointer[cGcGalaxyVoxelData],
        lRootOffset: _Pointer[basic.Vector3f],
    ): ...


class cTkLanguageManager(Structure):
    @static_function_hook(
        "48 83 EC ? 65 48 8B 04 25 ? ? ? ? B9 ? ? ? ? 48 8B 00 8B 04 01 39 05 ? ? ? ? 0F 8F ? ? ? ? 48 8D 05 "
        "? ? ? ? 48 83 C4 ? C3 4C 89 00"
    )
    @staticmethod
    def GetInstance() -> c_uint64: ...


@partial_struct
class cTkLanguageManagerBase(Structure):
    meRegion: Annotated[c_enum32[enums.eLanguageRegion], Field(c_enum32[enums.eLanguageRegion], 0x8)]

    @function_hook("48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 57 C0 49 8B E8")
    def Translate(
        self,
        this: "_Pointer[cTkLanguageManagerBase]",
        lpacText: c_char_p64,
        lpacDefaultReturnValue: _Pointer[basic.TkID[0x20]],
    ) -> c_uint64: ...

    @function_hook("48 89 5C 24 ? 57 48 81 EC ? ? ? ? 33 DB")
    def Load(
        self,
        this: "_Pointer[cTkLanguageManagerBase]",
        a2: c_char_p64,
        a3: Annotated[bool, c_bool],
    ): ...


class cGcNameGenerator(Structure):
    @function_hook(
        "4C 89 4C 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? "
        "? 44 8B D2"
    )
    def GeneratePlanetName(
        self,
        this: "_Pointer[cGcNameGenerator]",
        lu64Seed: Annotated[int, c_uint64],
        lResult: _Pointer[basic.cTkFixedString[0x79]],
        lLocResult: _Pointer[basic.cTkFixedString[0x79]],
    ): ...


class cGcCreatureComponent(Structure):
    @function_hook("48 8B C4 55 56 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 8B 51")
    def Prepare(self, this: "_Pointer[cGcCreatureComponent]"): ...


class cEgSceneGraphResource(Structure):
    @function_hook("4C 89 44 24 ? 55 53 56 57 41 55 41 56 48 8D AC 24")
    def ParseData(
        self,
        this: "_Pointer[cEgSceneGraphResource]",
        lData: c_uint64,  # std::string *
        lpParent: c_uint64,  # cEgSceneNodeTemplate *
    ) -> c_char: ...


class cGcApplicationBootState(Structure):
    @function_hook("48 89 5C 24 ? 55 56 57 41 56 41 57 48 81 EC ? ? ? ? 45 33 F6")
    def Update(
        self,
        this: "_Pointer[cGcApplicationBootState]",
        lfTimeStep: Annotated[float, c_float],
    ): ...


class cGcPlayerDiscoveryHelper(Structure):
    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 4C 24 ? 57 48 81 EC ? ? ? ? 48 8B 1D")
    def GetDiscoveryWorth(
        self,
        this: "_Pointer[cGcPlayerDiscoveryHelper]",
        lDiscoveryData: _Pointer[cGcDiscoveryData],
    ) -> c_uint64: ...


@partial_struct
class MenuAction(Structure): ...


class cGcQuickActionMenu(Structure):
    @function_hook("44 88 44 24 ? 48 89 4C 24 ? 55 56 57 41 54 41 56")
    def TriggerAction(
        self,
        this: "_Pointer[cGcQuickActionMenu]",
        lAction: _Pointer[MenuAction],
        lbCalledAsMenu: Annotated[bool, c_bool],
    ): ...


class cGcPlayerExperienceDirector(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 4C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? "
        "? ? 48 2B E0 48 8B 99"
    )
    def Update(
        self,
        this: "_Pointer[cGcPlayerExperienceDirector]",
        lfTimeStep: Annotated[float, c_float],
    ): ...


@partial_struct
class cGcPurchaseableItem(Structure):
    # Found in cGcPurchaseableItem::Update
    mePurchaseState: Annotated[int, Field(c_int32, 0x0)]  # cGcPurchaseableItem::ePurchaseState
    mItemType: Annotated[int, Field(c_int32, 0x4)]  # cGcPurchaseableItem::ePurchaseableItem
    mItemResource: Annotated[cTkSmartResHandle, 0x8]
    mItemNode: Annotated[basic.TkHandle, 0xC]
    mbIsFree: Annotated[bool, Field(c_bool, 0x20)]
    mbIsGift: Annotated[bool, Field(c_bool, 0x21)]
    mbIsReward: Annotated[bool, Field(c_bool, 0x22)]
    mbAddAdditionalItem: Annotated[bool, Field(c_bool, 0x31)]
    mbCleanResource: Annotated[bool, Field(c_bool, 0x1061)]
    mLinkedEntitlementId: Annotated[basic.TkID0x10, 0x1068]
    mLinkedEntitlementRewardId: Annotated[basic.TkID0x10, 0x1078]

    @function_hook("F3 0F 11 4C 24 ? 55 53 41 54 41 56")
    def Update(
        self,
        this: "_Pointer[cGcPurchaseableItem]",
        lfTimeStep: Annotated[float, c_float],
        a3: c_int64,
        a4: c_uint64,
    ): ...


class cGcApplicationGameModeSelectorState(Structure):
    @function_hook(
        "48 8B C4 55 53 56 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 48 8B F9"
    )
    def Update(
        self,
        this: "_Pointer[cGcApplicationGameModeSelectorState]",
        lfTimeStep: Annotated[float, c_float],
        # NOTE: This may have more arguments... 4 total in 4.13 exe, quite a few in mac binary.
    ): ...


@static_function_hook(
    "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 54 41 55 41 56 41 57 48 83 EC ? 33 FF 48 8D 59"
)
def GenerateModdedFilepath(
    Src: c_char_p64,
    Result: c_char_p64,
    lpacResultDirectory: c_char_p64,
    lpacBaseFilename: c_char_p64,
    lpacDirectory: c_char_p64,
    lbIsGlobal: Annotated[bool, c_bool],
) -> c_uint64:  # Length of generated filename.
    """Generate the filepath for the modded file to be written.

    Parameters
    ----------
    Result
        The full path to the file to be written.
    lpacResultDirectory
        The full directory path the file will be written in.
    lpacBaseFilename
        The filename to be written.
    lpacDirectory
        The directory the file is to be written to relative to the archive root.
    lbIsGlobal
        Indicates whether the file is a global. This is different to a "globals" file. This refers to files
        which are outside of mods (generally the TkGraphicsSettings.mxml and TkGameSettings.mxml).
    """
    ...


@partial_struct
class cTkFileSystem(Structure):
    @partial_struct
    class Data(Structure):
        mbMountBanks: Annotated[bool, Field(c_bool, 0x4658)]
        mbBanksTransparent: Annotated[bool, Field(c_bool, 0x4659)]
        mbIsModded: Annotated[bool, Field(c_bool, 0x465A)]
        mbIsTampered: Annotated[bool, Field(c_bool, 0x465B)]
        mArchiveRoot: Annotated[basic.cTkFixedString0x100, 0x465C]
        mModArchiveRoot: Annotated[basic.cTkFixedString0x100, 0x475C]
        mWorkingRoot: Annotated[basic.cTkFixedString0x100, 0x485C]
        mArchiveMountPoint: Annotated[basic.cTkFixedString0x100, 0x495C]

        @function_hook(
            "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 54 41 55 41 56 41 57 48 81 EC ? ? ? ? 4C 8D 35"
        )
        def Data(
            self,
            this: _Pointer["cTkFileSystem.Data"],
            lbMountBanks: Annotated[bool, c_bool],
            lbBanksTransparent: Annotated[bool, c_bool],
        ) -> c_uint64:  # _Pointer[cTkFileSystem.Data]
            ...

        @function_hook("4C 8B DC 45 88 43 ? 41 57")
        def MountAllArchives(
            self,
            this: _Pointer["cTkFileSystem.Data"],
            result: c_uint64,  # This is a vector of cTkBankInfo's
            lbCheckTampered: c_bool,
        ): ...

    # NOTE: This pattern is bad. It contains bytes from the proceeding function.
    @function_hook(
        "48 8B 01 48 85 C0 74 ? 0F B6 80 ? ? ? ? C3 C3 CC CC CC CC CC CC CC CC CC CC CC CC CC CC CC 48 8B 01"
    )
    def IsModded(self, this: "_Pointer[cTkFileSystem]") -> c_bool: ...

    @static_function_hook(
        "48 83 EC ? 65 48 8B 04 25 ? ? ? ? B9 ? ? ? ? 48 8B 00 8B 04 01 39 05 ? ? ? ? 7F ? 48 8D 05 ? ? ? ? "
        "48 83 C4 ? C3 48 8D 0D ? ? ? ? E8 ? ? ? ? 83 3D ? ? ? ? ? 75 ? 48 8D 0D ? ? ? ? 48 C7 05"
    )
    @staticmethod
    def GetInstance() -> c_uint64: ...

    @function_hook("40 55 53 56 57 41 55 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 48 8D 45")
    def EnumerateDirectory(
        self,
        this: "_Pointer[cTkFileSystem]",
        lpacPath: c_char_p64,
        lpaacDirectoryNamesOut: _Pointer[c_char_p64],
        liNumEntries: c_int32,
        liMaxStringSize: c_int32,
    ) -> c_uint64: ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 81 EC ? ? ? ? 80 3A")
    def DoesFileExist(
        self,
        this: "_Pointer[cTkFileSystem]",
        lpacPath: c_char_p64,
        a3: c_char_p64,
        lbSearchWorkingRoot: Annotated[bool, c_bool],
    ) -> c_uint64:
        # If lbSearchWorkingRoot is True, then it will check the path relative to `this.mWorkingRoot` which is
        # the GAMEDATA folder. Otherwise it will search `this.mArchiveMountPoint`
        # Note: This doesn't actually really check if the file exists or not, but it's used a lot so it's a
        # good way to know if the game is trying to find a file or directory to do something with.
        ...

    @function_hook("4C 89 44 24 ? 55 53 56 57 41 54 48 8D 6C 24")
    def LoadModDirectory(
        self,
        this: "_Pointer[cTkFileSystem]",
        lpacPath: c_char_p64,
        a3: c_char_p64,
        liMaxDirectories: Annotated[int, c_int32],
        a5: Annotated[int, c_int32],
        a6: c_uint64,
    ) -> c_uint64: ...

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 4C 89 74 24 ? 55 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 48 "
        "8B DA 48 8B F1"
    )
    def LoadModSubDirectory(
        self,
        this: "_Pointer[cTkFileSystem]",
        lpacPath: c_char_p64,
        a3: c_char_p64,
        a4: Annotated[bool, c_bool],
        a5: Annotated[bool, c_bool],
        a6: c_uint64,
        a7: Annotated[bool, c_bool],
    ) -> c_bool: ...

    @function_hook("48 81 EC ? ? ? ? 41 B1")
    def CreatePath(self, this: "_Pointer[cTkFileSystem]", lpacPath: c_char_p64): ...

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B 7C 24 ? 49 8B F0")
    def Write(
        self,
        this: "_Pointer[cTkFileSystem]",
        lpData: c_void_p,
        liSize: c_uint64,
        liNumElements: c_uint64,
        lFile: c_uint64,  # FIOS2HANDLE *
    ) -> c_uint64: ...

    @function_hook("40 53 56 57 48 81 EC ? ? ? ? 45 85 C0")
    def Open(
        self,
        this: "_Pointer[cTkFileSystem]",
        lpacFileName: c_char_p64,
        leMode: c_enum32[enums.eFileOpenMode],
    ) -> c_uint64:  # FIOS2HANDLE *
        ...

    mpData: Annotated[_Pointer[Data], 0x0]


# Note: There is no corresponding class in the 4.13 binary, nor in the mac binary unfortunately.
# All method names are guessed.
@partial_struct
class cGcModManager(Structure):
    liModCount: Annotated[int, Field(c_int32, 0x4)]

    @partial_struct
    class ModInfo(Structure):
        # This Struct and it's info is mostly determined from
        _total_size_ = 0x640
        liIndex: Annotated[int, Field(c_uint16, 0x28)]
        # Looks like there might be another cTkFixedString0x80 here too based on the constructor.
        mModName: Annotated[basic.cTkFixedString0x80, 0xAA]
        lbUnknown0x12A: Annotated[bool, Field(c_bool, 0x12A)]
        lbUnknown0x12B: Annotated[bool, Field(c_bool, 0x12B)]
        # Looks like this might be 8 * 0x80's from 0x130
        lpacPath: Annotated[c_char_p, 0x530]
        liUnknown0x630: Annotated[int, Field(c_int32, 0x630)]
        lbUnknown0x634: Annotated[bool, Field(c_bool, 0x634)]
        lbHasGlobals: Annotated[bool, Field(c_bool, 0x635)]
        lbHasBaseBuildingParts: Annotated[bool, Field(c_bool, 0x636)]
        lbHasLocTable: Annotated[bool, Field(c_bool, 0x637)]
        lbAlsoHasBaseBuildingPartsButDifferent: Annotated[bool, Field(c_bool, 0x638)]  # ???

    @static_function_hook(
        "48 83 EC ? 65 48 8B 04 25 ? ? ? ? B9 ? ? ? ? 48 8B 00 8B 04 01 39 05 ? ? ? ? 0F 8F ? ? ? ? 48 8D 05 "
        "? ? ? ? 48 83 C4 ? C3 48 8D 0D"
    )
    @staticmethod
    def GetInstance() -> c_uint64: ...

    @function_hook("40 55 53 56 57 41 55 41 57 48 8D AC 24 ? ? ? ? B8")
    def LoadModdedData(
        self,
        this: "_Pointer[cGcModManager]",
        lbVREnabled: Annotated[bool, c_bool],
    ) -> c_bool: ...


class cTkMemoryManager(Structure):
    @function_hook("44 89 4C 24 ? 4C 89 44 24 ? 53")
    def Malloc(
        self,
        this: "_Pointer[cTkMemoryManager]",
        liSize: Annotated[int, c_int32],
        lpacFile: c_char_p64,
        liLine: Annotated[int, c_int32],
        lpacFunction: c_char_p64,
        liAlign: Annotated[int, c_int32],
        liPool: Annotated[int, c_int32],
    ):
        """Hello Games' internal memory allocation function. This is used extensively.
        Hook with extreme caution! Doing so may easily crash the game or cause it to run VERY slow."""
        ...


class cGcOptionsPageUI(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 33 DB 48 8D 79 ? 89 59"
    )
    def BeginList(
        self,
        this: "_Pointer[cGcOptionsPageUI]",
        lpacMainText: c_char_p64,
        lpacDescriptionText: c_char_p64,
        liCurrentValue: Annotated[int, c_int32],
        liDefaultValue: Annotated[int, c_int32],
        a6: _Pointer[c_int32],
    ): ...

    @function_hook("4C 89 44 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 57 41 54 48 8D 6C 24")
    def QualityOption(
        self,
        this: "_Pointer[cGcOptionsPageUI]",
        lpacOptionName: c_char_p64,
        lpacDescriptionLocKey: c_char_p64,
        leValue: c_enum32[enums.eGraphicsDetail],
        leDefaultValue: c_enum32[enums.eGraphicsDetail],
    ) -> c_uint64: ...

    @function_hook("40 53 48 83 EC ? 48 63 41 ? 48 8D 59")
    def ListOption(
        self,
        this: "_Pointer[cGcOptionsPageUI]",
        lpacOptionText: c_char_p64,
        liValue: Annotated[int, c_int32],
    ): ...


class cGcFrontendPageFunctions(Structure):
    @static_function_hook(
        "4C 89 4C 24 ? 4C 89 44 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 55 41 56 41 57 48 8D AC 24"
    )
    @staticmethod
    def DoEmptySlotPopup(
        lpPage: _Pointer[cGcFrontendPage],
        lpSlot: _Pointer[cGcNGuiLayer],
        lEmptySlotActions: c_uint64,  # std::vector<enum ePopupAction,TkSTLAllocatorShim<enum ePopupAction,4,-1> >  # noqa
        lIndex: _Pointer[nmse.cGcInventoryIndex],
        lpCurrentInventory: _Pointer[cGcInventoryStore],
    ): ...

    @static_function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? BB")
    @staticmethod
    def SetEmptySlotBackground(
        lpPage: _Pointer[cGcFrontendPage],
        lpSlot: _Pointer[cGcNGuiLayer],
        leChoice: Annotated[int, c_uint32],
        lbUseSpecialTechSlot: Annotated[bool, c_bool],
    ): ...

    @static_function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 55 57 41 54 41 55 41 56 48 8D 68 ? 48 81 EC ? ? ? ? 0F 29 78 ? 48 8D "
        "1D"
    )
    @staticmethod
    def SetPopupBasics(
        lpParentLayer: _Pointer[cGcFrontendPage],
        lpacTitle: c_char_p64,
        lColour: _Pointer[basic.Colour],
        lpacDescription: _Pointer[basic.cTkFixedString0x200],
        lpacSubtitle: _Pointer[basic.cTkFixedString0x200],
        lpacType: c_char_p64,
        lpacTechTreeCost: c_char_p64,
        lpacTechTreeCostAlt: c_char_p64,
        lbSpecialSubtitle: Annotated[bool, c_bool],
        liAmountToShow: Annotated[int, c_int32],
        lLayerIDOverride: c_uint64,  # __m128i *
    ) -> c_uint64:  # cGcNGuiLayer *
        ...


class cTkSystem(Structure):
    @function_hook("80 B9 ? ? ? ? ? 75 ? 83 3D")
    def IntegratedGPUActive(self, this: "_Pointer[cTkSystem]") -> c_bool: ...

    @static_function_hook(
        "40 53 48 83 EC ? 65 48 8B 04 25 ? ? ? ? B9 ? ? ? ? 48 8B 00 8B 04 01 39 05 ? ? ? ? 7F ? 48 8D 05 ? "
        "? ? ? 48 83 C4 ? 5B C3 90"
    )
    @staticmethod
    def GetInstance() -> c_uint64: ...


class cTkEngineSettings(Structure):
    @function_hook("48 83 EC ? 83 EA ? 74 ? 83 FA")
    def GetSettingSupport(
        self,
        this: "_Pointer[cTkEngineSettings]",
        leEngineSetting: c_uint32,  # eEngineSetting
    ) -> c_bool: ...


class cTkEngineUtils(Structure):
    @static_function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 41 8B F0 48 8B F9")
    @staticmethod
    def GetMasterModelNode(
        result: _Pointer[basic.TkHandle],
        lNode: basic.TkHandle,
        lDistance: c_int32,
    ) -> c_uint64:  # TkHandle *
        ...

    @static_function_hook("48 83 EC ? 49 8B C0 48 85 D2")
    @staticmethod
    def GetMatricesFromNode(
        lHandle: basic.TkHandle,
        lAbsoluteMatrix: _Pointer[basic.cTkMatrix34],
        lRelativeMatrix: _Pointer[basic.cTkMatrix34],
    ) -> c_char: ...

    @static_function_hook("89 4C 24 ? 53 55 41 55")
    @staticmethod
    def LoadResourcesFromDisk(lBalancing: Annotated[int, c_int32]) -> c_uint64: ...


class cTkMetaDataXML(Structure):
    @static_function_hook("4C 89 4C 24 ? 4C 89 44 24 ? 48 89 54 24 ? 48 89 4C 24 ? 53 48 83 EC")
    @staticmethod
    def Register(
        lpacName: c_char_p64,
        lWriteFunction: c_uint64,
        lReadFunction: c_uint64,
        lSaveFunction: c_uint64,
    ): ...

    @static_function_hook("48 89 5C 24 ? 48 89 7C 24 ? 48 8B 05")
    @staticmethod
    def GetLookup(lpacName: c_char_p64) -> c_uint64: ...


@partial_struct
class cGcPlayerCommunicator(Structure):
    # Found in cGcPlayerCommunicator::Update passed into cGcInteractionComponent::FindFirstTypedComponent
    mActiveNode: Annotated[basic.TkHandle, 0x78]

    @function_hook("F3 0F 11 4C 24 ? 4C 8B DC 55 57 49 8D AB ? ? ? ? 48 81 EC ? ? ? ? 8B 81")
    def Update(
        self,
        this: "_Pointer[cGcPlayerCommunicator]",
        lfTimeStep: Annotated[float, c_float],
    ): ...


@partial_struct
class cGcNGuiNodeInfo(Structure):
    # Found in cGcNGuiNodeInfo::Get. It's the same as 4.13 other than the maChildren type...
    mNode: Annotated[basic.TkHandle, 0x8]
    mString: Annotated[basic.cTkFixedString0x100, 0xC]
    mTypeName: Annotated[basic.cTkFixedString0x80, 0x10C]
    maChildren: Annotated["basic.TkStd.tk_vector[_Pointer[cGcNGuiNodeInfo]]", 0x190]

    @function_hook("48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 81 EC ? ? ? ? 4C 8B F9")
    def Get(self, this: "_Pointer[cGcNGuiNodeInfo]", lNode: basic.TkHandle): ...


@partial_struct
class cEgSceneNode(Structure):
    _total_size_ = 0x38
    mLookupHandle: Annotated[basic.TkHandle, 0x8]
    muNameHash: Annotated[int, Field(c_uint32, 0xC)]
    mResHandle: Annotated[cTkSmartResHandle, 0x10]
    muNetworkId: Annotated[int, Field(c_uint32, 0x14)]
    msName: Annotated[cTkSharedPtr[c_char_p64], 0x18]
    mpAltId: Annotated[cTkSharedPtr[cTkResourceDescriptor], 0x20]


@partial_struct
class cEgModelNode(cEgSceneNode):
    mpGeometryResource: Annotated[cTkTypedSmartResHandle[cEgGeometryResource], 0x38]
    muVertBufferIndex: Annotated[int, Field(c_uint32, 0x60)]

    @function_hook("48 8B C4 55 53 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 83 B9")
    def UpdateGeometry(self, this: "_Pointer[cEgModelNode]") -> c_char: ...


class cEgMaterialResource(cEgResource):
    pass


@partial_struct
class cEgMeshNode(cEgSceneNode):
    _total_size_ = 0xE0

    mpMaterialResource: Annotated[cTkTypedSmartResHandle[cEgMaterialResource], 0x38]
    mpParentModel: Annotated[_Pointer[cEgModelNode], 0x48]
    muBatchStart: Annotated[int, Field(c_uint32, 0x60)]
    muBatchCount: Annotated[int, Field(c_uint32, 0x64)]
    muBatchStartPhysics: Annotated[int, Field(c_uint32, 0x68)]
    muVertRStart: Annotated[int, Field(c_uint32, 0x6C)]
    muVertREnd: Annotated[int, Field(c_uint32, 0x70)]
    muVertRStartPhysics: Annotated[int, Field(c_uint32, 0x74)]
    muVertREndPhysics: Annotated[int, Field(c_uint32, 0x78)]
    muBvVertStart: Annotated[int, Field(c_uint32, 0x7C)]
    muBvVertEnd: Annotated[int, Field(c_uint32, 0x80)]
    muLodLevel: Annotated[int, Field(c_uint32, 0x84)]

    mfLodFade: Annotated[float, Field(c_float, 0x94)]
    mUserData: Annotated[basic.Vector4f, 0xA0]
    mpMasterParentModel: Annotated[_Pointer[cEgModelNode], 0xB0]
    miGeometryBufferIndex: Annotated[int, Field(c_int32, 0xB8)]

    @static_function_hook("48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 4C 8B F9 41 8B E8")
    @staticmethod
    def ParsingFunc(
        lAttributes: _Pointer[basic.cTkDynamicArray[nmse.cTkSceneNodeAttributeData]],
        lpResourceDescriptor: _Pointer[cTkResourceDescriptor],
        lxResourceFlags: Annotated[int, c_int32],
    ) -> c_uint64:  # cEgMeshNodeTemplate*
        ...


@partial_struct
class cEgRenderQueue(Structure):
    pass


class cEgRenderer(Structure):
    @static_function_hook("48 8B C4 44 89 40 ? 48 89 48 ? 55 53 56 41 54")
    @staticmethod
    def DrawMeshes(
        lRenderQueue: _Pointer[cEgRenderQueueBuffer],
        lsShaderContext: _Pointer[basic.TkID0x10],
        liShaderContextVariant: Annotated[int, c_uint32],
        a4: c_uint64,  # Not used?
        leOrder: Annotated[int, c_int32],  # Not used
        lbSinglePassStereo: Annotated[bool, c_bool],
        lFrustum: c_uint64,  # cEgFrustum *
        lpThreadRenderData: _Pointer[cEgThreadableRenderCall],
    ): ...

    @static_function_hook(
        "4C 89 44 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? "
        "48 81 EC ? ? ? ? 49 83 79"
    )
    @staticmethod
    def DrawRenderables(
        lRenderQueue: _Pointer[cEgRenderQueue],
        lFrustum: c_uint64,  # cEgFrustum *
        lNodeType: _Pointer[basic.TkID0x10],
        lsMaterialClass: c_char_p64,
        lsShaderContext: _Pointer[basic.TkID0x10],
        liShaderContextVariant: Annotated[int, c_uint32],
        a7: c_uint64,
        leOrder: Annotated[int, c_int32],
        liRenderFromIndex: Annotated[int, c_uint32],
        liRenderToIndex: Annotated[int, c_uint32],
        lpThreadData: _Pointer[cEgThreadableRenderCall],
        lbRenderStereo: Annotated[bool, c_bool],
        lbRenderStereoSinglePass: Annotated[bool, c_bool],
    ): ...

    @static_function_hook("48 8B C4 48 89 58 ? 48 89 78 ? 4C 89 70 ? 55 48 8D 68")
    @staticmethod
    def SetupMeshMaterial(
        lpMaterialResource: _Pointer[cEgMaterialResource],
        lShaderContext: c_void_p,  # const TkIDHashed<128> *
        liShaderContextVariant: Annotated[int, c_int32],  # GPU::eContextVariant
        lMeshRSTransform: _Pointer[basic.cTkMatrix34],
        lMeshPrevRSTransform: _Pointer[basic.cTkMatrix34],
        lViewMat: _Pointer[basic.cTkMatrix44],
        lProjMat: _Pointer[basic.cTkMatrix44],
        lViewProjMat: _Pointer[basic.cTkMatrix44],
        mUserData: basic.Vector4f,  # TODO: See if this actually needs to be a pointer?
        lfFade: Annotated[float, c_float],
        liLodIndex: Annotated[int, c_int32],
        a12: Annotated[int, c_int32],
        lpSkinMatrixRows: _Pointer[basic.Vector4f],
        lpPrevSkinMatrixRows: _Pointer[basic.Vector4f],
        liNumSkinMatrixRows: Annotated[int, c_int32],
        a16: c_void_p,  # unknown
        lbIsStereo: Annotated[bool, c_bool],
        lpThreadRenderData: c_void_p,  # cEgThreadableRenderCall *
        lpShaderBinding: c_void_p,  # cEgShaderUniformBufferBinding *
    ) -> c_char: ...

    @static_function_hook("48 89 5C 24 ? 48 89 6C 24 ? 56 57 41 54 41 56 41 57 48 83 EC ? 49 8B F0")
    @staticmethod
    def SetupMeshGeometry(
        a1: c_uint32,
        a2: c_uint64,
        a3: c_uint64,
        a4: c_uint64,
    ) -> c_bool: ...


@partial_struct
class cEgSceneNodeData(Structure):
    # These are found in a few Engine:: functions.
    mpRelativeTransformBuffer: Annotated[_Pointer[basic.cTkMatrix34], 0x48]
    mpPrevRelativeTransformBuffer: Annotated[_Pointer[basic.cTkMatrix34], 0x48]
    mpAbsoluteTransformBuffer: Annotated[_Pointer[basic.cTkMatrix34], 0x60]
    mpSceneNodeBuffer: Annotated[_Pointer[_Pointer[cEgSceneNode]], 0x88]
    mpTypeBuffer: Annotated[_Pointer[c_uint8], 0x98]
    mpHandleToIndexBuffer: Annotated[_Pointer[c_int32], 0xD8]
    miCurFrame: Annotated[int, Field(c_int32, 0x210)]


@partial_struct
class cEgSceneManager(Structure):
    mData: Annotated[cEgSceneNodeData, 0x0]


class cEgRendererBase(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 48 8B F9 49 8B E9 48 81 C1"
    )
    def CreateVertexBuffer(
        self,
        this: "_Pointer[cEgRendererBase]",
        luSize: Annotated[int, c_int32],
        lpData: c_void_p,
        lVertexDecl: _Pointer[cTkVertexLayoutRT],
        luVertexCount: Annotated[int, c_uint32],
        a6: Annotated[bool, c_bool],
        lbMappable: Annotated[bool, c_bool],
        lbPersistent: Annotated[bool, c_bool],
    ) -> c_uint64: ...


class EgInstancedModelExtension:
    class cEgInstancedMeshNode(Structure):
        @static_function_hook("48 8B C4 44 89 40 ? 48 89 50 ? 48 89 48 ? 55 56 48 8D A8")
        @staticmethod
        def RenderAsync(
            lRenderQueue: c_void_p,  # cEgRenderQueueBuffer *
            lsShaderContext: _Pointer[basic.TkID0x10],
            liShaderContextVariant: Annotated[int, c_int32],
            leOrder: Annotated[int, c_uint8],
            lbUseLightweightGeometry: Annotated[bool, c_bool],
            lbRenderStereo: Annotated[bool, c_bool],
            lpFrustum: c_void_p,  # const cEgFrustum *
            lpThreadRenderData: c_void_p,  # cEgThreadableRenderCall *
        ): ...


@partial_struct
class cTkModelResourceRenderer(Structure):
    meSyncStage: Annotated[int, Field(c_int32, 0x498)]  # EModelResourceRendererSyncStage

    @function_hook("40 55 53 57 41 54 41 55 41 56 48 8D AC 24 ? ? ? ? 48 81 EC")
    def Update(
        self,
        this: "_Pointer[cTkModelResourceRenderer]",
        lfTimeStep: Annotated[float, c_float],
        lbForceAnimUpdate: Annotated[bool, c_bool],
        a4: c_uint64,  # unknown
    ): ...


class cEgModules:
    PATT = (
        "48 89 05 ? ? ? ? E8 ? ? ? ? 48 39 3D ? ? ? ? 75 ? B9 ? ? ? ? E8 ? ? ? ? 48 85 C0 74 ? 48 89 78 ? 40 "
        "88 78 ? 48 89 78 ? 40 88 78"
    )
    mgpSceneManager: _Pointer[cEgSceneManager]
    mgpResourceManager: cTkResourceManager

    def find_variables(self):
        patt_addr = find_pattern_in_binary(self.PATT, False)
        if patt_addr:
            start_addr = BASE_ADDRESS + patt_addr
            offset = c_uint32.from_address(start_addr + 3)
            mgpSceneManager_offset = start_addr + offset.value + 7
            self.mgpSceneManager = map_struct(mgpSceneManager_offset, _Pointer[cEgSceneManager])

    @static_function_hook("40 57 48 83 EC ? 33 FF 48 89 5C 24")
    @staticmethod
    def Initialise(): ...


engine_modules = cEgModules()

# Dummy values to copy and paste to make adding new things quicker...
# class name(Structure):
#     @function_hook("")
#     def method(self, this: "_Pointer[name]"):
#         ...
