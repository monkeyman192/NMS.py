from ctypes import (
    c_uint8,
    c_uint32,
    c_int32,
    c_uint16,
    _Pointer,
    c_float,
    c_uint64,
    c_int64,
    c_void_p,
    c_char_p,
    c_bool,
    c_char,
)
from typing import Annotated, Optional

from pymhf.core.hooking import static_function_hook
from pymhf.core.hooking import function_hook, Structure
from pymhf.utils.partial_struct import partial_struct, Field
from pymhf.extensions.cpptypes import std
from pymhf.extensions.ctypes import c_enum32

import nmspy.data.basic_types as basic
import nmspy.data.exported_types as nmse
import nmspy.data.enums as enums

# Exported functions


@partial_struct
class cTkResource(Structure):
    # __vftable: Annotated[c_uint64, Field(c_uint64, 0)]
    miType: Annotated[
        c_enum32[enums.ResourceTypes], Field(c_enum32[enums.ResourceTypes], 0x8)
    ]
    msName: Annotated[
        basic.cTkFixedString[0x100], Field(basic.cTkFixedString[0x100], 0xC)
    ]
    mxFlags: Annotated[int, Field(c_int32, 0x10C)]
    mHandle: Annotated[int, Field(c_int32, 0x128)]


class AK(Structure):
    class SoundEngine(Structure):
        @static_function_hook(
            exported_name="?RegisterGameObj@SoundEngine@AK@@YA?AW4AKRESULT@@_KPEBD@Z"
        )
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
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 81 EC ? ? ? ? 0F 29 70 ? 0F 29 78 ? 48 8D A8 ? ? ? ? 48 83 E5 ? 48 8B 01 48 8B F9"
    )
    def EditElement(self, this: "_Pointer[cGcNGuiText]"): ...


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

    @function_hook(
        "48 83 EC ? 33 C9 4C 8B D2 89 4C 24 ? 49 8B C0 48 89 4C 24 ? 45 33 C9"
    )
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

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 54 24 ? 57 48 81 EC ? ? ? ? 44 8B 51"
    )
    def AddElement(
        self,
        this: "_Pointer[cGcNGuiLayer]",
        lpElement: "_Pointer[cGcNGuiLayer]",
        lbOnTheEnd: c_int64,
    ): ...


@partial_struct
class cGcNGui(Structure):
    mRoot: Annotated[cGcNGuiLayer, Field(cGcNGuiLayer)]


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

    @function_hook(
        "40 55 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 4C 8B F9 48 8B 0D ? ? ? ? 48 81 C1"
    )
    def RenderHeadsUp(self, this: "_Pointer[cGcShipHUD]"): ...


class cTkStopwatch(Structure):
    @function_hook("48 83 EC ? 48 8B 11 0F 29 74 24")
    def GetDurationInSeconds(self, this: "_Pointer[cTkStopwatch]") -> c_float: ...


class cGcRealityManager(Structure):
    @function_hook("48 8B C4 48 89 48 ? 55 53 56 57 41 54 41 56 48 8D A8")
    def Construct(self, this: "_Pointer[cGcRealityManager]"): ...

    @function_hook(
        "48 89 54 24 ? 48 89 4C 24 ? 55 53 41 54 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B DA 4C 8B E1"
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
class cGcPlayerState(Structure):
    # We can find this in cGcPlayerState::GetPlayerUniverseAddress, which, while not mapped, can be found
    # inside cGcQuickActionMenu::TriggerAction below the string QUICK_MENU_EMERGENCY_WARP_BAN.
    mLocation: Annotated[nmse.cGcUniverseAddressData, 0x180]
    miShield: Annotated[int, Field(c_int32, 0x1B0)]
    miHealth: Annotated[int, Field(c_int32, 0x1B4)]
    miShipHealth: Annotated[int, Field(c_int32, 0x1B8)]
    muUnits: Annotated[int, Field(c_uint32, 0x1BC)]
    muNanites: Annotated[int, Field(c_uint32, 0x1C0)]
    muSpecials: Annotated[int, Field(c_uint32, 0x1C4)]
    # Found in cGcPlayerShipOwnership::SpawnNewShip
    miPrimaryShip: Annotated[int, Field(c_uint32, 0xC4F0)]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 44 8B 81 ? ? ? ? 48 8D 2D"
    )
    def AwardUnits(
        self,
        this: "_Pointer[cGcPlayerState]",
        liChange: Annotated[int, c_int32],
    ) -> c_uint64: ...

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 44 8B 81 ? ? ? ? 48 8D 35"
    )
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


