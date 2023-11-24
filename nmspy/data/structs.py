from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from ctypes import _Pointer

import ctypes
import ctypes.wintypes

from nmspy.data import common, enums as nms_enums
from nmspy.calling import call_function
# from nmspy.data.types import core, simple
from nmspy.memutils import map_struct
from nmspy.utils import safe_assign_enum


class cTkMetaDataXMLFunctionLookup(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char * 0x40),
        ("writeFunction", ctypes.c_longlong),
        ("readFunction", ctypes.c_longlong),
        ("saveFunction", ctypes.c_longlong),
    ]
    name: str
    writeFunction: int
    readFunction: int
    saveFunction: int


class cTkMetaDataEnumLookup(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_longlong),
        ("_name", ctypes.c_char_p),
    ]
    value: int
    _name: bytes

    @property
    def name(self) -> str:
        return self._name.decode()


class cTkMetaDataMember(ctypes.Structure):
    class eType(IntEnum):
        Unspecified = 0x0
        Bool = 0x1
        Byte = 0x2
        Class = 0x3
        ClassPointer = 0x4
        Colour = 0x5
        DynamicArray = 0x6
        DynamicString = 0x7
        DynamicWideString = 0x8
        Enum = 0x9
        Filename = 0xA
        Flags = 0xB
        Float = 0xC
        Id = 0xD
        Id256 = 0xE
        LocId = 0xF
        Int8 = 0x10
        Int16 = 0x11
        Int = 0x12
        Int64 = 0x13
        NodeHandle = 0x14
        Resource = 0x15
        Seed = 0x16
        StaticArray = 0x17
        String32 = 0x18
        String64 = 0x19
        String128 = 0x1A
        String256 = 0x1B
        String512 = 0x1C
        String1024 = 0x1D
        String2048 = 0x1E
        UInt8 = 0x1F
        UInt16 = 0x20
        UInt = 0x21
        UInt64 = 0x22
        UniqueId = 0x23
        Vector2 = 0x24
        Vector = 0x25
        Vector4 = 0x26
        WideChar = 0x27
        HalfVector4 = 0x28
        PhysRelVec = 0x29

    _fields_ = [
        ("_name", ctypes.c_char_p),
        ("nameHash", ctypes.c_uint32),
        ("categoryName", ctypes.c_char_p),
        ("categoryHash", ctypes.c_uint32),
        ("_type", ctypes.c_int32),
        ("_innerType", ctypes.c_int32),
        ("size", ctypes.c_int32),
        ("count", ctypes.c_int32),
        ("offset", ctypes.c_int32),
        ("classMetadata", ctypes.c_longlong),
        ("_enumLookup", ctypes.c_longlong),
        ("numEnumMembers", ctypes.c_int32),
    ]
    _name: bytes
    nameHash: int
    categoryName: bytes
    categoryHash: int
    _type: int
    _innerType: int
    size: int
    count: int
    offset: int
    classMetadata: int
    _enumLookup: int
    numEnumMembers: int

    @property
    def name(self) -> str:
        return self._name.decode()

    @property
    def type(self):
        return cTkMetaDataMember.eType(self._type)

    @property
    def innerType(self):
        return cTkMetaDataMember.eType(self._innerType)

    @property
    def enumLookup(self):
        _size = ctypes.sizeof(cTkMetaDataEnumLookup)
        for i in range(self.numEnumMembers):
            yield map_struct(self._enumLookup + i * _size, cTkMetaDataEnumLookup)


class cTkMetaDataClass(ctypes.Structure):
    _fields_ = [
        ("_name", ctypes.c_char_p),
        ("nameHash", ctypes.c_ulonglong),
        ("templateHash", ctypes.c_ulonglong),
        ("_members", ctypes.c_ulonglong),
        ("numMembers", ctypes.c_int32),
    ]
    _name: bytes
    nameHash: int
    templateHash: int
    _members: int
    numMembers: int

    @property
    def name(self) -> str:
        return self._name.decode()

    @property
    def members(self) -> Generator[cTkMetaDataMember, None, None]:
        for i in range(self.numMembers):
            yield map_struct(self._members + i * 0x60, cTkMetaDataMember)


class Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float)
    ]


class NVGColor(ctypes.Union):
    _fields_ = [
        ("rgba", ctypes.c_float * 4),
        ("color", Color),
    ]


class cTkMetaDataFunctionLookup(ctypes.Structure):
    _fields_ = [
        ("classMetadata", ctypes.c_longlong),
        ("createDefaultFunction", ctypes.c_longlong),
        ("renderFunction", ctypes.c_longlong),
        ("fixingFunction", ctypes.c_longlong),
        ("validateDataFunction", ctypes.c_longlong),
        ("equalsFunction", ctypes.c_longlong),
        ("copyFunction", ctypes.c_longlong),
        ("createPtrFunction", ctypes.c_longlong),
        ("hashFunction", ctypes.c_longlong),
        ("destroyFunction", ctypes.c_longlong),
    ]


class cTkFSM(ctypes.Structure):
    _fields_ = [
        ("__vftable", ctypes.c_longlong),
        ("OffsetTable", ctypes.c_longlong),
        ("State", ctypes.c_longlong),
        ("RequestedChangeNewState", ctypes.c_char * 0x10),
        ("RequestedChangeUserData", ctypes.c_longlong),
        ("RequestedChangeForceRestart", ctypes.wintypes.BOOLEAN),
    ]


class cGcFirstBootContext(ctypes.Structure):
    _fields_ = [
        ("state", ctypes.c_uint32),
        # TODO: map out...
        ("_rest", ctypes.c_ubyte * 0x3C)
    ]


class cGcRealityManagerData(ctypes.Structure):
    _fields_ = []


class cGcSubstanceTable(ctypes.Structure):
    _fields_ = []


class cGcTechnologyTable(ctypes.Structure):
    _fields_ = []


class cGcRealityManager(ctypes.Structure):
    _fields_ = [
        ("Data", ctypes.POINTER(cGcRealityManagerData)),
        ("SubstanceTable", ctypes.POINTER(cGcSubstanceTable)),
        ("TechnologyTable", ctypes.POINTER(cGcTechnologyTable)),
    ]

    def GenerateProceduralTechnology(self, lProcTechID: bytes, lbExampleForWiki: bool) -> int:
        this = ctypes.addressof(self)
        return call_function("cGcRealityManager::GenerateProceduralTechnology", this, lProcTechID, lbExampleForWiki)


class cGcApplication(ctypes.Structure):
    """The Main Application structure"""
    class Data(ctypes.Structure):
        """Much of the associated application data"""
        _fields_ = [
            ("FirstBootContext", cGcFirstBootContext),
            ("TkMcQmcLFSRStore", ctypes.c_ubyte * 0x18),
            ("RealityManager", cGcRealityManager),
        ]

        FirstBootContext: cGcFirstBootContext
        TkMcQmcLFSRStore: bytes
        RealityManager: cGcRealityManager

    _fields_ = [
        ("baseclass_0", cTkFSM),
        ("data", ctypes.POINTER(Data)),
        ("playerSaveSlot", ctypes.c_uint32),
        ("gameMode", ctypes.c_uint32),
        ("seasonalGameMode", ctypes.c_uint32),
        ("savingEnabled", ctypes.c_ubyte),
        ("fullyBooted", ctypes.c_ubyte),
    ]

    baseclass_0: cTkFSM
    data: _Pointer[Data]
    playerSaveSlot: int
    gameMode: int
    seasonalGameMode: int
    savingEnabled: bool
    fullyBooted: bool


class cGcWaterGlobals(ctypes.Structure):
    _fields_ = [
        ("UseNewWater", ctypes.wintypes.BOOLEAN),
        ("WaveHeight", ctypes.wintypes.FLOAT),
        ("WaveFrequency", ctypes.wintypes.FLOAT),
        ("WaveChoppiness", ctypes.wintypes.FLOAT),
        ("WaveCutoff", ctypes.wintypes.FLOAT),
        ("Epsilon", ctypes.wintypes.FLOAT),
        ("FresnelPow", ctypes.wintypes.FLOAT),
        ("FresnelMul", ctypes.wintypes.FLOAT),
        ("FresnelAlpha", ctypes.wintypes.FLOAT),
        ("FresnelBelowPow", ctypes.wintypes.FLOAT),
        ("FresnelBelowMul", ctypes.wintypes.FLOAT),
        ("FresnelBelowAlpha", ctypes.wintypes.FLOAT),
        ("WaterHeavyAirColour", common.Colour),
    ]

    UseNewWater: bool

