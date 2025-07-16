# pyright: reportReturnType=false

import ctypes
from typing import Annotated, Optional

from pymhf.core.memutils import get_addressof
from pymhf.core.hooking import static_function_hook
from pymhf.core.hooking import function_hook, Structure
from pymhf.utils.partial_struct import partial_struct, Field
from pymhf.extensions.cpptypes import std
from pymhf.extensions.ctypes import c_enum32

import nmspy.data.basic_types as basic
import nmspy.data.exported_types as nmse
import nmspy.data.enums as enums

# Exported functions


class AK(Structure):
    class SoundEngine(Structure):
        @static_function_hook(
            exported_name="?RegisterGameObj@SoundEngine@AK@@YA?AW4AKRESULT@@_KPEBD@Z"
        )
        @staticmethod
        def RegisterGameObj(
            in_GameObj: ctypes.c_uint64,
            in_pszObjName: ctypes.c_uint64,
        ) -> ctypes.c_int64:
            pass

        @static_function_hook(
            exported_name=(
                "?PostEvent@SoundEngine@AK@@YAII_KIP6AXW4AkCallbackType@@PEAUAkCallbackInfo@@@ZPEAXIPEAUAkExt"
                "ernalSourceInfo@@I@Z"
            )
        )
        @staticmethod
        def PostEvent(
            in_ulEventID: ctypes.c_uint32,
            in_GameObjID: ctypes.c_uint64,
            in_uiFlags: ctypes.c_uint32 = 0,
            callback: ctypes.c_uint64 = 0,
            in_pCookie: ctypes.c_void_p = 0,
            in_cExternals: ctypes.c_uint32 = 0,
            in_pExternalSources: ctypes.c_uint64 = 0,
            in_PlayingID: ctypes.c_uint32 = 0,
        ) -> ctypes.c_uint64:
            pass


@partial_struct
class cGcNGuiText(Structure):
    mpTextData: Annotated[
        ctypes._Pointer[nmse.cGcNGuiTextData],
        Field(ctypes._Pointer[nmse.cGcNGuiTextData], 0x180),
    ]


@partial_struct
class TkAudioID(ctypes.Structure):
    mpacName: Annotated[Optional[str], Field(ctypes.c_char_p)]
    muID: Annotated[int, Field(ctypes.c_uint32)]
    mbValid: Annotated[bool, Field(ctypes.c_bool)]


@partial_struct
class cTkAudioManager(Structure):
    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 56 48 83 EC ? 48 8B F1 48 8B C2")
    def Play_attenuated(
        self,
        this: "ctypes._Pointer[cTkAudioManager]",
        event: ctypes._Pointer[TkAudioID],
        position: ctypes.c_uint64,
        object: ctypes.c_int64,
        attenuationScale: ctypes.c_float,
    ) -> ctypes.c_bool:
        pass

    @function_hook(
        "48 83 EC ? 33 C9 4C 8B D2 89 4C 24 ? 49 8B C0 48 89 4C 24 ? 45 33 C9"
    )
    def Play(
        self,
        this: "ctypes._Pointer[cTkAudioManager]",
        event: ctypes._Pointer[TkAudioID],
        object: ctypes.c_int64,
    ) -> ctypes.c_bool:
        pass


@partial_struct
class cGcNGuiLayer(Structure):
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
        this: "ctypes._Pointer[cGcNGuiLayer]",
        lID: ctypes.c_uint64,
    ) -> ctypes.c_uint64:  # cGcNGuiElement *
        pass

    @function_hook("40 55 57 41 57 48 83 EC ? 4C 8B 89")
    def FindElementRecursive(
        self,
        this: "ctypes._Pointer[cGcNGuiLayer]",
        lID: ctypes.c_uint64,  # const cTkHashedNGuiElement *
        leType: ctypes.c_uint32,  # eNGuiGameElementType
    ) -> ctypes.c_uint64:  # cGcNGuiElement *
        pass

    @function_hook("48 8B C4 53 48 81 EC ? ? ? ? 48 89 78 ? 4C 8B D2")
    def LoadFromMetadata(
        self,
        this: "ctypes._Pointer[cGcNGuiLayer]",
        lpacFilename: ctypes._Pointer[basic.cTkFixedString[0x80]],
        lbUseCached: ctypes.c_bool,
        a4: ctypes.c_bool,
    ):
        pass


@partial_struct
class cGcNGui(Structure):
    mRoot: Annotated[cGcNGuiLayer, Field(cGcNGuiLayer)]


@partial_struct
class cGcShipHUD(Structure):
    # The following offset is found from cGcShipHUD::RenderHeadsUp below the 2nd
    # cGcNGuiLayer::FindElementRecursive call.
    miSelectedPlanet: Annotated[int, Field(ctypes.c_uint32, 0x23BF0)]
    mbSelectedPlanetPanelVisible: Annotated[bool, Field(ctypes.c_bool, 0x23C00)]

    # The following offset is found by searching for "UI\\HUD\\SHIP\\MAINSCREEN.MXML"
    # (It's above the below entry.)
    mMainScreenGUI: Annotated[cGcNGui, Field(cGcNGui, offset=0x275D8)]
    # The following offset is found by searching for "UI\\HUD\\SHIP\\HEADSUP.MXML"
    mHeadsUpGUI: Annotated[cGcNGui, Field(cGcNGui, offset=0x27B90)]

    # hud_root: Annotated[int, Field(ctypes.c_ulonglong, 0x27F70)]  # TODO: Fix

    @function_hook("48 89 5C 24 ? 57 41 54 41 55 41 56 41 57 48 81 EC")
    def LoadData(self, this: "ctypes._Pointer[cGcShipHUD]"):
        pass

    @function_hook("40 55 53 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 48 8B 1D")
    def RenderHeadsUp(self, this: "ctypes._Pointer[cGcShipHUD]"):
        pass


class cTkStopwatch(Structure):
    @function_hook("48 83 EC ? 48 8B 11 0F 29 74 24")
    def GetDurationInSeconds(
        self, this: "ctypes._Pointer[cTkStopwatch]"
    ) -> ctypes.c_float:
        pass