@partial_struct
class cGcPlayerShipOwnership(Structure):
    @partial_struct
    class sGcShipData(Structure):
        _total_size_ = 0x48

        mPlayerShipSeed: Annotated[basic.cTkSeed, 0x0]

    @function_hook(
        "48 89 5C 24 ? 55 56 57 41 54 41 56 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 45"
    )
    def UpdateMeshRefresh(self, this: "_Pointer[cGcPlayerShipOwnership]"): ...

    @function_hook(
        "48 8B C4 55 53 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 80 B9 ? ? ? ? ? 48 8B F1"
    )
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

    # Not sure about this...
    mShips: Annotated[list[sGcShipData], Field(sGcShipData * 12, 0x58)]
    # Both these found at the top of cGcPlayerShipOwnership::UpdateMeshRefresh
    mbShouldRefreshMesh: Annotated[bool, Field(c_bool, 0xA690)]
    mMeshRefreshState: Annotated[int, Field(c_uint32, 0xA694)]


@partial_struct
class cGcGameState(Structure):
    mPlayerState: Annotated[cGcPlayerState, 0xA950]
    # Found in cGcGameState::Update
    mPlayerShipOwnership: Annotated[cGcPlayerShipOwnership, 0xA2BD0]

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
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? F3 0F 10 91"
    )
    def Update(
        self, this: "_Pointer[cGcGameState]", lfTimeStep: Annotated[float, c_float]
    ): ...


class cTkFSM(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 ED 48 89 51"
    )
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

    @function_hook(
        "40 55 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 4C 8B F9 48 8B 0D ? ? ? ? 83 B9"
    )
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
        laEffectsDamageMultipliers: c_uint64,  # std::vector<cGcCombatEffectDamageMultiplier,TkSTLAllocatorShim<cGcCombatEffectDamageMultiplier,4,-1> > *
    ): ...

    @function_hook("40 53 48 81 EC E0 00 00 00 48 8B D9 E8 ?? ?? ?? ?? 83 78 10 05")
    def OnEnteredCockpit(self, this: "_Pointer[cGcPlayer]"): ...

    @function_hook(
        "40 53 48 83 EC 20 48 8B 1D ?? ?? ?? ?? E8 ?? ?? ?? ?? 83 78 10 05 75 ?? 48 8B"
    )
    def GetDominantHand(self, this: "_Pointer[cGcPlayer]") -> c_int64: ...

    @function_hook(
        "48 8B C4 55 53 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 78"
    )
    def Update(
        self, this: "_Pointer[cGcPlayer]", lfStep: Annotated[float, c_float]
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 57 48 81 EC ? ? ? ? 0F 29 70 ? 0F B6 F2"
    )
    def UpdateGraphics(
        self, this: "_Pointer[cGcPlayer]", lbSetNode: Annotated[bool, c_bool]
    ): ...

    @function_hook(
        "48 8B C4 55 53 56 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8B F2"
    )
    def Prepare(
        self, this: "_Pointer[cGcPlayer]", lpController: _Pointer[cGcPlayerController]
    ): ...

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B FA 48 8B D9 48 8B 15"
    )
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

    @function_hook(
        "48 8B C4 48 89 48 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D 6C 24"
    )
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
class GcEnvironmentProperties(Structure):
    AtmosphereEndHeight: Annotated[float, Field(c_float, 0x1C)]
    AtmosphereStartHeight: Annotated[float, Field(c_float, 0x20)]
    SkyAtmosphereHeight: Annotated[float, Field(c_float, 0x5C)]
    StratosphereHeight: Annotated[float, Field(c_float, 0x78)]