class cGcGalacticAddressData(ctypes.Structure):
    _fields_ = [
        ("voxelX", ctypes.c_uint32),
        ("voxelY", ctypes.c_uint32),
        ("voxelZ", ctypes.c_uint32),
        ("solarSystemIndex", ctypes.c_uint32),
        ("planetIndex", ctypes.c_uint32),
    ]

class cGcUniverseAddressData(ctypes.Structure):
    _fields_ = [
        ("realityIndex", ctypes.c_int32),
        ("galacticAddress", cGcGalacticAddressData),
    ]

class cGcPlayerState(ctypes.Structure):
    _fields_ = [
        ("nameWithTitle", ctypes.c_char * 0x100),
        ("titleStatWatcher", ctypes.c_byte * 0x48),
        ("_64ChangeRevision", ctypes.c_ulonglong),
        ("gameStartLocation1", cGcUniverseAddressData),
        ("gameStartLocation2", cGcUniverseAddressData),
        ("location", cGcUniverseAddressData),
        ("prevLocation", cGcUniverseAddressData),
        ("shield", ctypes.c_int32),
        ("health", ctypes.c_int32),
        ("shipHealth", ctypes.c_int32),
        ("units", ctypes.c_uint32),
        ("nanites", ctypes.c_uint32),
        ("specials", ctypes.c_uint32),
    ]

class cGcGameState(ctypes.Structure):
    _fields_ = [
        ("rRIT", ctypes.c_ulonglong),
        ("rRCE", ctypes.c_ulonglong),
        ("rRBB", ctypes.c_ulonglong),
        ("gameStateGroupNode", ctypes.c_ulonglong),
        ("playerState", cGcPlayerState)
    ]

class cGcSolarSystemData(ctypes.Structure):
    _fields_ = [
        ("seed", common.GcSeed),
        ("name", ctypes.c_char * 0x80),
        ("class", ctypes.c_uint32),
        ("starType", ctypes.c_uint32),
        ("planets", ctypes.c_uint32),
    ]

class cGcSolarSystem(ctypes.Structure):
    _fields_ = [
        ("solarSystemData", cGcSolarSystemData),
    ]
    solarSystemData: cGcSolarSystemData


class cGcPlanetData(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char * 0x80),
        ("dummy", ctypes.c_longlong),
    ]
    name: bytes
    dummy: int


class cGcPlanet(ctypes.Structure):
    _fields_ = [
        ("start", ctypes.c_char * 0x58),
        ("planetIndex", ctypes.c_uint32),
        ("planetData", cGcPlanetData),
    ]
    start: bytes
    planetIndex: int
    planetData: cGcPlanetData


class cTkFileSystem(ctypes.Structure):
    class Data(ctypes.Structure):
        _fields_ = [
            ("stuff", ctypes.c_char * 0x2692),
            ("isModded", ctypes.wintypes.BOOLEAN),
        ]
        isModded: bool
    _fields_ = [
        ("data", ctypes.POINTER(Data)),
    ]
    data: _Pointer[Data]

# class cGcHUDTrackArrow(ctypes.Structure):
#     class eReticuleState(IntEnum):
#         EReticule_Inactive = 0x0
#         EReticule_Active = 0x1
#         EReticule_Deactivating = 0x2

#     def cGcHUDTrackArrow(): pass

#     def Construct(): pass

#     def Update(): pass

#     def UpdateRender(): pass

#     def Render(): pass

#     def CalculateTargetSizeAndPos(): pass

#     def GetBorderPos(): pass

#     def SetTarget(): pass

#     def SetFixedTarget(): pass