# TODO: Once we have pymhf 0.1.14 subclass from cTkFSM
@partial_struct
class cGcApplication(Structure):
    # There are tricky to get...
    # The game mostly sets a lot of the fields of the cGcApplication struct in some kind of "baked" way, we
    # don't see the offsets as with other structs, and instead we need to find the object, and then infer the
    # offset from the offset of the cGcApplication object. We can get this by seeing the value passed in to
    # cTkFSM::Construct in cGcApplication::Construct.
    # These properties can be found in cGcApplication::Construct
    muPlayerSaveSlot: Annotated[int, Field(ctypes.c_uint32, 0x40)]
    mbPaused: Annotated[bool, Field(ctypes.c_bool, 0xB4F5)]

    @function_hook("40 53 48 83 EC 20 E8 ? ? ? ? 48 89")
    def Update(self, this: "ctypes._Pointer[cGcApplication]"):
        pass

    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 33 FF 48 89 74 24 ? 83 3D")
    def Construct(self, this: "ctypes._Pointer[cGcApplication]"):
        pass


class cTkFSM(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 ED 48 89 51"
    )
    def Construct(
        self,
        this: "ctypes._Pointer[cTkFSM]",
        lpOffsetTable: ctypes.c_uint64,
        lInitialState: ctypes.c_uint64,
    ):
        pass

    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 48 8B 05 ? ? ? ? 48 8B D9 0F 29 74 24")
    def Update(self, this: "ctypes._Pointer[cTkFSM]"):
        """Run every frame. Depsite `this` being of type `cTkFSM`, it's actually a pointer to the
        `cGcApplication` singleton since it has `cTkFSM` as a subclass."""
        pass

    @function_hook("48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 4C 8B 51 ? 49 8B E8")
    def StateChange(
        self,
        this: "ctypes._Pointer[cTkFSM]",
        lNewStateID: ctypes.c_uint64,
        lpUserData: ctypes.c_uint64,
        lbForceRestart: ctypes.c_bool,
    ):
        pass


class cGcBeamEffect(Structure):
    @function_hook(
        "40 53 48 83 EC ? 8B 41 ? 48 8B D9 A9 ? ? ? ? 76 ? 25 ? ? ? ? 3D ? ? ? ? 74 ? B0"
    )
    def Prepare(self, this: "ctypes._Pointer[cGcBeamEffect]"):
        pass


class cGcLaserBeam(Structure):
    @function_hook("48 89 5C 24 10 57 48 83 EC 50 48 83 B9")
    def Fire(
        self, this: "ctypes._Pointer[cGcLaserBeam]", lbHitOnFirstFrame: ctypes.c_bool
    ):
        pass


@partial_struct
class cGcMarkerPoint(Structure):
    _total_size_ = 0x280
    # Found in cGcScanEvent::Construct
    # Seems to be same as 4.13 at least up to where this is mapped
    mPosition: Annotated[basic.cTkPhysRelVec3, 0x0]
    mCenterOffset: Annotated[basic.Vector3f, 0x20]
    mCustomName: Annotated[basic.cTkFixedString[0x40], 0x3C]
    mNode: Annotated[basic.TkHandle, 0x108]
    mModelNode: Annotated[basic.TkHandle, 0x10C]
    meDisplay: Annotated[ctypes.c_bool * 4, 0x268]

    @static_function_hook("40 53 48 83 EC ? 33 C0 0F 57 C0 0F 11 01 48 8B D9")
    @staticmethod
    def cGcMarkerPoint(address: ctypes.c_uint64):
        """Construct an instance of the cGcMarkerPoint at the provided address"""
        pass

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 28 05 ? ? ? ? 48 8D 79"
    )
    def Reset(self, this: "ctypes._Pointer[cGcMarkerPoint]"):
        pass


@partial_struct
class cGcMarkerList(Structure):
    maMarkerObjects: Annotated[
        std.vector[cGcMarkerPoint], Field(std.vector[cGcMarkerPoint])
    ]

    @function_hook("48 89 5C 24 ? 55 56 41 56 48 83 EC ? 40 32 ED")
    def RemoveMarker(
        self,
        this: "ctypes._Pointer[cGcMarkerList]",
        lExampleMarker: ctypes._Pointer[cGcMarkerPoint],
    ) -> ctypes.c_uint64:
        pass

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 54 41 56 41 57 48 83 EC ? 80 BA"
    )
    def TryAddMarker(
        self,
        this: "ctypes._Pointer[cGcMarkerList]",
        lPoint: ctypes._Pointer[cGcMarkerPoint],
        lbUpdateTime: ctypes.c_bool,
    ) -> ctypes.c_char:
        pass


# TODO: Add/search for PersistentBaseBuffer data


class cGcBaseBuildingManager(Structure):
    @function_hook(
        "4C 8B DC 49 89 5B ? 49 89 6B ? 56 57 41 56 48 81 EC ? ? ? ? 41 0F B7 00"
    )
    def GetBaseRootNode(
        self,
        this: "ctypes._Pointer[cGcBaseBuildingManager]",
        result: ctypes._Pointer[basic.TkHandle],
        luBaseIndex: ctypes.c_uint64,  # _WORD *
        lbForceUpdateMatrix: ctypes.c_bool,
    ) -> ctypes.c_uint64:  # TkHandle *
        pass


class cGcBaseSearch(Structure):
    @static_function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 4C 89 70 ? 55 48 8D 68 ? 48 81 EC ? ? ? ? 66 0F 6F 05"
    )
    @staticmethod
    def FindNearestBaseInCurrentSystem(
        result: ctypes.c_uint64,  # BaseIndex *
        lWorldPosition: ctypes._Pointer[basic.Vector3f],  # cTkVector3 *
        leBaseType: ctypes.c_int32,  # ePersistentBaseTypes
    ):
        pass


class cGcBuilding(Structure):
    @function_hook("4C 8B DC 55 49 8D AB ? ? ? ? 48 81 EC ? ? ? ? 48 8B D1")
    def DestroyIntersectingVolcanoes(self, this: ctypes.c_uint64):
        pass