@partial_struct
class cGcDiscoveryData(Structure): ...


@partial_struct
class GcPlanetSkyProperties(Structure): ...


@partial_struct
class cGcPlanet(Structure):
    _total_size_ = 0xD9060
    # Most of these found in cGcPlanet::Construct or cGcPlanet::cGcPlanet
    miPlanetIndex: Annotated[int, Field(c_int32, 0x50)]
    mPlanetData: Annotated[nmse.cGcPlanetData, 0x60]
    # TODO: This field follows directly after the above one. Once we have the cGcPlanetData struct mapped
    # correctly we can remove the offset to make it just be determined automatically.
    mPlanetGenerationInputData: Annotated[cGcPlanetGenerationInputData, 0x3A60]
    mRegionMap: Annotated[cGcTerrainRegionMap, 0x3B80]
    mNode: Annotated[basic.TkHandle, 0xD73D8]
    mAtmosphereNode: Annotated[basic.TkHandle, 0xD73DC]
    mRingNode: Annotated[basic.TkHandle, 0xD73E4]
    mPosition: Annotated[basic.Vector3f, 0xD73F0]

    mpEnvProperties: Annotated[_Pointer[GcEnvironmentProperties], 0xD9058]
    mpSkyProperties: Annotated[_Pointer[GcPlanetSkyProperties], 0xD9060]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 45 33 FF 48 C7 41 ? ? ? ? ? 44 89 79"
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
    def UpdateClouds(
        self, this: "_Pointer[cGcPlanet]", lfTimeStep: Annotated[float, c_float]
    ): ...

    @function_hook("40 53 48 83 EC ? 83 B9 ? ? ? ? ? 48 8B D9 0F 29 74 24")
    def UpdateGravity(
        self,
        this: "_Pointer[cGcPlanet]",
        lfNewGravityMultiplier: Annotated[float, c_float],
    ): ...

    @function_hook("40 55 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 80 3D")
    def UpdateWeather(
        self, this: "_Pointer[cGcPlanet]", lfTimeStep: Annotated[float, c_float]
    ): ...


@partial_struct
class cGcSolarSystem(Structure):
    # These can be found in cGcSolarSystem::cGcSolarSystem
    mSolarSystemData: Annotated[nmse.cGcSolarSystemData, 0x0]
    maPlanets: Annotated[list["cGcPlanet"], Field(cGcPlanet * 6, 0x2630)]
    # Found in cGcPlayerState::StoreCurrentSystemSpaceStationEndpoint
    mSpaceStationNode: Annotated[basic.TkHandle, 0x51C068]

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 29 74 24 ? 48 8B F9 48 8B D9"
    )
    def cGcSolarSystem(self, this: "_Pointer[cGcSolarSystem]"): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 48 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 83 3D"
    )
    def Construct(self, this: "_Pointer[cGcSolarSystem]"): ...

    @function_hook("48 89 5C 24 ? 55 56 57 41 55 41 57 48 8B EC 48 83 EC ? 83 3D")
    def OnLeavePlanetOrbit(
        self, this: "_Pointer[cGcSolarSystem]", lbAnnounceOSD: Annotated[bool, c_bool]
    ):
        """lbAnnounceOSD not used."""
        ...

    @function_hook(
        "48 8B C4 55 41 54 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 89 58 ? 45 33 E4 44 39 25"
    )
    def OnEnterPlanetOrbit(
        self, this: "_Pointer[cGcSolarSystem]", lbAnnounceOSD: Annotated[bool, c_bool]
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8D 3D"
    )
    def Generate(
        self,
        this: "_Pointer[cGcSolarSystem]",
        lbUseSettingsFile: Annotated[bool, c_bool],
        lSeed: _Pointer[basic.GcSeed],
    ): ...

    @function_hook(
        "48 8B C4 55 53 56 41 55 41 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 44 0F 29 40"
    )
    def Update(
        self, this: "_Pointer[cGcSolarSystem]", lfTimeStep: Annotated[float, c_float]
    ): ...


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
    def IsOnboardOwnFreighter(
        self, this: "_Pointer[cGcPlayerEnvironment]"
    ) -> c_bool: ...

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
        "48 8B C4 48 89 48 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8B E9"
    )
    def UpdateRender(self, this: "_Pointer[cGcEnvironment]"):
        # TODO: There could be a few good functions to get which are called in here...
        ...