#     _fields_ = [
#         ("mSize", common.Vector2f),
#         ("mColour", common.Colour),
#         ("mfArrowScale", ctypes.c_float),
#         ("mfFadeTime", ctypes.c_float),
#         ("mbFade", ctypes.c_ubyte),
#         ("maReticules", core.cTkSmartResHandle * 0x18),
#         ("maReticuleGlows", core.cTkSmartResHandle * 0x18),
#         ("maArrows", core.cTkSmartResHandle * 0x18),
#         ("maArrowGlows", core.cTkSmartResHandle * 0x18),
#         ("maIcons", core.cTkSmartResHandle * 0x18),
#         ("maAudioPings", simple.TkAudioID * 0x18),
#         ("mCriticalIcon", core.cTkSmartResHandle),
#         ("mCriticalGlowIcon", core.cTkSmartResHandle),
#         ("mDamageGlow", core.cTkSmartResHandle),
#         ("mEnergyShieldGlow", core.cTkSmartResHandle),
#         ("mTypeIcon", core.cTkSmartResHandle),
#         ("mfTypeIconPulse", ctypes.c_float),
#         ("mfTypeIconFade", ctypes.c_float),
#         ("mafBaseSizes", ctypes.c_float * 0x18),
#         ("mafBaseDotSizes", ctypes.c_float * 0x18),
#         ("meType", eGcTrackArrowTypes),
#         ("mExternalIcon", core.cTkSmartResHandle),
#         ("mpTarget", ctypes.c_uint64),
#         ("mFixedTarget", cTkPhysRelVec3),
#         ("mWorldPos", cTkPhysRelVec3),
#         ("mProjWorldPos", cTkPhysRelVec3),
#         ("mScreenPos", common.Vector2f),
#         ("mReticulePos", common.Vector2f),
#         ("mfAngle", ctypes.c_float),
#         ("mfBorderFactor", ctypes.c_float),
#         ("mfCentreOffsetMultiplier", ctypes.c_float),
#         ("mHealthColour", common.Colour),
#         ("mHealthCriticalHitColour", common.Colour),
#         ("mfHealthBar", ctypes.c_float),
#         ("mfIconFade", ctypes.c_float),
#         ("mbUseLabelOffset", ctypes.c_ubyte),
#         ("mEnergyShieldColour", common.Colour),
#         ("mfEnergyShieldBar", ctypes.c_float),
#         ("mbFixedTarget", ctypes.c_ubyte),
#         ("mbOnScreen", ctypes.c_ubyte),
#         ("mbUsingSmallIcon", ctypes.c_ubyte),
#         ("_meReticuleState", ctypes.c_uint32),
#         ("mfReticuleActiveTime", ctypes.c_float),
#         ("mfReticuleDeactiveTime", ctypes.c_float),
#         ("mfReticuleScale", ctypes.c_float),
#         ("mGlowColour", common.Colour),
#         ("mDamageGlowColour", common.Colour),
#         ("mEnergyShieldGlowColour", common.Colour),
#         ("mText", ctypes.c_char * 0x80),
#         ("mTrackArrowHandle", ctypes.c_uint64),
#         ("mHealthHandle", ctypes.c_uint64),
#     ]
#     mSize: common.Vector2f
#     mColour: common.Colour
#     mfArrowScale: float
#     mfFadeTime: float
#     mbFade: bool
#     maReticules: list[core.cTkSmartResHandle]
#     maReticuleGlows: list[core.cTkSmartResHandle]
#     maArrows: list[core.cTkSmartResHandle]
#     maArrowGlows: list[core.cTkSmartResHandle]
#     maIcons: list[core.cTkSmartResHandle]
#     maAudioPings: list[simple.TkAudioID]
#     mCriticalIcon: core.cTkSmartResHandle
#     mCriticalGlowIcon: core.cTkSmartResHandle
#     mDamageGlow: core.cTkSmartResHandle
#     mEnergyShieldGlow: core.cTkSmartResHandle
#     mTypeIcon: core.cTkSmartResHandle
#     mfTypeIconPulse: float
#     mfTypeIconFade: float
#     mafBaseSizes: list[ctypes.c_float]
#     mafBaseDotSizes: list[ctypes.c_float]
#     meType: local_types.eGcTrackArrowTypes
#     mExternalIcon: core.cTkSmartResHandle
#     mpTarget: int
#     mFixedTarget: cTkPhysRelVec3
#     mWorldPos: cTkPhysRelVec3
#     mProjWorldPos: cTkPhysRelVec3
#     mScreenPos: common.Vector2f
#     mReticulePos: common.Vector2f
#     mfAngle: float
#     mfBorderFactor: float
#     mfCentreOffsetMultiplier: float
#     mHealthColour: common.Colour
#     mHealthCriticalHitColour: common.Colour
#     mfHealthBar: float
#     mfIconFade: float
#     mbUseLabelOffset: bool
#     mEnergyShieldColour: common.Colour
#     mfEnergyShieldBar: float
#     mbFixedTarget: bool
#     mbOnScreen: bool
#     mbUsingSmallIcon: bool
#     _meReticuleState: int
#     mfReticuleActiveTime: float
#     mfReticuleDeactiveTime: float
#     mfReticuleScale: float
#     mGlowColour: common.Colour
#     mDamageGlowColour: common.Colour
#     mEnergyShieldGlowColour: common.Colour
#     mText: bytes
#     mTrackArrowHandle: int
#     mHealthHandle: int

