from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from ctypes import _Pointer

import nmspy.data.struct_types as stypes

import ctypes
import ctypes.wintypes

from nmspy.data import common, enums as nms_enums
from nmspy.calling import call_function
# from nmspy.data.types import core, simple
from nmspy.data.cpptypes import std
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

class cTkLanguageManagerBase(ctypes.Structure):
    _fields_ = [
        ("_dummy0x0", ctypes.c_ubyte * 0x8),
        ("meRegion", ctypes.c_int32),
        ("_dummy0xC", ctypes.c_ubyte * 0x221C),
    ]

    meRegion: int


class cTkModelResource(ctypes.Structure):
    _fields_ = [
        ("macFilename", common.cTkFixedString[0x80]),
        ("mResHandle", ctypes.c_uint32),  # TODO cTkSmartResHandle
    ]

    macFilename: bytes

    def __str__(self) -> str:
        return str(self.macFilename)


class cGcAlienRace(ctypes.Structure):
    _fields_ = [
        ("_meAlienRace", ctypes.c_uint32),
    ]

    _meAlienRace: int

    @property
    def meAlienRace(self):
        return safe_assign_enum(nms_enums.eAlienRace, self._meAlienRace)

    def __str__(self) -> str:
        return str(self.meAlienRace)


class cGcInventoryType(ctypes.Structure):
    _fields_ = [
        ("_meInventoryType", ctypes.c_uint32),
    ]

    _meInventoryType: int

    @property
    def meInventoryType(self):
        return safe_assign_enum(nms_enums.eInventoryType, self._meInventoryType)

    def __str__(self) -> str:
        return str(self.meInventoryType)


class cGcItemPriceModifiers(ctypes.Structure):
    _fields_ = [
        ("mfSpaceStationMarkup", ctypes.c_float),
        ("mfLowPriceMod", ctypes.c_float),
        ("mfHighPriceMod", ctypes.c_float),
        ("mfBuyBaseMarkup", ctypes.c_float),
        ("mfBuyMarkupMod", ctypes.c_float),
    ]

    mfSpaceStationMarkup: float
    mfLowPriceMod: float
    mfHighPriceMod: float
    mfBuyBaseMarkup: float
    mfBuyMarkupMod: float


class cGcLegality(ctypes.Structure):
    _fields_ = [
        ("_meLegality", ctypes.c_uint32),
    ]

    _meLegality: int

    @property
    def meLegality(self):
        return safe_assign_enum(nms_enums.eLegality, self._meLegality)

    def __str__(self) -> str:
        return str(self.meLegality)


class cGcProductCategory(ctypes.Structure):
    _fields_ = [
        ("_meProductCategory", ctypes.c_uint32),
    ]

    _meProductCategory: int

    @property
    def meProductCategory(self):
        return safe_assign_enum(nms_enums.eProductCategory, self._meProductCategory)

    def __str__(self) -> str:
        return str(self.meProductCategory)


class cGcRarity(ctypes.Structure):
    _fields_ = [
        ("_meRarity", ctypes.c_uint32),
    ]

    _meRarity: int

    @property
    def meRarity(self):
        return safe_assign_enum(nms_enums.eRarity, self._meRarity)

    def __str__(self) -> str:
        return str(self.meRarity)


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


class cGcStatsBonus(ctypes.Structure):
    _fields_ = [
        ("mStat", cGcStatsTypes),
        ("mfBonus", ctypes.c_float),
        ("miLevel", ctypes.c_int32),
    ]

    mStat: cGcStatsTypes
    mfBonus: float
    miLevel: int

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.mStat}, {self.mfBonus})"


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
    _fields_ = [
        ("macFilename", common.cTkFixedString[0x80]),
        ("mResHandle", ctypes.c_uint32),  # TODO cTkSmartResHandle
    ]

    macFilename: bytes

    def __str__(self) -> str:
        return str(self.macFilename)