@partial_struct
class cGcSimulation(Structure):
    # Found in cGcSimulation::Update. Passed into cGcEnvironment::Update.
    mEnvironment: Annotated[cGcEnvironment, 0xAF790]
    mPlayer: Annotated[cGcPlayer, 0x24DE40]
    # Found in cGcSimulation::Update. Passed into cGcSolarSystem::Update.
    mpSolarSystem: Annotated[_Pointer[cGcSolarSystem], 0x24C670]

    @function_hook(
        "48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D 6C 24 ? 48 81 EC ? ? ? ? 45 33 FF"
    )
    def Construct(self, this: "_Pointer[cGcSimulation]"): ...

    @function_hook("48 8B C4 89 50 ? 55 48 8D 6C 24")
    def Update(
        self,
        this: "_Pointer[cGcSimulation]",
        leMode: c_uint32,  # SimulationUpdateMode
        lfTimeStep: Annotated[float, c_float],
    ): ...


@partial_struct
class cGcApplication(cTkFSM):
    @partial_struct
    class Data(Structure):
        # These are found in cGcApplication::Data::Data
        mRealityManager: Annotated[cGcRealityManager, 0x60]
        mGameState: Annotated[cGcGameState, 0xDB0]
        mSimulation: Annotated[cGcSimulation, 0x3D4D00]

        @function_hook(
            "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 45 33 FF 48 C7 41 ? ? ? ? ? 4C 89 39"
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
    @function_hook(
        "40 53 48 83 EC ? 8B 41 ? 48 8B D9 A9 ? ? ? ? 76 ? 25 ? ? ? ? 3D ? ? ? ? 74 ? B0"
    )
    def Prepare(self, this: "_Pointer[cGcBeamEffect]"): ...


class cGcLaserBeam(Structure):
    @function_hook(
        "48 89 5C 24 ? 57 48 83 EC ? 48 83 B9 ? ? ? ? ? 0F B6 FA 48 8B D9 77"
    )
    def Fire(
        self, this: "_Pointer[cGcLaserBeam]", lbHitOnFirstFrame: Annotated[bool, c_bool]
    ): ...


@partial_struct
class cGcMarkerPoint(Structure):
    # Size found in the vector allocator in cGcMarkerList::TryAddMarker
    _total_size_ = 0x260
    # Found in cGcMarkerPoint::Reset
    mPosition: Annotated[basic.cTkPhysRelVec3, 0x0]
    mCenterOffset: Annotated[basic.Vector3f, 0x20]
    mCustomName: Annotated[basic.cTkFixedString[0x40], 0x38]
    mCustomSubtitle: Annotated[basic.cTkFixedString[0x80], 0x78]
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

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 28 05 ? ? ? ? 48 8D 79"
    )
    def Reset(self, this: "_Pointer[cGcMarkerPoint]"): ...


@partial_struct
class cGcMarkerList(Structure):
    maMarkerObjects: Annotated[
        std.vector[cGcMarkerPoint], Field(std.vector[cGcMarkerPoint])
    ]

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


# TODO: Add/search for PersistentBaseBuffer data


class cGcBaseBuildingManager(Structure):
    @function_hook(
        "4C 8B DC 49 89 5B ? 49 89 6B ? 56 57 41 56 48 81 EC ? ? ? ? 41 0F B7 00"
    )
    def GetBaseRootNode(
        self,
        this: "_Pointer[cGcBaseBuildingManager]",
        result: _Pointer[basic.TkHandle],
        luBaseIndex: c_uint64,  # _WORD *
        lbForceUpdateMatrix: c_bool,
    ) -> c_uint64:  # TkHandle *
        ...

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 81 EC ? ? ? ? 48 8B E9 49 63 F1"
    )
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
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 33 F6"
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

    @function_hook(
        "4C 8B DC 55 57 49 8D AB ? ? ? ? 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 8B F9"
    )
    def Update(
        slef, this: "_Pointer[cGcScanEvent]", lfTimeStep: Annotated[float, c_float]
    ): ...

    @function_hook(
        "48 8B C4 55 53 57 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 8B 91"
    )
    def UpdateInteraction(self, this: "_Pointer[cGcScanEvent]"): ...

    @function_hook("4C 8B DC 55 56 49 8D 6B ? 48 81 EC ? ? ? ? 48 8B 81")
    def UpdateSpaceStationLocation(self, this: "_Pointer[cGcScanEvent]"): ...