@partial_struct
class cGcScanEvent(Structure):
    mMarker: Annotated[cGcMarkerPoint, Field(cGcMarkerPoint, 0x10)]
    mpEvent: Annotated[
        ctypes._Pointer[nmse.cGcScanEventData],
        Field(ctypes._Pointer[nmse.cGcScanEventData], 0x290),
    ]

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 33 F6"
    )
    def Construct(
        self,
        this: "ctypes._Pointer[cGcScanEvent]",
        leTable: ctypes.c_int32,  # eScanTable
        lpEvent: ctypes._Pointer[nmse.cGcScanEventData],
        lpBuilding: ctypes._Pointer[cGcBuilding],
        lfStartTime: ctypes.c_float,
        lbMostImportant: ctypes.c_bool,
        lpMission: ctypes.c_uint64,  # std::pair<TkID<128>,cTkSeed> *
    ):
        pass

    @function_hook(
        "48 8B C4 55 53 56 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 48 8B F9"
    )
    def CalculateMarkerPosition(self, this: "ctypes._Pointer[cGcScanEvent]"):
        pass

    @function_hook(
        "4C 8B DC 55 57 49 8D AB ? ? ? ? 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 8B F9"
    )
    def Update(slef, this: "ctypes._Pointer[cGcScanEvent]", lfTimeStep: ctypes.c_float):
        pass

    @function_hook(
        "48 8B C4 55 53 56 57 41 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8B F1 0F 29 78"
    )
    def UpdateInteraction(self, this: "ctypes._Pointer[cGcScanEvent]"):
        pass

    @function_hook("4C 8B DC 55 56 49 8D 6B ? 48 81 EC ? ? ? ? 48 8B 81")
    def UpdateSpaceStationLocation(self, this: "ctypes._Pointer[cGcScanEvent]"):
        pass


class cGcPlayer(Structure):
    @function_hook(
        "40 55 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 4C 8B F9"
    )
    def CheckFallenThroughFloor(self, this: "ctypes._Pointer[cGcPlayer]"):
        pass

    @function_hook(
        "48 8B C4 48 89 58 ? 44 89 40 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 4C 8B 35"
    )
    def TakeDamage(
        self,
        this: "ctypes._Pointer[cGcPlayer]",
        lfDamageAmount: ctypes.c_float,
        leDamageType: c_enum32[enums.GcDamageType],
        lDamageId: ctypes._Pointer[basic.TkID[0x10]],
        lDir: ctypes._Pointer[basic.Vector3f],
        lpOwner: ctypes.c_uint64,  # cGcOwnerConcept *
        laEffectsDamageMultipliers: ctypes.c_uint64,  # std::vector<cGcCombatEffectDamageMultiplier,TkSTLAllocatorShim<cGcCombatEffectDamageMultiplier,4,-1> > *
    ):
        pass

    @function_hook("40 53 48 81 EC E0 00 00 00 48 8B D9 E8 ?? ?? ?? ?? 83 78 10 05")
    def OnEnteredCockpit(self, this: "ctypes._Pointer[cGcPlayer]"):
        pass

    @function_hook(
        "40 53 48 83 EC 20 48 8B 1D ?? ?? ?? ?? E8 ?? ?? ?? ?? 83 78 10 05 75 ?? 48 8B"
    )
    def GetDominantHand(self, this: "ctypes._Pointer[cGcPlayer]") -> ctypes.c_int64:
        pass


class cGcPlayerState(Structure):
    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 44 8B 81 ? ? ? ? 48 8D 2D")
    def AwardUnits(
        self,
        this: "ctypes._Pointer[cGcPlayerState]",
        liChange: ctypes.c_int32,
    ) -> ctypes.c_uint64:
        pass

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 44 8B 81 ? ? ? ? 48 8D 35")
    def AwardNanites(
        self,
        this: "ctypes._Pointer[cGcPlayerState]",
        liChange: ctypes.c_int32,
    ) -> ctypes.c_uint64:
        pass


class cGcGameState(Structure):
    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 88 54 24")
    def OnSaveProgressCompleted(
        self,
        this: "ctypes._Pointer[cGcGameState]",
        a2: ctypes.c_uint64,
        lbShowMessage: ctypes.c_bool,
        lbFullSave: ctypes.c_bool,
        leSaveReason: ctypes.c_int32,
    ):
        pass

    @function_hook("44 89 44 24 ? 89 54 24 ? 55 56 57 41 57")
    def LoadFromPersistentStorage(
        self,
        this: "ctypes._Pointer[cGcGameState]",
        a2: ctypes.c_int32,
        a3: ctypes.c_int32,
        lbNetworkClientLoad: ctypes.c_bool,
    ) -> ctypes.c_uint64:
        pass


class cGcPlanetGenerationInputData(nmse.cGcPlanetGenerationInputData):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 0F 57 C0 33 FF 0F 11 01 48 89 7C 24")
    def SetDefaults(self, this: "ctypes._Pointer[cGcPlanetGenerationInputData]"):
        pass


@partial_struct
class cGcTerrainRegionMap(Structure):
    mfCachedRadius: Annotated[float, Field(ctypes.c_float, 0x30)]
    mMatrix: Annotated[basic.cTkMatrix34, 0xD3490]


@partial_struct
class GcEnvironmentProperties(Structure):
    AtmosphereEndHeight: Annotated[float, Field(ctypes.c_float, 0x1C)]
    AtmosphereStartHeight: Annotated[float, Field(ctypes.c_float, 0x20)]
    SkyAtmosphereHeight: Annotated[float, Field(ctypes.c_float, 0x5C)]
    StratosphereHeight: Annotated[float, Field(ctypes.c_float, 0x78)]


@partial_struct
class GcPlanetSkyProperties(Structure):
    pass