#     @property
#     def meReticuleState(self):
#         return cGcHUDTrackArrow.eReticuleState(self._meReticuleState)


# class cGcShipHUD(ctypes.Structure):
#     class eReticules(IntEnum):
#         EReticule_ShipLaser = 0x0
#         EReticule_ShipProjectile = 0x1
#         EReticule_ShipMissile = 0x2
#         EReticule_NumTypes = 0x3

#     class cGcVehicleScreen(ctypes.Structure):
#         _fields_ = [
#             ("mScreenTexture", cTkDynamicTexture),
#             ("mScreenGUI", cGcNGui),
#             ("mbValid", ctypes.c_ubyte),
#         ]
#         mScreenTexture: cTkDynamicTexture
#         mScreenGUI: cGcNGui
#         mbValid: bool

#     def cGcShipHUD(): pass

#     def RenderNGuiCallback(): pass

#     def LoadData(): pass

#     def Construct(): pass

#     def Update(): pass

#     def UpdateTrackArrows(): pass

#     def UpdateMarkerLockOn(): pass

#     def UpdateRender(): pass

#     def ReadPlanetStats(): pass

#     def RenderOffscreen2D(): pass

#     def Render2D(): pass

#     def RenderHeadsUp(): pass

#     _fields_ = [
#         ("baseclass_0", cGcHUD),
#         ("mHUDLayer", cTk2dLayer),
#         ("mCrosshairOuterCircleLarge", cTk2dImageEx),
#         ("mCrosshairOuterCircleLargeLayer", cTk3dLayer),
#         ("mCrosshairOuterCircleSmall", cTk2dImageEx),
#         ("mCrosshairOuterCircleSmallLayer", cTk3dLayer),
#         ("mMouseArrowLayer", cTk2dLayer),
#         ("mMouseArrowIcon", cTk2dImageEx),
#         ("mShipForwardScreenPos", common.Vector3f),
#         ("mfShipAngle", ctypes.c_float),
#         ("mfShipPitch", ctypes.c_float),
#         ("mLandingEffect", EffectInstance),
#         ("maTrackArrows", cGcHUDTrackArrow * 0x8),
#         ("maShootList", ctypes.c_char * 0x18),  # std::vector<cTkAttachmentPtr,TkSTLAllocatorShim<cTkAttachmentPtr,8,-1> >
#         ("miSelectedPlanet", ctypes.c_int32),
#         ("_meSelectedPlanetLabelState", ctypes.c_uint32),
#         ("mfSelectedPlanetPanelTime", ctypes.c_float),
#         ("mfSelectedPlanetPanelFadeTime", ctypes.c_float),
#         ("mbSelectedPlanetPanelVisible", ctypes.c_ubyte),
#         ("mbSelectedPlanetIsTargeted", ctypes.c_ubyte),
#         ("mfLastKnownScanTime", ctypes.c_float),
#         ("mfScanRevealTimer", ctypes.c_float),
#         ("meMiniJumpState", ePulseDriveState),
#         ("mbHasPulseEncounterOnHUD", ctypes.c_ubyte),
#         ("mapScreens", ctypes.c_ulonglong * 0x2),  # cGcRenderableScreen *[2]
#         ("miCurrentScreen", ctypes.c_int32),
#         ("maSideScreenTextures", cTkDynamicTexture * 0x4),  # cTkDynamicTexture[4]
#         ("maSideScreenGUI", cGcNGui * 0x4),  # cGcNGui[4]
#         ("maSideScreenCursor", common.Vector2f * 0x4),  # cTkVector2[4]
#         ("mbSideScreenActive", ctypes.c_ubyte),
#         ("maSideScreenMeshes", core.TkHandle * 0x4),
#         ("mCurrentCockpit", ctypes.c_uint32),
#         ("maVehicleScreens", cGcShipHUD.cGcVehicleScreen * 0x7),  # cGcShipHUD::cGcVehicleScreen[7]
#         ("mSpeedoReverseMesh", ctypes.c_uint32),
#         ("mSpeedoPulseMesh", ctypes.c_uint32),
#         ("maSpeedoBarsMeshes", core.TkHandle * 0x5),
#         ("miCurrentSpeedoBar", ctypes.c_int32),
#         ("miFinalSpeedReadout", ctypes.c_int32),
#         ("mMainScreenTexture", cTkDynamicTexture),
#         ("mMainScreenGUI", cGcNGui),
#         ("mTargetProcName", ctypes.c_char * 0x7F),  # cTkFixedString<127,char>
#         ("maPlanetWorldPositions", common.Vector3f * 0x6),  # cTkVector3[6]
#         ("maPlanetScreenPositions", common.Vector3f * 0x6),  # cTkVector3[6]
#         ("mHeadsUpGUI", cGcNGui),
#         ("mHeadsUpScreenHandle", ctypes.c_uint64),
#         ("mEnemyTargetSceneRes", core.cTkSmartResHandle),
#         ("mfBoostMultiplier", ctypes.c_float),
#     ]
#     baseclass_0: cGcHUD
#     mHUDLayer: cTk2dLayer
#     mCrosshairOuterCircleLarge: cTk2dImageEx
#     mCrosshairOuterCircleLargeLayer: cTk3dLayer
#     mCrosshairOuterCircleSmall: cTk2dImageEx
#     mCrosshairOuterCircleSmallLayer: cTk3dLayer
#     mMouseArrowLayer: cTk2dLayer
#     mMouseArrowIcon: cTk2dImageEx
#     mShipForwardScreenPos: common.Vector3f
#     mfShipAngle: float
#     mfShipPitch: float
#     mLandingEffect: EffectInstance
#     maTrackArrows: bytes
#     maShootList: bytes
#     miSelectedPlanet: int
#     _meSelectedPlanetLabelState: int
#     mfSelectedPlanetPanelTime: float
#     mfSelectedPlanetPanelFadeTime: float
#     mbSelectedPlanetPanelVisible: bool
#     mbSelectedPlanetIsTargeted: bool
#     mfLastKnownScanTime: float
#     mfScanRevealTimer: float
#     meMiniJumpState: ePulseDriveState
#     mbHasPulseEncounterOnHUD: bool
#     mapScreens: list[ctypes.c_ulonglong]
#     miCurrentScreen: int
#     maSideScreenTextures: list[cTkDynamicTexture]
#     maSideScreenGUI: list[cGcNGui]
#     maSideScreenCursor: list[common.Vector2f]
#     mbSideScreenActive: bool
#     maSideScreenMeshes: list[core.TkHandle]
#     mCurrentCockpit: int
#     maVehicleScreens: list[cGcShipHUD.cGcVehicleScreen]
#     mSpeedoReverseMesh: int
#     mSpeedoPulseMesh: int
#     maSpeedoBarsMeshes: list[core.TkHandle]
#     miCurrentSpeedoBar: int
#     miFinalSpeedReadout: int
#     mMainScreenTexture: cTkDynamicTexture
#     mMainScreenGUI: cGcNGui
#     mTargetProcName: bytes
#     maPlanetWorldPositions: list[common.Vector3f]
#     maPlanetScreenPositions: list[common.Vector3f]
#     mHeadsUpGUI: cGcNGui
#     mHeadsUpScreenHandle: int
#     mEnemyTargetSceneRes: core.cTkSmartResHandle
#     mfBoostMultiplier: float