class cGcApplicationLocalLoadState(Structure):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 80 B9 ? ? ? ? ? 48 8B F9 BB")
    def GetRespawnReason(
        self, this: "_Pointer[cGcApplicationLocalLoadState]"
    ) -> c_int64: ...


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
    @static_function_hook("40 53 48 83 EC ? 44 8B D1 44 8B C1")
    @staticmethod
    def ShiftAllTransformsForNode(
        node: basic.TkHandle, lShift: _Pointer[basic.Vector3f]
    ): ...

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
        name: c_uint64,  # char *
        lpafData: c_uint64,  # float *
        liNumVectors: c_int32,
    ) -> c_int64: ...

    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 4D 63 F1 49 8B F8"
    )
    @staticmethod
    def SetMaterialUniformArray(
        materialRes: c_uint64,  # TkStrongType<int,TkStrongTypeIDs::TkResHandleID>
        name: c_uint64,  # char *
        lpafData: c_uint64,  # float *
        liNumVectors: c_int32,
    ): ...

    @static_function_hook("48 83 EC ? FF C9")
    @staticmethod
    def SetOption(leParam: c_int32, lfValue: Annotated[float, c_float]) -> c_char: ...

    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 81 EC ? ? ? ? 48 8B BC 24 ? ? ? ? 48 8B D9 4C 8B 3D"
    )
    @staticmethod
    def AddResource(
        result: c_uint64,  # cTkSmartResHandle *
        liType: c_int32,
        lpcName: c_char_p,
        liFlags: c_uint32,
        lAlternateMaterialId: c_uint64,  # cTkResourceDescriptor *
        unknown: c_uint64,
    ) -> c_uint64:  # cTkSmartResHandle *
        ...

    @static_function_hook(
        "48 89 5C 24 ? 57 48 81 EC ? ? ? ? 44 8B D2 44 8B CA 41 C1 EA ? 41 81 E1 ? ? ? ? 48 8B D9 45 85 D2 0F 84 ? ? ? ? 41 81 F9 ? ? ? ? 0F 84 ? ? ? ? 8B CA 48 8B 15 ? ? ? ? 81 E1 ? ? ? ? 48 8B 82 ? ? ? ? 48 63 0C 88 48 8B 82 ? ? ? ? 48 8B 3C C8 48 85 FF 74 ? 8B 4F ? 8B C1 25 ? ? ? ? 41 3B C1 75 ? C1 E9 ? 41 3B CA 75 ? 4C 8B CF 48 8D 4C 24 ? BA ? ? ? ? E8 ? ? ? ? 48 8B 0D ? ? ? ? 48 8D 05 ? ? ? ? 4C 8D 4C 24 ? 48 89 44 24 ? 41 B8 ? ? ? ? 48 89 7C 24 ? 48 8B D3 E8 ? ? ? ? 48 8D 4C 24 ? E8 ? ? ? ? EB ? C7 03 ? ? ? ? 48 8B C3 48 8B 9C 24 ? ? ? ? 48 81 C4 ? ? ? ? 5F C3 CC CC CC CC CC 48 89 5C 24"
    )
    @staticmethod
    def AddGroupNode(
        result: _Pointer[basic.TkHandle], parent: basic.TkHandle, name: c_char_p
    ) -> c_uint64: ...