@partial_struct
class cGcPlanet(Structure):
    # Most of these found in cGcPlanet::Construct or cGcPlanet::cGcPlanet
    miPlanetIndex: Annotated[int, Field(ctypes.c_int32, 0x50)]
    mPlanetData: Annotated[nmse.cGcPlanetData, 0x60]
    # TODO: This field follows directly after the above one. Once we have the cGcPlanetData struct mapped
    # correctly we can remove the offset to make it just be determined automatically.
    mPlanetGenerationInputData: Annotated[cGcPlanetGenerationInputData, 0x3A50]
    mRegionMap: Annotated[cGcTerrainRegionMap, 0x3B80]
    mNode: Annotated[basic.TkHandle, 0xD73C8]
    mPosition: Annotated[basic.Vector3f, 0xD73E0]

    mpEnvProperties: Annotated[ctypes._Pointer[GcEnvironmentProperties], 0xD9048]
    mpSkyProperties: Annotated[ctypes._Pointer[GcPlanetSkyProperties], 0xD9050]

    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 45 33 FF 48 C7 41 ? ? ? ? ? 44 89 79"
    )
    def cGcPlanet(self, this: "ctypes._Pointer[cGcPlanet]"):
        pass

    @function_hook("48 8B C4 4C 89 40 ? 88 50 ? 55 53")
    def Generate(
        self,
        this: "ctypes._Pointer[cGcPlanet]",
        lbLoad: ctypes.c_bool,
        lPosition: ctypes._Pointer[basic.Vector3f],
        lSolarSystemDiscoveryData: ctypes.c_uint64,  # cGcDiscoveryData *
        lGenerationInputParams: ctypes._Pointer[nmse.cGcPlanetGenerationInputData],
    ):
        pass

    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 F6 89 51 ? 89 B1")
    def Construct(self, this: "ctypes._Pointer[cGcPlanet]", liIndex: ctypes.c_int32):
        pass

    @function_hook("48 89 5C 24 ? 48 89 6C 24 ? 56 57 41 56 48 83 EC ? 48 8B D9 8B 89")
    def SetupRegionMap(self, this: "ctypes._Pointer[cGcPlanet]"):
        pass

    @function_hook("48 8B C4 57 48 81 EC ? ? ? ? F3 0F 10 15")
    def UpdateClouds(
        self, this: "ctypes._Pointer[cGcPlanet]", lfTimeStep: ctypes.c_float
    ):
        pass

    @function_hook("40 53 48 83 EC ? 83 B9 ? ? ? ? ? 48 8B D9 0F 29 74 24")
    def UpdateGravity(
        self, this: "ctypes._Pointer[cGcPlanet]", lfNewGravityMultiplier: ctypes.c_float
    ):
        pass

    @function_hook("40 55 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 80 3D")
    def UpdateWeather(
        self, this: "ctypes._Pointer[cGcPlanet]", lfTimeStep: ctypes.c_float
    ):
        pass


@partial_struct
class cGcSolarSystem(Structure):
    mSolarSystemData: Annotated[nmse.cGcSolarSystemData, 0x0]
    maPlanets: Annotated[list["cGcPlanet"], Field(cGcPlanet * 6, 0x2630)]

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 29 74 24 ? 48 8B D9 48 8B F9"
    )
    def cGcSolarSystem(self, this: "ctypes._Pointer[cGcSolarSystem]"):
        pass

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 48 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 83 3D"
    )
    def Construct(self, this: "ctypes._Pointer[cGcSolarSystem]"):
        pass

    @function_hook("48 89 5C 24 ? 55 56 57 41 55 41 57 48 8B EC 48 83 EC ? 83 3D")
    def OnLeavePlanetOrbit(
        self, this: "ctypes._Pointer[cGcSolarSystem]", lbAnnounceOSD: ctypes.c_bool
    ):
        """lbAnnounceOSD not used."""
        pass

    @function_hook(
        "48 8B C4 55 41 54 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 89 58 ? 45 33 E4 44 39 25"
    )
    def OnEnterPlanetOrbit(
        self, this: "ctypes._Pointer[cGcSolarSystem]", lbAnnounceOSD: ctypes.c_bool
    ):
        pass

    @function_hook(
        "48 8B C4 48 89 58 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 41 BC"
    )
    def Generate(
        self,
        this: "ctypes._Pointer[cGcSolarSystem]",
        lbUseSettingsFile: ctypes.c_bool,
        lSeed: ctypes._Pointer[basic.GcSeed],
    ):
        pass


class cGcApplicationLocalLoadState(Structure):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 80 B9 ? ? ? ? ? 48 8B F9 BB")
    def GetRespawnReason(
        self, this: "ctypes._Pointer[cGcApplicationLocalLoadState]"
    ) -> ctypes.c_int64:
        pass


class cTkDynamicGravityControl(Structure):
    @partial_struct
    class cTkGravityPoint(Structure):
        _total_size_ = 0x20
        mCenter: Annotated[basic.Vector3f, 0x0]
        mfStrength: Annotated[float, Field(ctypes.c_float, 0x10)]
        mfFalloffRadiusSqr: Annotated[float, Field(ctypes.c_float, 0x14)]
        mfMaxStrength: Annotated[float, Field(ctypes.c_float, 0x18)]

    @partial_struct
    class cTkGravityOBB(Structure):
        _total_size_ = 0xA0
        mUp: Annotated[basic.Vector3f, 0x0]
        mfConstantStrength: Annotated[float, Field(ctypes.c_float, 0x10)]
        mfFalloffStrength: Annotated[float, Field(ctypes.c_float, 0x14)]
        mTransformInverse: Annotated[basic.cTkMatrix34, 0x20]
        mUntransformedCentre: Annotated[basic.Vector3f, 0x60]
        mOBB: Annotated[basic.cTkAABB, 0x70]
        mfFalloffRadiusSqr: Annotated[float, Field(ctypes.c_float, 0x90)]

    maGravityPoints: list["cTkDynamicGravityControl.cTkGravityPoint"]
    miNumGravityPoints: int
    maGravityOBBs: bytes

    @function_hook("33 C0 48 8D 91 ? ? ? ? 89 81")
    def Construct(self, this: "ctypes._Pointer[cTkDynamicGravityControl]"):
        pass

    @function_hook("4C 8B C1 48 8B C1 BA ? ? ? ? 0F 57 C0")
    def cTkDynamicGravityControl(
        self, this: "ctypes._Pointer[cTkDynamicGravityControl]"
    ):
        pass

    @function_hook("48 8B C4 55 57 41 54 41 55 48 81 EC")
    def GetGravity(
        self,
        this: "ctypes._Pointer[cTkDynamicGravityControl]",
        result: ctypes.c_uint64,
        lPos: ctypes._Pointer[basic.Vector3f],
    ) -> ctypes.c_uint64:
        pass

    @function_hook("40 57 48 83 EC ? 48 63 81 ? ? ? ? 45 33 D2")
    def UpdateGravityPoint(
        self,
        this: "ctypes._Pointer[cTkDynamicGravityControl]",
        lCentre: ctypes._Pointer[basic.Vector3f],
        lfRadius: ctypes.c_float,
        lfNewStrength: ctypes.c_float,
    ):
        pass


cTkDynamicGravityControl._fields_ = [
    ("maGravityPoints", cTkDynamicGravityControl.cTkGravityPoint * 0x9),
    ("miNumGravityPoints", ctypes.c_int32),
    ("maGravityOBBs", basic.cTkClassPool[cTkDynamicGravityControl.cTkGravityOBB, 0x40]),
]


class cGcSimulation(Structure):
    @function_hook(
        "48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D 6C 24 ? 48 81 EC ? ? ? ? 45 33 FF"
    )
    def Construct(self, this: "ctypes._Pointer[cGcSimulation]"):
        pass