class cGcTechnologyRequirement(ctypes.Structure):
    _fields_ = [
        ("mID", common.TkID[0x10]),
        ("mType", cGcInventoryType),
        ("miAmount", ctypes.c_int32),
    ]

    mID: bytes
    mType: cGcInventoryType
    miAmount: int


class cGcTradeCategory(ctypes.Structure):
    _fields_ = [
        ("_meTradeCategory", ctypes.c_uint32),
    ]

    _meTradeCategory: int

    @property
    def meTradeCategory(self):
        return safe_assign_enum(nms_enums.eTradeCategory, self._meTradeCategory)

    def __str__(self) -> str:
        return str(self.meTradeCategory)


class cGcProductData(ctypes.Structure):
    _fields_ = [
        ("mID", common.TkID[0x10]),
        ("macName", common.cTkFixedString[0x80]),
        ("macNameLower", common.cTkFixedString[0x80]),
        ("macSubtitle", common.cTkDynamicString),
        ("macDescription", common.cTkDynamicString),
        ("mHint", common.TkID[0x20]),
        ("mGroupID", common.TkID[0x10]),
        ("mDebrisFile", cTkModelResource),
        ("miBaseValue", ctypes.c_int32),
        ("miLevel", ctypes.c_int32),
        ("mIcon", cTkTextureResource),
        ("mHeroIcon", cTkTextureResource),
        ("_padding0x2F4", ctypes.c_ubyte * 0xC),
        ("mColour", common.Colour),
        ("mCategory", cGcTechnologyCategory),
        ("mType", cGcProductCategory),
        ("mRarity", cGcRarity),
        ("mLegality", cGcLegality),
        ("mbConsumable", ctypes.c_ubyte),
        ("_padding0x321", ctypes.c_ubyte * 0x3),
        ("miChargeValue", ctypes.c_int32),
        ("miStackMultiplier", ctypes.c_int32),
        ("miDefaultCraftAmount", ctypes.c_int32),
        ("miCraftAmountStepSize", ctypes.c_int32),
        ("miCraftAmountMultiplier", ctypes.c_int32),
        ("maRequirements", common.cTkDynamicArray[cGcTechnologyRequirement]),
        ("maAltRequirements", common.cTkDynamicArray[cGcTechnologyRequirement]),
        ("mCost", cGcItemPriceModifiers),
        ("miRecipeCost", ctypes.c_int32),
        ("mbSpecificChargeOnly", ctypes.c_ubyte),
        ("_padding0x371", ctypes.c_ubyte * 0x3),
        ("mfNormalisedValueOnWorld", ctypes.c_float),
        ("mfNormalisedValueOffWorld", ctypes.c_float),
        ("mTradeCategory", cGcTradeCategory),
        ("_meWikiCategory", ctypes.c_uint32),
        ("mbIsCraftable", ctypes.c_ubyte),
        ("_padding0x385", ctypes.c_ubyte * 0x3),
        ("mDeploysInto", common.TkID[0x10]),
        ("mfEconomyInfluenceMultiplier", ctypes.c_float),
        ("_padding0x39C", ctypes.c_ubyte * 0x4),
        ("mPinObjective", common.TkID[0x20]),
        ("mPinObjectiveTip", common.TkID[0x20]),
        ("mbCookingIngredient", ctypes.c_ubyte),
        ("_padding0x3E1", ctypes.c_ubyte * 0x3),
        ("mfCookingValue", ctypes.c_float),
        ("mbGoodForSelling", ctypes.c_ubyte),
        ("_padding0x3E9", ctypes.c_ubyte * 0x7),
        ("mGiveRewardOnSpecialPurchase", common.TkID[0x10]),
        ("mbEggModifierIngredient", ctypes.c_ubyte),
        ("mbIsTechbox", ctypes.c_ubyte),
        ("mbCanSendToOtherPlayers", ctypes.c_ubyte),
        ("_padding0x403", ctypes.c_ubyte * 0xD),
    ]

    @property
    def meWikiCategory(self):
        return safe_assign_enum(nms_enums.eWikiCategory, self._meWikiCategory)


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
        ("_padding0x235", ctypes.c_ubyte * 0x3),
        ("miChargeAmount", ctypes.c_int32),
        ("mChargeType", cGcRealitySubstanceCategory),
        ("maChargeBy", common.cTkDynamicArray[common.TkID[0x10]]),
        ("mfChargeMultiplier", ctypes.c_float),
        ("mbBuildFullyCharged", ctypes.c_ubyte),
        ("mbUsesAmmo", ctypes.c_ubyte),
        ("_padding0x256", ctypes.c_ubyte * 0x2),
        ("mAmmoId", common.TkID[0x10]),
        ("mbPrimaryItem", ctypes.c_ubyte),
        ("mbUpgrade", ctypes.c_ubyte),
        ("mbCore", ctypes.c_ubyte),
        ("mbRepairTech", ctypes.c_ubyte),
        ("mbProcedural", ctypes.c_ubyte),
        ("_padding0x26B", ctypes.c_ubyte * 0x3),
        ("mCategory", cGcTechnologyCategory),
        ("mRarity", cGcTechnologyRarity),
        ("mfValue", ctypes.c_float),
        ("_padding0x27A", ctypes.c_ubyte * 0x4),
        ("maRequirements", common.cTkDynamicArray[cGcTechnologyRequirement]),
        ("mBaseStat", cGcStatsTypes),
        ("_padding0x28E", ctypes.c_ubyte * 0x4),
        ("maStatBonuses", common.cTkDynamicArray[cGcStatsBonus]),
        ("mRequiredTech", common.TkID[0x10]),
        ("miRequiredLevel", ctypes.c_int32),
        ("_padding0x2B6", ctypes.c_ubyte * 0x4),
        ("mFocusLocator", common.TkID[0x20]),
        ("mUpgradeColour", common.Colour),
        ("mLinkColour", common.Colour),
        ("mRewardGroup", common.TkID[0x10]),
        ("miBaseValue", ctypes.c_int32),
        ("mCost", cGcItemPriceModifiers),
        ("miRequiredRank", ctypes.c_int32),
        ("mDispensingRace", cGcAlienRace),
        ("miFragmentCost", ctypes.c_int32),
        ("mTechShopRarity", cGcTechnologyRarity),
        ("mbWikiEnabled", ctypes.c_ubyte),
        ("_padding0x333", ctypes.c_ubyte * 0x7),
        ("macDamagedDescription", common.cTkDynamicString),
        ("mParentTechId", common.TkID[0x10]),
        ("mbIsTemplate", ctypes.c_ubyte),
        ("_padding0x354", ctypes.c_ubyte * 0xF),
    ]
    mID: bytes