class cTkResourceManager(Structure):
    @function_hook("44 89 44 24 ? 55 57 41 54 41 55")
    def AddResource(
        self,
        this: "_Pointer[cTkResourceManager]",
        result: c_uint64,  # cTkSmartResHandle *
        liType: c_enum32[enums.ResourceTypes],
        lsName: c_char_p,
        lxFlags: c_uint32,
        lbUserCall: Annotated[bool, c_bool],
        lpResourceDescriptor: c_uint64,  # cTkResourceDescriptor *
        unknown: c_uint64,
    ) -> c_uint64:  # cTkSmartResHandle *
        ...

    @function_hook("4C 89 4C 24 ? 89 54 24 ? 53 55 48 81 EC")
    def FindResourceA(
        self,
        this: "_Pointer[cTkResourceManager]",
        liType: c_enum32[enums.ResourceTypes],
        lsName: c_char_p,
        lpResourceDescriptor: c_uint64,  # cTkResourceDescriptor *
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

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 41 8B D8 8B FA 48 8B F1 45 84 C9"
    )
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

    @function_hook(
        "48 8B C4 55 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 89 70"
    )
    def UpdateTarget(
        self, this: "_Pointer[cGcBinoculars]", lfTimeStep: Annotated[float, c_float]
    ): ...

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
        lIcon: c_uint64,  # cTkSmartResHandle*
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
    def SetStormState(
        self, this: "_Pointer[cGcSky]", leNewState: c_enum32[eStormState]
    ): ...

    @function_hook("40 53 48 83 EC ? 0F 28 C1 0F 29 7C 24 ? F3 0F 5E 05")
    def SetSunAngle(
        self, this: "_Pointer[cGcSky]", lfAngle: Annotated[float, c_float]
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 55 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 48 8B D9"
    )
    def Update(
        self, this: "_Pointer[cGcSky]", lfTimeStep: Annotated[float, c_float]
    ): ...

    @function_hook("48 8B C4 53 48 81 EC ? ? ? ? 4C 8B 05 ? ? ? ? 48 8B D9")
    def UpdateSunPosition(
        self, this: "_Pointer[cGcSky]", lfAngle: Annotated[float, c_float]
    ): ...


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
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 8B F2"
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

    @function_hook(
        "48 89 5C 24 ? 48 89 7C 24 ? 55 48 8D 6C 24 ? 48 81 EC ? ? ? ? 0F 28 05 ? ? ? ? 48 8B D9"
    )
    def StartEffect(self, this: "_Pointer[cGcTerrainEditorBeam]"): ...

    @function_hook(
        "4C 89 44 24 18 55 53 56 57 41 54 41 55 41 56 48 8D AC 24 ?? FE FF FF 48"
    )
    def ApplyTerrainEditStroke(
        self,
        this: "_Pointer[cGcTerrainEditorBeam]",
        lEditData: sTerrainEditData,
        lImpact: c_uint64,  # cGcProjectileImpact *
    ) -> c_int64: ...

    @function_hook(
        "48 8B C4 4C 89 40 ? 48 89 48 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8"
    )
    def ApplyTerrainEditFlatten(
        self,
        this: "_Pointer[cGcTerrainEditorBeam]",
        lEditData: sTerrainEditData,
        lImpact: c_uint64,  # cGcProjectileImpact *
    ) -> c_uint64: ...


class cGcLocalPlayerCharacterInterface(Structure):
    @function_hook(
        "40 53 48 83 EC 20 48 8B 1D ?? ?? ?? ?? 48 8D 8B ?? ?? ?? 00 E8 ?? ?? ?? 00"
    )
    def IsJetpacking(
        self, this: "_Pointer[cGcLocalPlayerCharacterInterface]"
    ) -> c_bool: ...


class cGcSpaceshipComponent(Structure):
    @function_hook("48 89 5C 24 18 48 89 54 24 10 57 48 83 EC 70 41 0F B6 F8")
    def Eject(
        self,
        this: "_Pointer[cGcSpaceshipComponent]",
        lpPlayer: _Pointer[cGcPlayer],
        lbAnimate: Annotated[bool, c_bool],
        lbForceDuringCommunicator: Annotated[bool, c_bool],
    ): ...