@partial_struct
class cGcPlayerEnvironment(Structure):
    mPlayerTM: Annotated[basic.cTkMatrix34, Field(basic.cTkMatrix34, 0x0)]
    mUp: Annotated[basic.Vector3f, Field(basic.Vector3f, 0x40)]

    miNearestPlanetIndex: Annotated[int, Field(ctypes.c_uint32, 0x2BC)]
    mfDistanceFromPlanet: Annotated[float, Field(ctypes.c_float, 0x2C0)]
    mfNearestPlanetSealevel: Annotated[float, Field(ctypes.c_float, 0x2C4)]
    mNearestPlanetPos: Annotated[basic.Vector3f, Field(basic.Vector3f, 0x2D0)]
    mbInsidePlanetAtmosphere: Annotated[bool, Field(ctypes.c_bool, 0x2EC)]

    @function_hook("48 83 EC ? 80 B9 ? ? ? ? ? C6 04 24")
    def IsOnboardOwnFreighter(self, this: "ctypes._Pointer[cGcPlayerEnvironment]"):
        pass

    @function_hook("8B 81 ? ? ? ? 83 E8 ? 83 F8 ? 0F 96 C0 C3 4C 8B D1")
    def IsOnPlanet(self, this: "ctypes._Pointer[cGcPlayerEnvironment]"):
        pass

    @function_hook("48 8B C4 F3 0F 11 48 ? 55 53 57 41 56 48 8D A8")
    def Update(
        self, this: "ctypes._Pointer[cGcPlayerEnvironment]", lfTimeStep: ctypes.c_float
    ):
        pass


class Engine:
    @static_function_hook("40 53 48 83 EC ? 44 8B D1 44 8B C1")
    @staticmethod
    def ShiftAllTransformsForNode(node: ctypes.c_uint32, lShift: ctypes.c_uint64):
        pass

    @static_function_hook("40 56 48 83 EC ? 44 8B C9")
    @staticmethod
    def GetNodeAbsoluteTransMatrix(
        node: ctypes.c_uint32,  # TkHandle
        absMat: ctypes.c_uint64,  # cTkMatrix34 *
    ):
        pass

    @static_function_hook("4C 89 4C 24 ? 48 89 4C 24 ? 55 56 41 57")
    @staticmethod
    def SetUniformArrayDefaultMultipleShaders(
        laShaderRes: ctypes.c_uint64,
        liNumShaders: ctypes.c_int32,
        name: ctypes.c_uint64,  # char *
        lpafData: ctypes.c_uint64,  # float *
        liNumVectors: ctypes.c_int32,
    ) -> ctypes.c_int64:
        pass

    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 41 56 48 83 EC ? 4D 63 F1 49 8B F8"
    )
    @staticmethod
    def SetMaterialUniformArray(
        materialRes: ctypes.c_uint64,  # TkStrongType<int,TkStrongTypeIDs::TkResHandleID>
        name: ctypes.c_uint64,  # char *
        lpafData: ctypes.c_uint64,  # float *
        liNumVectors: ctypes.c_int32,
    ):
        pass


def ShiftAllTransformsForNode(node: basic.TkHandle, shift: basic.Vector3f):
    Engine.ShiftAllTransformsForNode(node.lookupInt, get_addressof(shift))


def GetNodeAbsoluteTransMatrix(node: basic.TkHandle, absMat: basic.cTkMatrix34):
    Engine.ShiftAllTransformsForNode(node.lookupInt, get_addressof(absMat))


class cGcRewardManager(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 41 56 41 57 48 83 EC ? 48 8B 3D ? ? ? ? 48 8B F1"
    )
    def GiveGenericReward(
        self,
        this: "ctypes._Pointer[cGcRewardManager]",
        lRewardID: ctypes._Pointer[basic.cTkFixedString[0x10]],
        lMissionID: ctypes._Pointer[basic.cTkFixedString[0x10]],
        lSeed: ctypes._Pointer[basic.cTkSeed],
        lbPeek: ctypes.c_bool,
        lbForceShowMessage: ctypes.c_bool,
        liOutMultiProductCount: ctypes.c_uint64,
        lbForceSilent: ctypes.c_bool,
        lInventoryChoiceOverride: ctypes.c_int32,
        lbUseMiningModifier: ctypes.c_bool,
    ) -> ctypes.c_uint64:
        pass


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
    mpData: Annotated[ctypes._Pointer[nmse.cGcInteractionComponentData], 0x30]

    @function_hook("44 88 4C 24 ? 44 88 44 24 ? 48 89 54 24")
    def GiveReward(
        self,
        this: "ctypes._Pointer[cGcInteractionComponent]",
        lOption: ctypes._Pointer[cGcAlienPuzzleOption],
        lbPeek: ctypes.c_bool,
        lbForceShowMessage: ctypes.c_bool,
        lbForceSilent: ctypes.c_bool,
    ) -> ctypes.c_uint64:
        pass

    @function_hook("48 8B 81 ? ? ? ? 48 85 C0 74 ? 48 83 B9 ? ? ? ? ? 75 ? 48 83 B9")
    def GetPuzzle(
        self,
        this: "ctypes._Pointer[cGcInteractionComponent]",
    ) -> ctypes.c_uint64:  # cGcAlienPuzzleEntry *
        pass


@partial_struct
class cTkInputPort(Structure):
    mButtons: Annotated[
        basic.cTkBitArray[ctypes.c_uint64, 512],
        Field(basic.cTkBitArray[ctypes.c_uint64, 512], 0x108),
    ]
    mButtonsPrev: Annotated[
        basic.cTkBitArray[ctypes.c_uint64, 512],
        Field(basic.cTkBitArray[ctypes.c_uint64, 512], 0x148),
    ]

    @function_hook("40 57 48 83 EC ? 48 83 79 ? ? 44 8B CA")
    def SetButton(
        self,
        this: "ctypes._Pointer[cTkInputPort]",
        leIndex: ctypes.c_int32,
    ):
        pass

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 41 8B D8 8B FA 48 8B F1 45 84 C9"
    )
    def GetButton(
        self,
        this: "ctypes._Pointer[cTkInputPort]",
        leIndex: ctypes.c_int32,
        leValidation: ctypes.c_int32,
        lbDebugOnly: ctypes.c_bool,
    ) -> ctypes.c_uint8:
        pass