#     @property
#     def meSelectedPlanetLabelState(self):
#         return ePlanetLabelState(self._meSelectedPlanetLabelState)


class cGcRealitySubstanceCategory(ctypes.Structure):
    _fields_ = [
        ("_meSubstanceCategory", ctypes.c_uint32),
    ]

    _meSubstanceCategory: int

    @property
    def meSubstanceCategory(self):
        return safe_assign_enum(nms_enums.eSubstanceCategory, self._meSubstanceCategory)

    def __str__(self) -> str:
        return str(self.meSubstanceCategory)


class cGcStatsTypes(ctypes.Structure):
    _fields_ = [
        ("_meStatsType", ctypes.c_uint32),
    ]

    _meStatsType: int

    @property
    def meStatsType(self):
        return safe_assign_enum(nms_enums.eStatsType, self._meStatsType)

    def __str__(self) -> str:
        return str(self.meStatsType)


class cGcTechnologyCategory(ctypes.Structure):
    _fields_ = [
        ("_meTechnologyCategory", ctypes.c_uint32),
    ]

    _meTechnologyCategory: int

    @property
    def meTechnologyCategory(self):
        return safe_assign_enum(nms_enums.eTechnologyCategory, self._meTechnologyCategory)

    def __str__(self) -> str:
        return str(self.meTechnologyCategory)