class cGcSpaceshipWarp(Structure):
    @function_hook(
        "48 83 EC ? 48 8B 0D ? ? ? ? 41 B9 ? ? ? ? 48 81 C1 ? ? ? ? C7 44 24 ? ? ? ? ? BA ? ? ? ? 45 8D 41 ? E8 ? ? ? ? 48 85 C0 74 ? 66 0F 6E 40"
    )
    def GetPulseDriveFuelFactor(
        self, this: "_Pointer[cGcSpaceshipWarp]"
    ) -> c_float: ...


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


class cGcPlayerCharacterComponent(Structure):
    @function_hook("48 8B C4 55 53 56 57 41 56 48 8D 68 A1 48 81 EC 90 00 00")
    def SetDeathState(self, this: c_uint64): ...


class cGcTextChatInput(Structure):
    @function_hook(
        "40 55 53 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 80 3A"
    )
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
    @function_hook(
        "48 89 5C 24 ? 57 48 83 EC ? 48 8B 81 ? ? ? ? 48 8D 91 ? ? ? ? 44 8B 81"
    )
    def DeepInterstellarSearch(
        self, this: "_Pointer[cGcNotificationSequenceStartEvent]"
    ) -> c_char: ...


class PlanetGenerationQuery(Structure): ...


class cGcScanEventSolarSystemLookup(Structure): ...


class cGcScanEventManager(Structure):
    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 8B B1 ? ? ? ? 48 8B DA"
    )
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
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 4D 8B F8 C6 85"
    )
    def Generate(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lPlanetData: _Pointer[nmse.cGcPlanetData],
        lGenerationData: _Pointer[nmse.cGcPlanetGenerationInputData],
        lpPlanet: _Pointer[cGcPlanet],
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 50 ? 48 89 48 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 4C 63 B2"
    )
    def GenerateCreatureRoles(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lPlanetData: _Pointer[nmse.cGcPlanetData],
        lUA: c_uint64,
    ): ...

    @function_hook(
        "48 8B C4 48 89 50 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 33 F6"
    )
    def GenerateCreatureInfo(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lPlanetData: _Pointer[nmse.cGcPlanetData],
        lRole: _Pointer[nmse.cGcCreatureRoleData],
    ): ...

    @function_hook(
        "4C 89 4C 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B 0D"
    )
    def GenerateQueryInfo(
        self,
        this: "_Pointer[cGcPlanetGenerator]",
        lQueryData: _Pointer[PlanetGenerationQuery],
        lGenerationData: _Pointer[nmse.cGcPlanetGenerationInputData],
        lUA: c_uint64,
    ): ...

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 68 ? 48 89 70 ? 4C 89 48 ? 57 41 54 41 55 41 56 41 57 48 81 EC ? ? ? ? 4C 8B E1"
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
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 33 F6"
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
        "4C 89 4C 24 ? 4C 89 44 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B 99"
    )
    def DoDiscoveryView(
        self,
        this: "_Pointer[cGcFrontendPageDiscovery]",
        lPageData: _Pointer[cGcDiscoveryPageData],
        lFrontEndTextInput: _Pointer[cGcFrontendTextInput],
        lFronteEndModelRenderer: _Pointer[cGcFrontendModelRenderer],
    ): ...

    @static_function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 56 41 57 48 8D 6C 24 ? 48 81 EC ? ? ? ? 48 8D 05 ? ? ? ? 41 8B F9"
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


@partial_struct
class cGcGalacticVoxelCoordinate(Structure):
    mX: Annotated[int, Field(c_uint16)]
    mZ: Annotated[int, Field(c_uint16)]
    mY: Annotated[int, Field(c_uint16)]
    mbValid: Annotated[bool, Field(c_bool)]


class cGcFrontendPage(Structure): ...


class cGcFrontendPagePortalRunes(Structure):
    @static_function_hook(
        "48 8B C4 44 88 48 20 44 88 40 18 48 89 50 10 55 53 56 57 41 54"
    )
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
    @function_hook(
        "33 C0 0F 57 C0 0F 11 01 0F 11 41 ? 0F 11 41 ? 48 89 41 ? 48 89 41 ? 48 89 41 ? 48 89 41"
    )
    def SetDefaults(self, this: "_Pointer[cGcGalaxyVoxelAttributesData]"): ...