class cGcRealityManager(ctypes.Structure):
    Data: _Pointer["cGcRealityManagerData"]
    SubstanceTable: _Pointer["cGcSubstanceTable"]
    TechnologyTable: _Pointer["cGcTechnologyTable"]
    PendingNewTechnologies: std.vector[_Pointer["cGcTechnology"]]

    @property
    def GenerateProceduralProduct(self) -> stypes.cGcRealityManager.GenerateProceduralProduct:
        return {
            "cGcRealityManager *, int, const cTkSeed *, eRarity, eQuality": self._GenerateProceduralProduct_1,
            "cGcRealityManager *, const TkID<128> *": self._GenerateProceduralProduct_2,
        }

    @property
    def GenerateProceduralTechnologyID(self) -> stypes.cGcRealityManager.GenerateProceduralTechnologyID:
        return {
            "cGcRealityManager *, TkID<128> *, eProceduralTechnologyCategory, const cTkSeed *": self._GenerateProceduralTechnologyID_1,
            "cGcRealityManager *, TkID<128> *, const TkID<128> *, const cTkSeed *": self._GenerateProceduralTechnologyID_2,
        }

    def GenerateProceduralTechnology(self, lProcTechID: bytes, lbExampleForWiki: bool) -> int:
        this = ctypes.addressof(self)
        return call_function("cGcRealityManager::GenerateProceduralTechnology", this, lProcTechID, lbExampleForWiki)

    def _GenerateProceduralProduct_1(self, leProcProdCategory: int, lSeed: int, leRarityOverride: int, leQualityOverride: int):
        this = ctypes.addressof(self)
        return call_function(
            "cGcRealityManager::GenerateProceduralProduct",
            this,
            leProcProdCategory,
            lSeed,
            leRarityOverride,
            leQualityOverride,
            overload="cGcRealityManager *, int, const cTkSeed *, eRarity, eQuality",
        )

    def _GenerateProceduralProduct_2(self, lProcProdID: bytes):
        this = ctypes.addressof(self)
        return call_function(
            "cGcRealityManager::GenerateProceduralProduct",
            this,
            lProcProdID,
            overload="cGcRealityManager *, const TkID<128> *",
        )

    def _GenerateProceduralTechnologyID_1(self, result: int, leProcTechCategory: int, lSeed: int):
        this = ctypes.addressof(self)
        return call_function(
            "cGcRealityManager::GenerateProceduralTechnologyID",
            this,
            result,
            leProcTechCategory,
            lSeed,
            overload="cGcRealityManager *, TkID<128> *, eProceduralTechnologyCategory, const cTkSeed *",
        )

    def _GenerateProceduralTechnologyID_2(self, result: int, lBaseTechID: bytes, lSeed: int):
        this = ctypes.addressof(self)
        return call_function(
            "cGcRealityManager::GenerateProceduralTechnologyID",
            this,
            result,
            lBaseTechID,
            lSeed,
            overload="cGcRealityManager *, TkID<128> *, const TkID<128> *, const cTkSeed *",
        )