@partial_struct
class cGcBinoculars(Structure):
    mfScanProgress: Annotated[float, Field(ctypes.c_float, 0x24)]
    mpBinocularInfoGui: Annotated[ctypes._Pointer[cGcNGui], 0x800]

    @function_hook("40 55 41 56 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 80 3D")
    def SetMarker(self, this: "ctypes._Pointer[cGcBinoculars]"):
        pass

    @function_hook("40 53 48 81 EC ? ? ? ? 48 8B 05 ? ? ? ? 48 8D 54 24")
    def GetRange(self, this: "ctypes._Pointer[cGcBinoculars]") -> ctypes.c_float:
        pass

    @function_hook(
        "48 8B C4 55 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 48 89 70"
    )
    def UpdateTarget(
        self, this: "ctypes._Pointer[cGcBinoculars]", lfTimeStep: ctypes.c_float
    ):
        pass

    @function_hook("40 53 48 83 EC ? 48 8B 91 ? ? ? ? 48 8B D9 F3 0F 11 49")
    def UpdateScanBarProgress(
        self, this: "ctypes._Pointer[cGcBinoculars]", lfScanProgress: ctypes.c_float
    ):
        """Called each frame while scanning to set the cGcBinoculars.mfScanProgress from the lfScanProgress
        argument of this function."""
        pass

    @function_hook(
        "48 8B C4 55 53 56 57 41 56 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8B F1 48 8B 0D"
    )
    def UpdateRayCasts(
        self,
        this: "ctypes._Pointer[cGcBinoculars]",
        lTargetInfo: ctypes.c_uint64,  # cTkContactPoint *
    ):
        pass


class cTkFSMState(Structure):
    @function_hook(signature="4C 8B 51 ? 4D 8B D8")
    def StateChange(
        self,
        this: "ctypes._Pointer[cTkFSMState]",
        lNewStateID: ctypes._Pointer[basic.cTkFixedString[0x10]],
        lpUserData: ctypes.c_void_p,
        lbForceRestart: ctypes.c_bool,
    ):
        pass


class cGcEnvironment(Structure):
    @function_hook(
        "48 8B C4 48 89 48 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 4C 8B F9"
    )
    def UpdateRender(self, this: "ctypes._Pointer[cGcEnvironment]"):
        pass


class cGcPlayerNotifications(Structure):
    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 81 EC ? ? ? ? 44 8B 81")
    def AddTimedMessage(
        self,
        this: "ctypes._Pointer[cGcPlayerNotifications]",
        lsMessage: ctypes._Pointer[basic.cTkFixedString[512]],
        lfDisplayTime: ctypes.c_float,
        lColour: ctypes._Pointer[basic.Colour],
        liAudioID: ctypes.c_uint32,
        lIcon: ctypes.c_uint64,  # cTkSmartResHandle*
        # Note: The following fields have changed since 4.13... Might need to confirm...
        unknown: ctypes.c_uint64,
        unknown2: ctypes.c_uint32,
        lbShowMessageBackground: ctypes.c_bool,
        lbShowIconGlow: ctypes.c_bool,
    ):
        pass


class cGcSky(Structure):
    eStormState = enums.eStormState

    @function_hook("40 53 55 56 57 41 56 48 83 EC ? 4C 8B 15")
    def SetStormState(
        self, this: "ctypes._Pointer[cGcSky]", leNewState: c_enum32[eStormState]
    ):
        pass


class sTerrainEditData(ctypes.Structure):
    mVoxelType: int
    mShape: int
    mCustom1: int
    mCustom2: int

    _fields_ = [
        ("mVoxelType", ctypes.c_uint8, 3),
        ("mShape", ctypes.c_uint8, 1),
        ("mCustom1", ctypes.c_uint8, 3),
        ("mCustom2", ctypes.c_uint8, 1),
    ]


class cGcTerrainEditorBeam(Structure):
    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 70 ? 48 89 78 ? 55 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 4C 8B F2"
    )
    def Fire(
        self,
        this: "ctypes._Pointer[cGcTerrainEditorBeam]",
        lvTargetPos: ctypes._Pointer[basic.cTkPhysRelVec3],
        lpTargetBody: ctypes.c_uint64,  # cTkRigidBody *
        lpOwnerConcept: ctypes.c_uint64,  # cGcOwnerConcept *
        leStatType: c_enum32[enums.GcStatsTypes],
        lbVehicle: ctypes.c_bool,
    ) -> ctypes.c_char:
        pass

    @function_hook(
        "48 89 5C 24 ? 48 89 7C 24 ? 55 48 8D 6C 24 ? 48 81 EC ? ? ? ? 0F 28 05 ? ? ? ? 48 8B D9"
    )
    def StartEffect(self, this: "ctypes._Pointer[cGcTerrainEditorBeam]"):
        pass

    @function_hook(
        "4C 89 44 24 18 55 53 56 57 41 54 41 55 41 56 48 8D AC 24 ?? FE FF FF 48"
    )
    def ApplyTerrainEditStroke(
        self,
        this: "ctypes._Pointer[cGcTerrainEditorBeam]",
        lEditData: sTerrainEditData,
        lImpact: ctypes.c_uint64,  # cGcProjectileImpact *
    ) -> ctypes.c_int64:
        pass

    @function_hook("48 8B C4 4C 89 40 ? 88 50 ? 48 89 48")
    def ApplyTerrainEditFlatten(
        self,
        this: "ctypes._Pointer[cGcTerrainEditorBeam]",
        lEditData: sTerrainEditData,
        lImpact: ctypes.c_uint64,  # cGcProjectileImpact *
    ) -> ctypes.c_uint64:
        pass


class cGcLocalPlayerCharacterInterface(Structure):
    @function_hook(
        "40 53 48 83 EC 20 48 8B 1D ?? ?? ?? ?? 48 8D 8B ?? ?? ?? 00 E8 ?? ?? ?? 00"
    )
    def IsJetpacking(
        self, this: "ctypes._Pointer[cGcLocalPlayerCharacterInterface]"
    ) -> ctypes.c_bool:
        pass


class cGcSpaceshipComponent(Structure):
    @function_hook("48 89 5C 24 18 48 89 54 24 10 57 48 83 EC 70 41 0F B6 F8")
    def Eject(
        self,
        this: "ctypes._Pointer[cGcSpaceshipComponent]",
        lpPlayer: ctypes._Pointer[cGcPlayer],
        lbAnimate: ctypes.c_bool,
        lbForceDuringCommunicator: ctypes.c_bool,
    ):
        pass