class cGcGalaxyStarAttributesData(nmse.cGcGalaxyStarAttributesData):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 ED 48 8D B9 ? ? ? ? 48 89 6C 24"
    )
    def SetDefaults(self, this: "_Pointer[cGcGalaxyStarAttributesData]"): ...


class cGcGalaxyAttributeGenerator(Structure):
    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F BF 41"
    )
    @staticmethod
    def ClassifyVoxel(
        lCoordinate: _Pointer[cGcGalacticVoxelCoordinate],
        lOutput: _Pointer[cGcGalaxyVoxelAttributesData],
    ): ...

    @static_function_hook(
        "48 89 54 24 ? 55 53 56 57 41 54 41 55 41 57 48 8B EC 48 83 EC ? 48 8B F9"
    )
    @staticmethod
    def ClassifyStarSystem(
        lUA: c_uint64, lOutput: _Pointer[cGcGalaxyStarAttributesData]
    ): ...


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
        "48 83 EC ? 65 48 8B 04 25 ? ? ? ? B9 ? ? ? ? 48 8B 00 8B 04 01 39 05 ? ? ? ? 0F 8F ? ? ? ? 48 8D 05 ? ? ? ? 48 83 C4 ? C3 4C 89 00"
    )
    def GetInstance(self) -> c_uint64: ...


@partial_struct
class cTkLanguageManagerBase(Structure):
    meRegion: Annotated[
        c_enum32[enums.eLanguageRegion], Field(c_enum32[enums.eLanguageRegion], 0x8)
    ]

    @function_hook("48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 57 C0 49 8B E8")
    def Translate(
        self,
        this: "_Pointer[cTkLanguageManagerBase]",
        lpacText: c_char_p,
        lpacDefaultReturnValue: _Pointer[basic.TkID[0x20]],
    ) -> c_uint64: ...

    @function_hook("48 89 5C 24 ? 57 48 81 EC ? ? ? ? 33 DB")
    def Load(
        self,
        this: "_Pointer[cTkLanguageManagerBase]",
        a2: c_char_p,
        a3: Annotated[bool, c_bool],
    ): ...


class cGcNameGenerator(Structure):
    @function_hook(
        "4C 89 4C 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 44 8B D2"
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


class cGcPlayerHUD(Structure):
    @function_hook("48 8B C4 55 57 48 8D 68 ? 48 81 EC ? ? ? ? 48 8B 91")
    def RenderIndicatorPanel(self, this: "_Pointer[cGcPlayerHUD]"): ...

    @function_hook(
        "48 8B C4 48 89 48 ? 55 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 83 B9"
    )
    def RenderWeaponPanel(self, this: "_Pointer[cGcPlayerHUD]"): ...

    @function_hook(
        "40 55 53 56 57 41 54 41 55 41 56 48 8D 6C 24 ? 48 81 EC ? ? ? ? 48 8B F1"
    )
    def RenderCrosshair(self, this: "_Pointer[cGcPlayerHUD]"): ...


class cGcApplicationBootState(Structure):
    @function_hook("48 89 5C 24 ? 55 56 57 41 56 41 57 48 81 EC ? ? ? ? 45 33 F6")
    def Update(
        self,
        this: "_Pointer[cGcApplicationBootState]",
        lfTimeStep: Annotated[float, c_float],
    ): ...


class cGcPlayerDiscoveryHelper(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 4C 24 ? 57 48 81 EC ? ? ? ? 48 8B 1D"
    )
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
        "48 89 5C 24 ? 48 89 4C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B 99"
    )
    def Update(
        self,
        this: "_Pointer[cGcPlayerExperienceDirector]",
        lfTimeStep: Annotated[float, c_float],
    ): ...


# Dummy values to copy and paste to make adding new things quicker...
# class name(Structure):
#     @function_hook("")
#     def method(self, this: "_Pointer[name]"):
#         ...