class cGcTechnologyRarity(ctypes.Structure):
    _fields_ = [
        ("_meTechnologyRarity", ctypes.c_uint32),
    ]

    _meTechnologyRarity: int

    @property
    def meTechnologyRarity(self):
        return safe_assign_enum(nms_enums.eTechnologyRarity, self._meTechnologyRarity)

    def __str__(self) -> str:
        return str(self.meTechnologyRarity)


class cTkTextureResource(ctypes.Structure):
    _pack_ = 0x84
    _fields_ = [
        ("macFilename", ctypes.c_char * 0x80),
        ("mResHandle", ctypes.c_uint32),  # TODO cTkSmartResHandle
    ]

    macFilename: bytes

    def __str__(self) -> str:
        return self.macFilename.decode()


class cGcTechnology(ctypes.Structure):
    _fields_ = [
        ("mID", common.TkID[0x10]),
        ("mGroup", common.TkID[0x20]),
        ("macName", common.cTkFixedString[0x80]),
        ("macNameLower", common.cTkFixedString[0x80]),
        ("macSubtitle", common.cTkDynamicString),
        ("macDescription", common.cTkDynamicString),
        ("mbTeach", ctypes.c_ubyte),
        ("_padding0x151", ctypes.c_ubyte * 0x7),
        ("mHintStart", common.TkID[0x20]),
        ("mHintEnd", common.TkID[0x20]),
        ("mIcon", cTkTextureResource),
        ("_padding0x21C", ctypes.c_ubyte * 0x4),
        ("mColour", common.Colour),
        ("miLevel", ctypes.c_int32),
        ("mbChargeable", ctypes.c_ubyte),
        ("miChargeAmount", ctypes.c_int32),
        ("mChargeType", cGcRealitySubstanceCategory),
        ("maChargeBy", common.cTkDynamicArray[ctypes.c_char * 0x10]),
        ("mfChargeMultiplier", ctypes.c_float),
        ("mbBuildFullyCharged", ctypes.c_ubyte),
        ("mbUsesAmmo", ctypes.c_ubyte),
        ("mAmmoId", ctypes.c_char * 0x10),
        ("mbPrimaryItem", ctypes.c_ubyte),
        ("mbUpgrade", ctypes.c_ubyte),
        ("mbCore", ctypes.c_ubyte),
        ("mbRepairTech", ctypes.c_ubyte),
        ("mbProcedural", ctypes.c_ubyte),
        ("mCategory", cGcTechnologyCategory),
        ("mRarity", cGcTechnologyRarity),
        ("mfValue", ctypes.c_float),
    ]