class cGcSpaceshipWarp(Structure):
    @function_hook(
        "48 83 EC 38 48 8B 0D ?? ?? ?? ?? 41 B9 01 00 00 00 48 81 C1 30 B3 00 00 C7 44 24 20 FF FF FF FF BA 9A"
    )
    def GetPulseDriveFuelFactor(
        self, this: "ctypes._Pointer[cGcSpaceshipWarp]"
    ) -> ctypes.c_float:
        pass


class cGcSpaceshipWeapons(Structure):
    @function_hook("48 63 81 ?? ?? 00 00 80 BC 08 ?? ?? 00 00 00 74 12")
    def GetOverheatProgress(
        self, this: "ctypes._Pointer[cGcSpaceshipWeapons]"
    ) -> ctypes.c_float:
        pass

    @function_hook("48 8B C4 48 89 70 ? 57 48 81 EC ? ? ? ? 83 B9")
    def GetAverageBarrelPos(
        self,
        this: "ctypes._Pointer[cGcSpaceshipWeapons]",
        result: ctypes._Pointer[basic.cTkPhysRelVec3],
    ) -> ctypes.c_uint64:  # cTkPhysRelVec3 *
        pass

    @function_hook(
        "40 53 48 83 EC ? 48 8B 41 ? 48 8B D9 0F BF 0D ? ? ? ? 48 8B 50 ? E8 ? ? ? ? 48 85 C0 74 ? 48 89 7C 24"
    )
    def GetCurrentShootPoints(
        self,
        this: "ctypes._Pointer[cGcSpaceshipWeapons]",
    ) -> ctypes.c_uint64:  # cGcShootPoint *
        pass


class cGcPlayerCharacterComponent(Structure):
    @function_hook("48 8B C4 55 53 56 57 41 56 48 8D 68 A1 48 81 EC 90 00 00")
    def SetDeathState(self, this: ctypes.c_uint64):
        pass


class cGcTextChatInput(Structure):
    @function_hook(
        "40 55 53 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 80 3A"
    )
    def ParseTextForCommands(
        self,
        this: "ctypes._Pointer[cGcTextChatInput]",
        lMessageText: ctypes._Pointer[basic.cTkFixedString[0x80]],
    ):
        pass


class cGcTextChatManager(Structure):
    @function_hook("48 89 5C 24 ? 57 48 83 EC ? 48 8D 91 ? ? ? ? 33 FF")
    def Construct(self, this: "ctypes._Pointer[cGcTextChatManager]"):
        pass

    @function_hook("40 53 48 81 EC ? ? ? ? F3 0F 10 05")
    def Say(
        self,
        this: "ctypes._Pointer[cGcTextChatManager]",
        lsMessageBody: ctypes._Pointer[basic.cTkFixedString[0x80]],
        lbSystemMessage: ctypes.c_bool,
    ):
        pass


class cGcNotificationSequenceStartEvent(Structure):
    @function_hook(
        "48 89 5C 24 ? 57 48 83 EC ? 48 8B 81 ? ? ? ? 48 8D 91 ? ? ? ? 44 8B 81"
    )
    def DeepInterstellarSearch(
        self, this: "ctypes._Pointer[cGcNotificationSequenceStartEvent]"
    ) -> ctypes.c_char:
        pass


class PlanetGenerationQuery(Structure):
    pass


class cGcScanEventSolarSystemLookup(Structure):
    pass


class cGcScanEventManager(Structure):
    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 8B B1 ? ? ? ? 48 8B DA"
    )
    @staticmethod
    def PassesPlanetInfoChecks(
        lPlanet: ctypes._Pointer[PlanetGenerationQuery],
        lSolarSystemLookup: ctypes._Pointer[cGcScanEventSolarSystemLookup],
        lbAbandonedSystemInteraction: ctypes.c_bool,
        leBuildingClass: ctypes.c_uint32,  # eBuildingClass
        lbIsAbandonedOrEmptySystem: ctypes.c_bool,
    ) -> ctypes.c_bool:
        pass


class cGcPlanetGenerator(Structure):
    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 4D 8B F8 C6 85"
    )
    def Generate(
        self,
        this: "ctypes._Pointer[cGcPlanetGenerator]",
        lPlanetData: ctypes._Pointer[nmse.cGcPlanetData],
        lGenerationData: ctypes._Pointer[nmse.cGcPlanetGenerationInputData],
        lpPlanet: ctypes._Pointer[cGcPlanet],
    ):
        pass

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 50 ? 48 89 48 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 4C 63 B2"
    )
    def GenerateCreatureRoles(
        self,
        this: "ctypes._Pointer[cGcPlanetGenerator]",
        lPlanetData: ctypes._Pointer[nmse.cGcPlanetData],
        lUA: ctypes.c_uint64,
    ):
        pass

    @function_hook(
        "48 8B C4 48 89 50 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC ? ? ? ? 0F 29 70 ? 33 F6"
    )
    def GenerateCreatureInfo(
        self,
        this: "ctypes._Pointer[cGcPlanetGenerator]",
        lPlanetData: ctypes._Pointer[nmse.cGcPlanetData],
        lRole: ctypes._Pointer[nmse.cGcCreatureRoleData],
    ):
        pass

    @function_hook(
        "4C 89 4C 24 ? 48 89 54 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24"
    )
    def GenerateQueryInfo(
        self,
        this: "ctypes._Pointer[cGcPlanetGenerator]",
        lQueryData: ctypes._Pointer[PlanetGenerationQuery],
        lGenerationData: ctypes._Pointer[nmse.cGcPlanetGenerationInputData],
        lUA: ctypes.c_uint64,
    ):
        pass

    @function_hook(
        "48 8B C4 48 89 58 ? 48 89 68 ? 48 89 70 ? 4C 89 48 ? 57 41 54 41 55 41 56 41 57 48 81 EC ? ? ? ? 4C 8B E1"
    )
    def FillCreatureSpawnDataFromDescription(
        self,
        this: "ctypes._Pointer[cGcPlanetGenerator]",
        lRole: ctypes._Pointer[nmse.cGcCreatureRoleData],
        lSpawnData: ctypes._Pointer[nmse.cGcCreatureSpawnData],
        lPlanetData: ctypes._Pointer[nmse.cGcPlanetData],
    ):
        pass


class cGcGalaxyAttributesAtAddress(Structure):
    pass