cGcRealityManager._fields_ = [
    ("Data", ctypes.POINTER(cGcRealityManagerData)),
    ("SubstanceTable", ctypes.POINTER(cGcSubstanceTable)),
    ("TechnologyTable", ctypes.POINTER(cGcTechnologyTable)),
    ("_padding", ctypes.c_ubyte * 0x220),
    ("PendingNewTechnologies", std.vector[ctypes.POINTER(cGcTechnology)]),
    ("_rest", ctypes.c_ubyte * 0xD20),
]


class cGcPlayerEnvironment(ctypes.Structure):
    mPlayerTM: common.cTkMatrix34
    mUp: common.Vector3f
    mu64UA: int
    miNearestPlanetIndex: int
    mfDistanceFromPlanet: float
    mfNearestPlanetSealevel: float
    mNearestPlanetPos: common.Vector3f
    miNearestPlanetCreatureRoles: int
    _meStarAnomaly: int
    mfDistanceFromAnomaly: float
    mbInsidePlanetAtmosphere: bool
    _meBiome: int
    _meBiomeSubType: int
    mbIsRaining: bool
    mfStormLevel: float
    _meWeather: int
    mfTimeOfDay: float
    mfLightFactor: float
    mfNightFactor: float
    mbIsNight: bool
    mfLightShaftFactor: float
    meLocation: int  # EnvironmentLocation::Enum
    mfTimeInLocation: float
    mbUndergroundIsCave: bool
    meCameraLocation: int  # EnvironmentLocation::Enum
    mfTimeInCameraLocation: float
    meCameraLocationStable: int  # EnvironmentLocation::Enum
    mInsideBuildingNode: int
    _meInterest: int
    mfTimeInInterest: float
    meLocationStable: int  # EnvironmentLocation::Enum
    _meInterestStable: int
    mbInAsteroidFieldStable: bool
    meVehicleLocation: int  # EnvironmentLocation::Enum
    _meNearestBuildingClass: int
    mfNearestBuildingDistance: float
    mbNearestBuildingValid: bool
    _meBasePartAudioLocation: int
    mbPilotingShip: bool
    mbPilotingVehicle: bool
    mbFullControlOfShip: bool
    mbIsWarping: bool
    mbIsWanted: bool
    mbSpaceCombatActive: bool
    mfSpaceCombatActiveTime: float
    mbIsInPlayerFreighter: bool
    mbIsInFreighterBase: bool
    mbForceFreighterShipHidingUpdate: bool
    mOccupiedFreighterOwner: bytes
    mbBlockedFromCraftingBySeasonalBaseRequirements: bool
    mPlanetRegionQueryValid: bool
    # mPlanetRegionQuery : cTkRegionHeightResult
    # mPlanetRegionQueryDistance : float
    # mfUnderwaterDepth : float
    # mfExteriorExposure : float
    # mfTemperature : float
    # mfTemperatureSmoothed : float
    # mfTemperatureExternal : float
    # mfToxicity : float
    # mfToxicitySmoothed : float
    # mfToxicityExternal : float
    # mfRadiation : float
    # mfRadiationSmoothed : float
    # mfRadiationExternal : float
    # mfLifeSupportDrain : float
    # mafHazardFactors : float[6]
    # mafTargetHazardFactors : float[6]
    # mafNormalisedHazardFactors : float[6]
    # mePrimaryHazardControl : eHazardValue
    # maObscuredAroundNear : float[2]
    # maObscuredAroundNearSlow : float[2]
    # maObscuredAroundFar : float[2]
    # maObscuredAroundFarSlow : float[2]
    # maObscuredOverhead : float[2]
    # maObscuredTowardsSun : float[2]
    # mfGlassSurfacesNearby : float
    # mfNearestSurface : float
    # mfNearestSurfaceOverhead : float
    # meCollisionGroupOverhead : eCollisionGroup
    # meCollisionGroupDirectUnder : eCollisionGroup
    # mfDistanceDirectUnder : float
    # meCollisionGroupDirectUnderNA : eCollisionGroup
    # mfDistanceDirectUnderNA : float
    # maGroundCoverage : float[2]
    # mfIndoorLightingFactor : float
    # mfIndoorLightingFactorRate : float
    # mfIndoorLightTransitionFactor : float
    # mbFlyingTowardsPlanet : bool
    # miFlyingTowardsPlanetIndex : int
    # mbSpaceStateValid : bool
    # mSpaceState : cGcPlayerEnvironment::SpaceState
    # mCurrentlyActiveTriggers : cTkStackVector<cGcPlayerEnvironment::ActiveTriggerVolume,16,-1>
    # mbInteriorTriggerTypeActive : bool
    # mbCoveredExteriorTriggerTypeActive : bool
    # mbInsideHazardProtectionVolume : bool
    # mbInsideHazardProtectionColdVolume : bool
    # mbInsideSpaceStorm : bool
    # mfTemperatureSpringRate : float
    # mfToxicitySpringRate : float
    # mfRadiationSpringRate : float
    # maObscuredAroundNearRate : float[2]
    # maObscuredAroundNearRateSlow : float[2]
    # maObscuredAroundFarRate : float[2]
    # maObscuredAroundFarRateSlow : float[2]
    # maObscuredOverheadRate : float[2]
    # maObscuredTowardsSunRate : float[2]
    # maGroundCoverageRate : float[2]
    # mfNearestSurfaceRate : float
    # mfNearestSurfaceOverheadRate : float
    # mfGlassSurfacesNearbyRate : float
    # mbInAsteroidField : bool
    # mfAsteroidFieldStateTime : float

    @property
    def meStarAnomaly(self):
        return safe_assign_enum(nms_enums.eGalaxyStarAnomaly, self._meStarAnomaly)

    @property
    def meBiome(self):
        return safe_assign_enum(nms_enums.eBiome, self._meBiome)

    @property
    def meBiomeSubType(self):
        return safe_assign_enum(nms_enums.eBiomeSubType, self._meBiomeSubType)

    @property
    def meWeather(self):
        return safe_assign_enum(nms_enums.eWeather, self._meWeather)

    @property
    def meInterest(self):
        return safe_assign_enum(nms_enums.eRegionKnowledgeInterest, self._meInterest)

    @property
    def meInterestStable(self):
        return safe_assign_enum(nms_enums.eRegionKnowledgeInterest, self._meInterestStable)

    @property
    def meNearestBuildingClass(self):
        return safe_assign_enum(nms_enums.eBuildingClass, self._meNearestBuildingClass)

    @property
    def meBasePartAudioLocation(self):
        return safe_assign_enum(nms_enums.eBasePartAudioLocation, self._meBasePartAudioLocation)