class cGcSolarSystemGenerator(Structure):
    class GenerationData(Structure):
        pass

    @function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 33 F6"
    )
    def GenerateQueryInfo(
        self,
        this: "ctypes._Pointer[cGcSolarSystemGenerator]",
        lSeed: ctypes._Pointer[basic.cTkSeed],
        lAttributes: ctypes._Pointer[cGcGalaxyAttributesAtAddress],
        lData: "ctypes._Pointer[cGcSolarSystemGenerator.GenerationData]",
    ):
        pass


class cGcDiscoveryPageData(Structure):
    pass


class cGcFrontendTextInput(Structure):
    pass


class cGcFrontendModelRenderer(Structure):
    pass


class cGcFrontendPageDiscovery(Structure):
    @function_hook(
        "4C 89 4C 24 ? 4C 89 44 24 ? 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? B8 ? ? ? ? E8 ? ? ? ? 48 2B E0 48 8B 99"
    )
    def DoDiscoveryView(
        self,
        this: "ctypes._Pointer[cGcFrontendPageDiscovery]",
        lPageData: ctypes._Pointer[cGcDiscoveryPageData],
        lFrontEndTextInput: ctypes._Pointer[cGcFrontendTextInput],
        lFronteEndModelRenderer: ctypes._Pointer[cGcFrontendModelRenderer],
    ):
        pass

    @static_function_hook(
        "48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 56 41 57 48 8D 6C 24 ? 48 81 EC ? ? ? ? 48 8D 05 ? ? ? ? 41 8B F9"
    )
    @staticmethod
    def GetDiscoveryHintString(
        result: ctypes._Pointer[basic.cTkFixedString[0x40]],
        leTileType: ctypes.c_uint32,  # eTileType
        leCreatureType: c_enum32[enums.GcCreatureTypes],
        leRarity: c_enum32[enums.GcRarity],
        leActiveTime: c_enum32[enums.GcCreatureActiveTime],
        leHemisphere: c_enum32[enums.GcCreatureHemiSphere],
    ):
        pass


@partial_struct
class cGcGalacticVoxelCoordinate(Structure):
    mX: Annotated[int, Field(ctypes.c_uint16)]
    mZ: Annotated[int, Field(ctypes.c_uint16)]
    mY: Annotated[int, Field(ctypes.c_uint16)]
    mbValid: Annotated[bool, Field(ctypes.c_bool)]


class cGcFrontendPage(Structure):
    pass


class cGcFrontendPagePortalRunes(Structure):
    @static_function_hook(
        "48 8B C4 44 88 48 20 44 88 40 18 48 89 50 10 55 53 56 57 41 54"
    )
    @staticmethod
    def CheckUAIsValid(
        lTargetUA: ctypes.c_ulonglong,
        lModifiedUA: "ctypes._Pointer[cGcGalacticVoxelCoordinate]",
        lbDeterministicRandom: ctypes.c_bool,
        a4: ctypes.c_bool,
    ) -> ctypes.c_bool:
        pass

    @function_hook(
        "48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 48 8D 6C 24 ? 48 81 EC ? ? ? ? 0F 57 C0"
    )
    def DoInteraction(
        self,
        this: "ctypes._Pointer[cGcFrontendPagePortalRunes]",
        lpPage: ctypes._Pointer[cGcFrontendPage],
    ):
        pass


class cGcGalaxyVoxelAttributesData(nmse.cGcGalaxyVoxelAttributesData):
    @function_hook(
        "33 C0 0F 57 C0 0F 11 01 0F 11 41 ? 0F 11 41 ? 48 89 41 ? 48 89 41 ? 48 89 41 ? 48 89 41"
    )
    def SetDefaults(self, this: "ctypes._Pointer[cGcGalaxyVoxelAttributesData]"):
        pass


class cGcGalaxyStarAttributesData(nmse.cGcGalaxyStarAttributesData):
    @function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 33 ED 48 8D B9 ? ? ? ? 48 89 6C 24"
    )
    def SetDefaults(self, this: "ctypes._Pointer[cGcGalaxyStarAttributesData]"):
        pass


class cGcGalaxyAttributeGenerator(Structure):
    @static_function_hook(
        "48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F BF 41"
    )
    @staticmethod
    def ClassifyVoxel(
        lCoordinate: ctypes._Pointer[cGcGalacticVoxelCoordinate],
        lOutput: ctypes._Pointer[cGcGalaxyVoxelAttributesData],
    ):
        pass

    @static_function_hook(
        "48 89 54 24 ? 55 53 56 57 41 54 41 55 41 57 48 8B EC 48 83 EC ? 48 8B F9"
    )
    @staticmethod
    def ClassifyStarSystem(
        lUA: ctypes.c_ulonglong, lOutput: ctypes._Pointer[cGcGalaxyStarAttributesData]
    ):
        pass


class cGcGalaxyVoxelData(Structure):
    pass


class cGcGalaxyVoxelGenerator(nmse.cGcGalaxyStarAttributesData):
    @static_function_hook("48 8B C4 4C 89 40 ? 48 89 48 ? 55 53 56 57 41 56 48 8D A8")
    @staticmethod
    def Populate(
        lu64UniverseAddress: ctypes.c_uint64,
        lVoxelData: ctypes._Pointer[cGcGalaxyVoxelData],
        lRootOffset: ctypes._Pointer[basic.Vector3f],
    ):
        pass


class cTkLanguageManagerBase(Structure):
    @function_hook("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 0F 57 C0 49 8B F0")
    def Translate(
        self,
        this: "ctypes._Pointer[cTkLanguageManagerBase]",
        lpacText: ctypes.c_char_p,
        lpacDefaultReturnValue: ctypes._Pointer[basic.TkID[0x20]],
    ) -> ctypes.c_uint64:
        pass


class cGcNameGenerator(Structure):
    @function_hook(
        "4C 89 4C 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC ? ? ? ? 44 8B D2"
    )
    def GeneratePlanetName(
        self,
        this: "ctypes._Pointer[cGcNameGenerator]",
        lu64Seed: ctypes.c_uint64,
        lResult: ctypes._Pointer[basic.cTkFixedString[0x79]],
        lLocResult: ctypes._Pointer[basic.cTkFixedString[0x79]],
    ):
        pass


# Dummy values to copy and paste to make adding new things quicker...
# class name(Structure):
#     @function_hook("")
#     def method(self, this: "ctypes._Pointer[name]"):
#         pass