cGcPlayerEnvironment._fields_ = [
    ("mPlayerTM", common.cTkMatrix34),
    ("mUp", common.Vector3f),
    ("_dummy0x4C", ctypes.c_ubyte * 0x4),
    ("mu64UA",  ctypes.c_ulonglong),
    ("miNearestPlanetIndex", ctypes.c_int32),
    ("mfDistanceFromPlanet", ctypes.c_float),
    ("mfNearestPlanetSealevel", ctypes.c_float),
    ("_dummy0x64", ctypes.c_ubyte * 0xC),
    ("mNearestPlanetPos", common.Vector3f),
    ("_dummy0x7C", ctypes.c_ubyte * 0x4),
    ("miNearestPlanetCreatureRoles", ctypes.c_int32),
    ("meStarAnomaly", ctypes.c_uint32),  # eGalaxyStarAnomaly
    ("mfDistanceFromAnomaly", ctypes.c_float),
    ("mbInsidePlanetAtmosphere", ctypes.c_byte),
    ("meBiome", ctypes.c_uint32),  # eBiome
    ("meBiomeSubType", ctypes.c_uint32),  # eBiomeSubType
    ("mbIsRaining", ctypes.c_byte),
    ("mfStormLevel", ctypes.c_float),
    ("meWeather",  ctypes.c_uint32),  # eWeather
    ("mfTimeOfDay", ctypes.c_float),
    ("mfLightFactor", ctypes.c_float),
    ("mfNightFactor", ctypes.c_float),
    ("mbIsNight", ctypes.c_byte),
    ("mfLightShaftFactor", ctypes.c_float),
    ("meLocation", ctypes.c_uint32),  # EnvironmentLocation::Enum
    ("mfTimeInLocation", ctypes.c_float),
    ("mbUndergroundIsCave", ctypes.c_byte),
    ("meCameraLocation", ctypes.c_uint32),  # EnvironmentLocation::Enum
    ("mfTimeInCameraLocation", ctypes.c_float),
    ("meCameraLocationStable", ctypes.c_uint32),  # EnvironmentLocation::Enum
    ("mInsideBuildingNode", ctypes.c_uint32),  # TkHandle
    ("meInterest", ctypes.c_uint32),  # eRegionKnowledgeInterest
    ("mfTimeInInterest", ctypes.c_float),
    ("meLocationStable", ctypes.c_uint32),  # EnvironmentLocation::Enum
    ("meInterestStable", ctypes.c_uint32),  # eRegionKnowledgeInterest
    ("mbInAsteroidFieldStable", ctypes.c_byte),
    ("meVehicleLocation", ctypes.c_uint32),  # EnvironmentLocation::Enum
    ("meNearestBuildingClass", ctypes.c_uint32),  # eBuildingClass
    ("mfNearestBuildingDistance", ctypes.c_float),
    ("mbNearestBuildingValid", ctypes.c_byte),
    ("meBasePartAudioLocation", ctypes.c_uint32),  # eBasePartAudioLocation
    ("mbPilotingShip", ctypes.c_byte),
    ("mbPilotingVehicle", ctypes.c_byte),
    ("mbFullControlOfShip", ctypes.c_byte),
    ("mbIsWarping", ctypes.c_byte),
    ("mbIsWanted", ctypes.c_byte),
    ("mbSpaceCombatActive", ctypes.c_byte),
    ("mfSpaceCombatActiveTime", ctypes.c_float),
    ("mbIsInPlayerFreighter", ctypes.c_byte),
    ("mbIsInFreighterBase", ctypes.c_byte),
    ("mbForceFreighterShipHidingUpdate", ctypes.c_byte),
    ("mOccupiedFreighterOwner", ctypes.c_char * 0x40),  # cTkUserIdBase<cTkFixedString<64,char> >
    ("mbBlockedFromCraftingBySeasonalBaseRequirements", ctypes.c_byte),
    ("mPlanetRegionQueryValid", ctypes.c_byte),
    # ("mPlanetRegionQuery",  cTkRegionHeightResult), 336 48
    # ("mPlanetRegionQueryDistance", ctypes.c_float), 384 4
    # ("mfUnderwaterDepth", ctypes.c_float), 388 4
    # ("mfExteriorExposure", ctypes.c_float), 392 4
    # ("mfTemperature", ctypes.c_float), 396 4
    # ("mfTemperatureSmoothed", ctypes.c_float), 400 4
    # ("mfTemperatureExternal", ctypes.c_float), 404 4
    # ("mfToxicity", ctypes.c_float), 408 4
    # ("mfToxicitySmoothed", ctypes.c_float), 412 4
    # ("mfToxicityExternal", ctypes.c_float), 416 4
    # ("mfRadiation", ctypes.c_float), 420 4
    # ("mfRadiationSmoothed", ctypes.c_float), 424 4
    # ("mfRadiationExternal", ctypes.c_float), 428 4
    # ("mfLifeSupportDrain", ctypes.c_float), 432 4
    # ("mafHazardFactors",  float[6]), 436 24
    # ("mafTargetHazardFactors",  float[6]), 460 24
    # ("mafNormalisedHazardFactors",  float[6]), 484 24
    # ("mePrimaryHazardControl",  eHazardValue), 508 4
    # ("maObscuredAroundNear",  float[2]), 512 8
    # ("maObscuredAroundNearSlow",  float[2]), 520 8
    # ("maObscuredAroundFar",  float[2]), 528 8
    # ("maObscuredAroundFarSlow",  float[2]), 536 8
    # ("maObscuredOverhead",  float[2]), 544 8
    # ("maObscuredTowardsSun",  float[2]), 552 8
    # ("mfGlassSurfacesNearby", ctypes.c_float), 560 4
    # ("mfNearestSurface", ctypes.c_float), 564 4
    # ("mfNearestSurfaceOverhead", ctypes.c_float), 568 4
    # ("meCollisionGroupOverhead",  eCollisionGroup), 572 4
    # ("meCollisionGroupDirectUnder",  eCollisionGroup), 576 4
    # ("mfDistanceDirectUnder", ctypes.c_float), 580 4
    # ("meCollisionGroupDirectUnderNA",  eCollisionGroup), 584 4
    # ("mfDistanceDirectUnderNA", ctypes.c_float), 588 4
    # ("maGroundCoverage",  float[2]), 592 8
    # ("mfIndoorLightingFactor", ctypes.c_float), 600 4
    # ("mfIndoorLightingFactorRate", ctypes.c_float), 604 4
    # ("mfIndoorLightTransitionFactor", ctypes.c_float), 608 4
    # ("mbFlyingTowardsPlanet", ctypes.c_byte), 612 1
    # ("miFlyingTowardsPlanetIndex", ctypes.c_int32), 616 4
    # ("mbSpaceStateValid", ctypes.c_byte), 620 1
    # ("mSpaceState",  cGcPlayerEnvironment::SpaceState), 624 16
    # ("mCurrentlyActiveTriggers",  cTkStackVector<cGcPlayerEnvironment::ActiveTriggerVolume,16,-1>), 640 176
    # ("mbInteriorTriggerTypeActive", ctypes.c_byte), 816 1
    # ("mbCoveredExteriorTriggerTypeActive", ctypes.c_byte), 817 1
    # ("mbInsideHazardProtectionVolume", ctypes.c_byte), 818 1
    # ("mbInsideHazardProtectionColdVolume", ctypes.c_byte), 819 1
    # ("mbInsideSpaceStorm", ctypes.c_byte), 820 1
    # ("mfTemperatureSpringRate", ctypes.c_float), 824 4
    # ("mfToxicitySpringRate", ctypes.c_float), 828 4
    # ("mfRadiationSpringRate", ctypes.c_float), 832 4
    # ("maObscuredAroundNearRate",  float[2]), 836 8
    # ("maObscuredAroundNearRateSlow",  float[2]), 844 8
    # ("maObscuredAroundFarRate",  float[2]), 852 8
    # ("maObscuredAroundFarRateSlow",  float[2]), 860 8
    # ("maObscuredOverheadRate",  float[2]), 868 8
    # ("maObscuredTowardsSunRate",  float[2]), 876 8
    # ("maGroundCoverageRate",  float[2]), 884 8
    # ("mfNearestSurfaceRate", ctypes.c_float), 892 4
    # ("mfNearestSurfaceOverheadRate", ctypes.c_float), 896 4
    # ("mfGlassSurfacesNearbyRate", ctypes.c_float), 900 4
    # ("mbInAsteroidField", ctypes.c_byte), 904 1
    # ("mfAsteroidFieldStateTime", ctypes.c_float), 908 4
]


class cGcEnvironment(ctypes.Structure):
    playerEnvironment: cGcPlayerEnvironment


cGcEnvironment._fields_ = [
    ("dummy", ctypes.c_ubyte * 0x6D0),
    ("playerEnvironment", cGcPlayerEnvironment)
]


class cGcSimulation(ctypes.Structure):
    environment: cGcEnvironment


cGcSimulation._fields_ = [
    ("dummy", ctypes.c_ubyte * 0x997F0),
    ("environment", cGcEnvironment)
]


class cTkInputPort(ctypes.Structure):
    _fields_ = [
        ("inputManager", ctypes.c_longlong),
        # TODO: Add more...
    ]

    inputManager: int

    def SetButton(self, leIndex: nms_enums.eInputButton) -> None:
        """ Set the provided button as pressed. """
        this = ctypes.addressof(self)
        return call_function("cTkInputPort::SetButton", this, leIndex)

    @staticmethod
    def SetButton_(this: int, leIndex: nms_enums.eInputButton) -> None:
        """ Set the provided button as pressed for the provided instance. """
        return call_function("cTkInputPort::SetButton", this, leIndex)


class cGcApplication(ctypes.Structure):
    """The Main Application structure"""
    class Data(ctypes.Structure):
        """Much of the associated application data"""
        FirstBootContext: cGcFirstBootContext
        TkMcQmcLFSRStore: bytes
        RealityManager: cGcRealityManager
        Simulation: cGcSimulation

    baseclass_0: cTkFSM
    data: _Pointer[Data]
    playerSaveSlot: int
    gameMode: int
    seasonalGameMode: int
    savingEnabled: bool
    fullyBooted: bool


cGcApplication.Data._fields_ = [
    ("FirstBootContext", cGcFirstBootContext),
    ("TkMcQmcLFSRStore", ctypes.c_ubyte * 0x18),
    ("RealityManager", cGcRealityManager),
    ("_padding_0xFC8", ctypes.c_ubyte * 0x8),
    ("GameState", ctypes.c_ubyte * 0x43c560),  # +0xFD0
    ("SeasonalData", ctypes.c_ubyte * 0x69F0),  # +0x43D530'
    ("Simulation", cGcSimulation),  # +0x443F20
]


cGcApplication._fields_ = [
    ("baseclass_0", cTkFSM),
    ("data", ctypes.POINTER(cGcApplication.Data)),
    ("playerSaveSlot", ctypes.c_uint32),
    ("gameMode", ctypes.c_uint32),
    ("seasonalGameMode", ctypes.c_uint32),
    ("savingEnabled", ctypes.c_ubyte),
    ("fullyBooted", ctypes.c_ubyte),
]