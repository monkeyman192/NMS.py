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


class cGcSolarSystemClass(ctypes.Structure):
    _meSolarSystemClass: ctypes.c_int32

cGcSolarSystemClass._fields_ = [
    ("_meSolarSystemClass", ctypes.c_int32),
]


class cGcGalaxyStarTypes(ctypes.Structure):
    _meGalaxyStarType: ctypes.c_int32

cGcGalaxyStarTypes._fields_ = [
    ("_meGalaxyStarType", ctypes.c_int32),
]


class cGcPlanetClass(ctypes.Structure):
    _mePlanetClass: ctypes.c_int32

cGcPlanetClass._fields_ = [
    ("_mePlanetClass", ctypes.c_int32),
]


class cGcPlanetSize(ctypes.Structure):
    _mePlanetSize: ctypes.c_int32

cGcPlanetSize._fields_ = [
    ("_mePlanetSize", ctypes.c_int32),
]


class cGcBiomeType(ctypes.Structure):
    _meBiome: ctypes.c_int32

cGcBiomeType._fields_ = [
    ("_meBiome", ctypes.c_int32),
]


class cGcBiomeSubType(ctypes.Structure):
    _meBiomeSubType: ctypes.c_int32

cGcBiomeSubType._fields_ = [
    ("_meBiomeSubType", ctypes.c_int32),
]


class cGcPlanetGenerationInputData(ctypes.Structure):
    seed: common.GcSeed
    star: "cGcGalaxyStarTypes"
    class_: "cGcPlanetClass"
    commonSubstance: common.TkID[0x10]
    rareSubstance: common.TkID[0x10]
    planetSize: "cGcPlanetSize"
    biome: "cGcBiomeType"
    biomeSubType: "cGcBiomeSubType"
    hasRings: bool
    forceContinents: bool
    inEmptySystem: bool
    inAbandonedSystem: bool
    inPirateSystem: bool
    prime: bool
    realityIndex: int

cGcPlanetGenerationInputData._fields_ = [
    ("seed", common.GcSeed),
    ("star", cGcGalaxyStarTypes),
    ("class_", cGcPlanetClass),
    ("commonSubstance", common.TkID[0x10]),
    ("rareSubstance", common.TkID[0x10]),
    ("planetSize", cGcPlanetSize),
    ("biome", cGcBiomeType),
    ("biomeSubType", cGcBiomeSubType),
    ("hasRings", ctypes.c_ubyte),
    ("forceContinents", ctypes.c_ubyte),
    ("inEmptySystem", ctypes.c_ubyte),
    ("inAbandonedSystem", ctypes.c_ubyte),
    ("inPirateSystem", ctypes.c_ubyte),
    ("prime", ctypes.c_ubyte),
    ("padding0x4A", ctypes.c_ubyte * 0x2),
    ("realityIndex", ctypes.c_int32),
]


class cGcSolarSystemData(ctypes.Structure):
    seed: common.GcSeed
    name: common.cTkFixedString[0x80]
    class_: "cGcSolarSystemClass"
    starType: "cGcGalaxyStarTypes"
    planets: int
    planetPositions: list[common.Vector3f]
    planetGenerationInputs: list[cGcPlanetGenerationInputData]
    planetOrbits: list[int]
    primePlanets: int
    sunPosition: common.Vector3f
    asteroidSubstanceID: common.TkID[0x10]
    numTradeRoutes: int
    numVisibleTradeRoutes: int
    maxNumFreighters: int
    startWithFreighters: bool
    freighterTimer: common.Vector2f
    spacePirateTimer: common.Vector2f
    planetPirateTimer: common.Vector2f
    flybyTimer: common.Vector2f
    policeTimer: common.Vector2f
    # spaceStationSpawn: "cGcSpaceStationSpawnData"
    # traderSpawnOnOutposts: "cGcSolarSystemTraderSpawnData"
    # traderSpawnInStations: "cGcSolarSystemTraderSpawnData"
    # locators: common.cTkDynamicArray[cGcSolarSystemLocator]
    # asteroidGenerators: common.cTkDynamicArray[common.cTkClassPointer]
    # _meAsteroidLevel: ctypes.c_int32
    # colours: "cGcPlanetColourData"
    # light: "cGcLightProperties"
    # sky: "cGcSpaceSkyProperties"
    # screenFilter: "cGcScreenFilters"
    # heavyAir: common.cTkFixedString[0x80]
    # systemShips: common.cTkDynamicArray[cGcAISpaceshipPreloadCacheData]
    # inhabitingRace: "cGcAlienRace"
    # tradingData: "cGcPlanetTradingData"
    # conflictData: "cGcPlayerConflictData"

cGcSolarSystemData._fields_ = [
    ("seed", common.GcSeed),
    ("name", common.cTkFixedString[0x80]),
    ("class_", cGcSolarSystemClass),
    ("starType", cGcGalaxyStarTypes),
    ("planets", ctypes.c_int32),
    ("padding0x9C", ctypes.c_ubyte * 0x4),
    ("planetPositions", common.Vector3f * 0x8),
    ("planetGenerationInputs", cGcPlanetGenerationInputData * 0x8),
    ("planetOrbits", ctypes.c_int32 * 0x8),
    ("primePlanets", ctypes.c_int32),
    ("padding0x3C4", ctypes.c_ubyte * 0xC),
    ("sunPosition", common.Vector3f),
    ("asteroidSubstanceID", common.TkID[0x10]),
    ("numTradeRoutes", ctypes.c_int32),
    ("numVisibleTradeRoutes", ctypes.c_int32),
    ("maxNumFreighters", ctypes.c_int32),
    ("startWithFreighters", ctypes.c_ubyte),
    ("padding0x3FD", ctypes.c_ubyte * 0x3),
    ("freighterTimer", common.Vector2f),
    ("spacePirateTimer", common.Vector2f),
    ("planetPirateTimer", common.Vector2f),
    ("flybyTimer", common.Vector2f),
    ("policeTimer", common.Vector2f),
    ("padding0x428", ctypes.c_ubyte * 0x8),
    # ("spaceStationSpawn", cGcSpaceStationSpawnData),
    # ("traderSpawnOnOutposts", cGcSolarSystemTraderSpawnData),
    # ("traderSpawnInStations", cGcSolarSystemTraderSpawnData),
    # ("locators", common.cTkDynamicArray[cGcSolarSystemLocator]),
    # ("asteroidGenerators", common.cTkDynamicArray[common.cTkClassPointer]),
    # ("_meAsteroidLevel", ctypes.c_int32),
    # ("padding0x5BC", ctypes.c_ubyte * 0x4),
    # ("colours", cGcPlanetColourData),
    # ("light", cGcLightProperties),
    # ("sky", cGcSpaceSkyProperties),
    # ("screenFilter", cGcScreenFilters),
    # ("heavyAir", common.cTkFixedString[0x80]),
    # ("padding0x2084", ctypes.c_ubyte * 0x4),
    # ("systemShips", common.cTkDynamicArray[cGcAISpaceshipPreloadCacheData]),
    # ("inhabitingRace", cGcAlienRace),
    # ("tradingData", cGcPlanetTradingData),
    # ("conflictData", cGcPlayerConflictData),
]

class cGcSolarSystem(ctypes.Structure):
    _fields_ = [
        ("solarSystemData", cGcSolarSystemData),
    ]
    solarSystemData: cGcSolarSystemData


class cTkPersonalRNG(ctypes.Structure):
    state0: int
    state1: int

cTkPersonalRNG._fields_ = [
    ("state0", ctypes.c_uint32),
    ("state1", ctypes.c_uint32),
]


class cGcSolarSystemGeometry(ctypes.Structure):
    planetSpheres: bytes
    planetExclusion: bytes

cGcSolarSystemGeometry._fields_ = [
    ("planetSpheres", ctypes.c_ubyte * 0x100),
    ("planetExclusion", ctypes.c_ubyte * 0x100),
]


class cGcSolarSystemGenerator(ctypes.Structure):
    class GenerationData(ctypes.Structure):
        solarSystem: _Pointer["cGcSolarSystem"]
        metaData: _Pointer["cGcSolarSystemData"]
        # infomap: _Pointer["cGcSolarSystemAsteroidFields"]

    GenerationData._fields_ = [
        ("solarSystem", ctypes.POINTER(cGcSolarSystem)),
        ("metaData", ctypes.POINTER(cGcSolarSystemData)),
        # ("infomap", ctypes.POINTER(cGcSolarSystemAsteroidFields)),
    ]


    generatedLocators: bytes
    RNG: "cTkPersonalRNG"
    geometry: "cGcSolarSystemGeometry"
    skyColours: bytes
    loggingActive: bool

cGcSolarSystemGenerator._fields_ = [
    ("generatedLocators", ctypes.c_ubyte * 0x640),
    ("RNG", cTkPersonalRNG),
    ("padding0x648", ctypes.c_ubyte * 0x8),
    ("geometry", cGcSolarSystemGeometry),
    ("skyColours", ctypes.c_ubyte * 0x10),
    ("loggingActive", ctypes.c_ubyte),
]


class cGcPlanetData(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char * 0x80),
        ("padding", ctypes.c_ubyte * 15904),
    ]
    name: bytes


class cGcTerrainRegionMapOcttree(ctypes.Structure):
    class sTableEntry(ctypes.Structure):
        _bf_0: int

    sTableEntry._fields_ = [
        ("_bf_0", ctypes.c_int16),
    ]


    class sNode(ctypes.Structure):
        region: bytes

    sNode._fields_ = [
        ("region", ctypes.c_ubyte * 0x8),
    ]


    class sNodePos(ctypes.Structure):
        X: int
        Y: int
        Z: int

    sNodePos._fields_ = [
        ("X", ctypes.c_uint16),
        ("Y", ctypes.c_uint16),
        ("Z", ctypes.c_uint16),
    ]


    rootTable: bytes
    rootNodeIndices: bytes
    rootNodeHashes: bytes
    nodes: bytes
    positions: bytes
    depths: bytes
    parents: bytes
    children: bytes
    numNodes: int
    numRootNodes: int
    numLODs: int
    rootMask: int
    mapScale: float
    mapOffset: float
    addingRoots: bool

cGcTerrainRegionMapOcttree._fields_ = [
    ("rootTable", ctypes.c_ubyte * 0x1000),
    ("rootNodeIndices", ctypes.c_ubyte * 0x800),
    ("rootNodeHashes", ctypes.c_ubyte * 0x4E20),
    ("nodes", ctypes.c_ubyte * 0x13880),
    ("positions", ctypes.c_ubyte * 0xEA60),
    ("depths", ctypes.c_ubyte * 0x2710),
    ("parents", ctypes.c_ubyte * 0x4E20),
    ("children", ctypes.c_ubyte * 0x4E20),
    ("numNodes", ctypes.c_uint16),
    ("numRootNodes", ctypes.c_uint16),
    ("numLODs", ctypes.c_uint16),
    ("rootMask", ctypes.c_uint16),
    ("mapScale", ctypes.c_double),
    ("mapOffset", ctypes.c_double),
    ("addingRoots", ctypes.c_ubyte),
]


class cTkTerrainVertex(ctypes.Structure):
    position: "common.cTkHalfVector4"
    tile: "common.cTkHalfVector4"
    texCoords_Normal: "common.cTkHalfVector4"
    texCenter_DPDU: "common.cTkHalfVector4"

cTkTerrainVertex._fields_ = [
    ("position", common.cTkHalfVector4),
    ("tile", common.cTkHalfVector4),
    ("texCoords_Normal", common.cTkHalfVector4),
    ("texCenter_DPDU", common.cTkHalfVector4),
]


class cTkTerrainVertexData(ctypes.Structure):
    vertexArray: _Pointer["cTkTerrainVertex"]
    numVertices: int
    maxNumVertices: int

cTkTerrainVertexData._fields_ = [
    ("vertexArray", ctypes.POINTER(cTkTerrainVertex)),
    ("numVertices", ctypes.c_int32),
    ("maxNumVertices", ctypes.c_int32),
]


class cTkRegionMapBase_vtbl(ctypes.Structure):
    GetScaleX: bytes
    GetScaleY: bytes
    GetScaleZ: bytes
    GetCentre: bytes

cTkRegionMapBase_vtbl._fields_ = [
    ("GetScaleX", ctypes.c_ubyte * 0x8),
    ("GetScaleY", ctypes.c_ubyte * 0x8),
    ("GetScaleZ", ctypes.c_ubyte * 0x8),
    ("GetCentre", ctypes.c_ubyte * 0x8),
]


class cTkVoxel(ctypes.Structure):
    pack_Edit1_Mat4_Secmat4_Tex6: int
    pack_Density16: int
    pack_TileBlend16: int

cTkVoxel._fields_ = [
    ("pack_Edit1_Mat4_Secmat4_Tex6", ctypes.c_uint16),
    ("pack_Density16", ctypes.c_uint16),
    ("pack_TileBlend16", ctypes.c_uint16),
]


class cTkVoxelArray(ctypes.Structure):
    voxels: _Pointer["cTkVoxel"]
    sizeX: int
    sizeY: int
    sizeZ: int
    sizeZY: int
    voxelMaterialMask: int

cTkVoxelArray._fields_ = [
    ("voxels", ctypes.POINTER(cTkVoxel)),
    ("sizeX", ctypes.c_int32),
    ("sizeY", ctypes.c_int32),
    ("sizeZ", ctypes.c_int32),
    ("sizeZY", ctypes.c_int32),
    ("voxelMaterialMask", ctypes.c_uint32),
]


class cTkRegionMapBase(ctypes.Structure):
    __vftable: _Pointer["cTkRegionMapBase_vtbl"]

cTkRegionMapBase._fields_ = [
    ("__vftable", ctypes.POINTER(cTkRegionMapBase_vtbl)),
]


class cTkRegion_vtbl(ctypes.Structure):
    cTkRegion_dtor_0: bytes
    Construct: bytes
    Destruct: bytes
    UpdateMatrix: bytes
    Assign: bytes
    PostPolygonise: bytes
    PostPolygonisePopulate: bytes
    KnowledgeBuilt: bytes
    PollToUnmapStreams: bytes
    TryToClear: bytes
    Invalidate: bytes
    Clear: bytes
    RefreshKnowledge: bytes
    RefreshFoliage: bytes
    GetResource: bytes
    GetStatusColour: bytes
    GenerateVoxels: bytes
    Polygonise: bytes
    BuildKnowledge: bytes
    InvalidateKnowledge: bytes
    AreResourcesLoaded: bytes

cTkRegion_vtbl._fields_ = [
    ("cTkRegion_dtor_0", ctypes.c_ubyte * 0x8),
    ("Construct", ctypes.c_ubyte * 0x8),
    ("Destruct", ctypes.c_ubyte * 0x8),
    ("UpdateMatrix", ctypes.c_ubyte * 0x8),
    ("Assign", ctypes.c_ubyte * 0x8),
    ("PostPolygonise", ctypes.c_ubyte * 0x8),
    ("PostPolygonisePopulate", ctypes.c_ubyte * 0x8),
    ("KnowledgeBuilt", ctypes.c_ubyte * 0x8),
    ("PollToUnmapStreams", ctypes.c_ubyte * 0x8),
    ("TryToClear", ctypes.c_ubyte * 0x8),
    ("Invalidate", ctypes.c_ubyte * 0x8),
    ("Clear", ctypes.c_ubyte * 0x8),
    ("RefreshKnowledge", ctypes.c_ubyte * 0x8),
    ("RefreshFoliage", ctypes.c_ubyte * 0x8),
    ("GetResource", ctypes.c_ubyte * 0x8),
    ("GetStatusColour", ctypes.c_ubyte * 0x8),
    ("GenerateVoxels", ctypes.c_ubyte * 0x8),
    ("Polygonise", ctypes.c_ubyte * 0x8),
    ("BuildKnowledge", ctypes.c_ubyte * 0x8),
    ("InvalidateKnowledge", ctypes.c_ubyte * 0x8),
    ("AreResourcesLoaded", ctypes.c_ubyte * 0x8),
]


class cTkRegion(ctypes.Structure):
    __vftable: _Pointer["cTkRegion_vtbl"]
    regionMap: _Pointer["cTkRegionMapBase"]
    regionData: _Pointer["cTkVoxelArray"]
    node: common.TkHandle
    parentNode: common.TkHandle
    resource: common.cTkSmartResHandle
    _meStatus: ctypes.c_int32
    edited: bool
    clearRequested: bool
    empty: bool
    pendingEditUpdate: bool
    pendingRefresh: bool
    pendingKnowledgeRefresh: bool
    scaleX: int
    scaleY: int
    scaleZ: int
    offsetX: int
    offsetY: int
    offsetZ: int
    sizeX: int
    sizeY: int
    sizeZ: int
    voxelsX: int
    voxelsY: int
    voxelsZ: int
    diameter: int
    border: int
    normal: common.Vector3f
    cubeMatrix: "common.cTkMatrix34"
    tileFlags: int

cTkRegion._fields_ = [
    ("__vftable", ctypes.POINTER(cTkRegion_vtbl)),
    ("padding0x8", ctypes.c_ubyte * 0x8),
    ("regionMap", ctypes.POINTER(cTkRegionMapBase)),
    ("regionData", ctypes.POINTER(cTkVoxelArray)),
    ("node", common.TkHandle),
    ("parentNode", common.TkHandle),
    ("resource", common.cTkSmartResHandle),
    ("_meStatus", ctypes.c_int32),
    ("edited", ctypes.c_ubyte),
    ("clearRequested", ctypes.c_ubyte),
    ("empty", ctypes.c_ubyte),
    ("pendingEditUpdate", ctypes.c_ubyte),
    ("pendingRefresh", ctypes.c_ubyte),
    ("pendingKnowledgeRefresh", ctypes.c_ubyte),
    ("padding0x33", ctypes.c_ubyte * 0x1),
    ("scaleX", ctypes.c_int32),
    ("scaleY", ctypes.c_int32),
    ("scaleZ", ctypes.c_int32),
    ("offsetX", ctypes.c_int32),
    ("offsetY", ctypes.c_int32),
    ("offsetZ", ctypes.c_int32),
    ("sizeX", ctypes.c_int32),
    ("sizeY", ctypes.c_int32),
    ("sizeZ", ctypes.c_int32),
    ("voxelsX", ctypes.c_int32),
    ("voxelsY", ctypes.c_int32),
    ("voxelsZ", ctypes.c_int32),
    ("diameter", ctypes.c_int32),
    ("border", ctypes.c_int32),
    ("padding0x6C", ctypes.c_ubyte * 0x4),
    ("normal", common.Vector3f),
    ("cubeMatrix", common.cTkMatrix34),
    ("tileFlags", ctypes.c_int32),
]


class cGcFadeNodeBase_vtbl(ctypes.Structure):
    SetNodeActivation: bytes
    CheckNodeActivation: bytes
    SetNodeParamF: bytes
    Update: bytes

cGcFadeNodeBase_vtbl._fields_ = [
    ("SetNodeActivation", ctypes.c_ubyte * 0x8),
    ("CheckNodeActivation", ctypes.c_ubyte * 0x8),
    ("SetNodeParamF", ctypes.c_ubyte * 0x8),
    ("Update", ctypes.c_ubyte * 0x8),
]


class cGcFadeNodeBase(ctypes.Structure):
    __vftable: _Pointer["cGcFadeNodeBase_vtbl"]
    timer: float
    totalTime: float
    nodeParam: int
    nodeSetIndex: int
    _meFadeState: ctypes.c_int32
    _meFadeType: ctypes.c_int32

cGcFadeNodeBase._fields_ = [
    ("__vftable", ctypes.POINTER(cGcFadeNodeBase_vtbl)),
    ("timer", ctypes.c_float),
    ("totalTime", ctypes.c_float),
    ("nodeParam", ctypes.c_int32),
    ("nodeSetIndex", ctypes.c_int32),
    ("_meFadeState", ctypes.c_int32),
    ("_meFadeType", ctypes.c_int32),
]


class cGcFadeNode(cGcFadeNodeBase, ctypes.Structure):
    node: common.TkHandle

cGcFadeNode._fields_ = [
    ("node", common.TkHandle),
]


class TkJobHandle(ctypes.Structure):
    queue: int
    index: int
    count: int

TkJobHandle._fields_ = [
    ("queue", ctypes.c_int32),
    ("index", ctypes.c_int32),
    ("count", ctypes.c_uint64),
]


class cGcRegionBase(cTkRegion, ctypes.Structure):
    class cGcUnmapStreamData(ctypes.Structure):
        token: "TkJobHandle"
        node: common.TkHandle
        resource: common.cTkSmartResHandle
        tileBlendStart: int
        valid: bool

    cGcUnmapStreamData._fields_ = [
        ("token", TkJobHandle),
        ("node", common.TkHandle),
        ("resource", common.cTkSmartResHandle),
        ("tileBlendStart", ctypes.c_int32),
        ("valid", ctypes.c_ubyte),
    ]


    unmapStreamData: bytes

cGcRegionBase._fields_ = [
    ("unmapStreamData", ctypes.c_ubyte * 0xA0),
]


class cTkBasicNoiseHelper(ctypes.Structure):
    class NoisePositionData(ctypes.Structure):
        position: common.Vector3f
        normal: common.Vector3f
        _mVoxelType: ctypes.c_int32

    NoisePositionData._fields_ = [
        ("position", common.Vector3f),
        ("normal", common.Vector3f),
        ("_mVoxelType", ctypes.c_int32),
    ]


    class NoisePositionOutput(ctypes.Structure):
        _meCurrentType: ctypes.c_int32
        resources: std.vector[cTkBasicNoiseHelper.NoisePositionData]

    NoisePositionOutput._fields_ = [
        ("_meCurrentType", ctypes.c_int32),
        ("padding0x4", ctypes.c_ubyte * 0x4),
        ("resources", std.vector[NoisePositionData]),
    ]



cTkBasicNoiseHelper._fields_ = []


class cGcRegionTerrain(cGcRegionBase, ctypes.Structure):
    _mePolygoniser: ctypes.c_int32
    mappedStreamTerrain: _Pointer["cTkTerrainVertexData"]
    needsOverflowStream: bool
    deferEditsGeneration: bool
    numTerrainVerts: int
    distance: int
    parentDistance: int
    angle: float
    terrainMaterial: common.cTkSmartResHandle
    waterMaterial: common.cTkSmartResHandle
    boundingBox: "common.cTkAABB"
    parent: _Pointer["cGcRegionTerrain"]
    children: bytes
    maxHeights: None
    elevation: None
    fade: "cGcFadeNode"
    lod: int
    tileBlendStart: int
    resourcePositions: std.vector[cTkBasicNoiseHelper.NoisePositionData]
    absolutePosition: common.Vector3f

cGcRegionTerrain._fields_ = [
    ("_mePolygoniser", ctypes.c_int32),
    ("padding0x174", ctypes.c_ubyte * 0x4),
    ("mappedStreamTerrain", ctypes.POINTER(cTkTerrainVertexData)),
    ("needsOverflowStream", ctypes.c_ubyte),
    ("deferEditsGeneration", ctypes.c_ubyte),
    ("padding0x182", ctypes.c_ubyte * 0x2),
    ("numTerrainVerts", ctypes.c_int32),
    ("distance", ctypes.c_int32),
    ("parentDistance", ctypes.c_int32),
    ("angle", ctypes.c_float),
    ("terrainMaterial", common.cTkSmartResHandle),
    ("waterMaterial", common.cTkSmartResHandle),
    ("padding0x19C", ctypes.c_ubyte * 0x4),
    ("boundingBox", common.cTkAABB),
    ("parent", ctypes.POINTER(cGcRegionTerrain)),
    ("children", ctypes.c_ubyte * 0x40),
    ("maxHeights", ctypes.POINTER(ctypes.c_float)),
    ("elevation", ctypes.POINTER(ctypes.c_float)),
    ("fade", cGcFadeNode),
    ("lod", ctypes.c_int32),
    ("tileBlendStart", ctypes.c_int32),
    ("resourcePositions", std.vector[cTkBasicNoiseHelper.NoisePositionData]),
    ("absolutePosition", common.Vector3f),
]


class cGcTerrainRegionMap(cTkRegionMapBase, ctypes.Structure):
    class cTkRegionStub(ctypes.Structure):
        position: common.Vector3f
        parentPosition: common.Vector3f
        region: bytes
        active: bool
        fastTreeIdx: int
        parentFastTreeIdx: int

    cTkRegionStub._fields_ = [
        ("position", common.Vector3f),
        ("parentPosition", common.Vector3f),
        ("region", ctypes.c_ubyte * 0x8),
        ("active", ctypes.c_ubyte),
        ("padding0x29", ctypes.c_ubyte * 0x3),
        ("fastTreeIdx", ctypes.c_uint32),
        ("parentFastTreeIdx", ctypes.c_uint32),
    ]


    class AreChildrenRenderableJob(ctypes.Structure):
        regionMap: _Pointer["cGcTerrainRegionMap"]
        lod: int
        startIndex: int
        endIndex: int
        outResults: None
        complete: ctypes.c_int32
        kicked: bool

    AreChildrenRenderableJob._fields_ = [
        ("regionMap", ctypes.c_ubyte * 0x8),
        ("lod", ctypes.c_int32),
        ("startIndex", ctypes.c_int32),
        ("endIndex", ctypes.c_int32),
        ("padding0x14", ctypes.c_ubyte * 0x4),
        ("outResults", ctypes.POINTER(ctypes.c_uint8)),
        ("complete", ctypes.c_int32),
        ("kicked", ctypes.c_ubyte),
    ]


    class AreSiblingsRenderableJob(ctypes.Structure):
        regionMap: _Pointer["cGcTerrainRegionMap"]
        lod: int
        startIndex: int
        endIndex: int
        furthestActiveLod: int
        outResults: None
        complete: ctypes.c_int32
        kicked: bool

    AreSiblingsRenderableJob._fields_ = [
        ("regionMap", ctypes.c_ubyte * 0x8),
        ("lod", ctypes.c_int32),
        ("startIndex", ctypes.c_int32),
        ("endIndex", ctypes.c_int32),
        ("furthestActiveLod", ctypes.c_int32),
        ("outResults", ctypes.POINTER(ctypes.c_uint8)),
        ("complete", ctypes.c_int32),
        ("kicked", ctypes.c_ubyte),
    ]


    borderRegions: int
    octreeDiameter: int
    centrePosX: int
    centrePosY: int
    centrePosZ: int
    exactCentre: common.Vector3f
    cachedRadius: float
    minDistance: int
    totalSize: int
    regionListDirty: bool
    numGeneratorCallsPerFrame: None
    numPolygoniseCallsPerFrame: None
    numPostPolygoniseCallsPerFrame: None
    regionPools: bytes
    prevStubs: bytes
    activeRegions: bytes
    rootNode: common.TkHandle
    fastRegionTree: "cGcTerrainRegionMapOcttree"
    generatorData: bytes
    buildingData: bytes
    matrix: common.cTkMatrix34
    toCamera: common.Vector3f
    lODGroups: bytes
    isLodVisible: bytes
    isLodAABBVisible: bytes
    isLodActive: bytes
    numRegions: bytes
    regionArrays: bytes
    lodOrder: bytes
    numVoxelsX: bytes
    numVoxelsY: bytes
    numVoxelsZ: bytes
    childrenRenderableJobs: bytes
    siblingsRenderableJobs: bytes
    objectsUpgradeList: bytes
    rigidBodyRefreshList: bytes
    buildingsUpgradeList: bytes
    hide: bool
    name: common.cTkFixedString[0x40]
    regionGeneratesInFlight: int
    regionStreamsMapped: int
    regionsWaitingToPostPolygonise: int
    regionsWaitingToPopulate: int
    regionsPostPolygonisedThisFrame: int
    regionsPopulatedThisFrame: int
    regionBuildsInFlight: int
    timeSpentPostPolygonisingThisFrame: float
    timeSpentPopulatingThisFrame: float

cGcTerrainRegionMap._fields_ = [
    ("borderRegions", ctypes.c_int32),
    ("octreeDiameter", ctypes.c_int32),
    ("centrePosX", ctypes.c_int32),
    ("centrePosY", ctypes.c_int32),
    ("centrePosZ", ctypes.c_int32),
    ("padding0x1C", ctypes.c_ubyte * 0x4),
    ("exactCentre", common.Vector3f),
    ("cachedRadius", ctypes.c_float),
    ("minDistance", ctypes.c_int32),
    ("totalSize", ctypes.c_int32),
    ("regionListDirty", ctypes.c_ubyte),
    ("padding0x3D", ctypes.c_ubyte * 0x3),
    ("numGeneratorCallsPerFrame", ctypes.POINTER(ctypes.c_int32)),
    ("numPolygoniseCallsPerFrame", ctypes.POINTER(ctypes.c_int32)),
    ("numPostPolygoniseCallsPerFrame", ctypes.POINTER(ctypes.c_int32)),
    ("regionPools", std.array[std.array[ctypes.POINTER(cGcRegionTerrain), 1500], 6]),
    ("padding0x11998", ctypes.c_ubyte * 0x8),
    ("prevStubs", ctypes.c_ubyte * 0x8CA00),
    ("activeRegions", ctypes.c_ubyte * 0x468),
    ("rootNode", common.TkHandle),
    ("padding0x9E80C", ctypes.c_ubyte * 0x4),
    ("fastRegionTree", cGcTerrainRegionMapOcttree),
    ("generatorData", ctypes.c_ubyte * 0x8),
    ("buildingData", ctypes.c_ubyte * 0x8),
    ("matrix", common.cTkMatrix34),
    ("toCamera", common.Vector3f),
    ("lODGroups", ctypes.c_ubyte * 0x18),
    ("isLodVisible", ctypes.c_ubyte * 0x6),
    ("isLodAABBVisible", ctypes.c_ubyte * 0x6),
    ("isLodActive", ctypes.c_ubyte * 0x6),
    ("padding0xD350A", ctypes.c_ubyte * 0x2),
    ("numRegions", ctypes.c_ubyte * 0x18),
    ("padding0xD3524", ctypes.c_ubyte * 0x4),
    ("regionArrays", ctypes.c_ubyte * 0x30),
    ("lodOrder", ctypes.c_ubyte * 0x18),
    ("numVoxelsX", ctypes.c_ubyte * 0x18),
    ("numVoxelsY", ctypes.c_ubyte * 0x18),
    ("numVoxelsZ", ctypes.c_ubyte * 0x18),
    ("childrenRenderableJobs", ctypes.c_ubyte * 0xF0),
    ("siblingsRenderableJobs", ctypes.c_ubyte * 0xF0),
    ("objectsUpgradeList", ctypes.c_ubyte * 0x18),
    ("rigidBodyRefreshList", ctypes.c_ubyte * 0x18),
    ("buildingsUpgradeList", ctypes.c_ubyte * 0x18),
    ("hide", ctypes.c_ubyte),
    ("name", common.cTkFixedString[0x40]),
    ("padding0xD3821", ctypes.c_ubyte * 0x3),
    ("regionGeneratesInFlight", ctypes.c_int32),
    ("regionStreamsMapped", ctypes.c_int32),
    ("regionsWaitingToPostPolygonise", ctypes.c_int32),
    ("regionsWaitingToPopulate", ctypes.c_int32),
    ("regionsPostPolygonisedThisFrame", ctypes.c_int32),
    ("regionsPopulatedThisFrame", ctypes.c_int32),
    ("regionBuildsInFlight", ctypes.c_int32),
    ("timeSpentPostPolygonisingThisFrame", ctypes.c_double),
    ("timeSpentPopulatingThisFrame", ctypes.c_double),
]


class cGcEnvironmentProperties(ctypes.Structure):
    flightFogHeight: float
    flightFogBlend: float
    cloudHeightMin: float
    cloudHeightMax: float
    heavyAirHeightMin: float
    heavyAirHeightMax: float
    planetObjectSwitch: float
    planetLodSwitch0: float
    planetLodSwitch0Elevation: float
    planetLodSwitch1: float
    planetLodSwitch2: float
    planetLodSwitch3: float
    asteroidFadeHeightMin: float
    asteroidFadeHeightMax: float
    skyHeight: list[float]
    skyAtmosphereHeight: float
    horizonBlendHeight: float
    horizonBlendLength: float
    skyColourHeight: float
    skyColourBlendLength: float
    skyPositionHeight: float
    skyPositionBlendLength: float
    solarSystemLUTHeight: float
    solarSystemLUTBlendLength: float
    atmosphereStartHeight: float
    atmosphereEndHeight: float
    stratosphereHeight: float

cGcEnvironmentProperties._fields_ = [
    ("flightFogHeight", ctypes.c_float),
    ("flightFogBlend", ctypes.c_float),
    ("cloudHeightMin", ctypes.c_float),
    ("cloudHeightMax", ctypes.c_float),
    ("heavyAirHeightMin", ctypes.c_float),
    ("heavyAirHeightMax", ctypes.c_float),
    ("planetObjectSwitch", ctypes.c_float),
    ("planetLodSwitch0", ctypes.c_float),
    ("planetLodSwitch0Elevation", ctypes.c_float),
    ("planetLodSwitch1", ctypes.c_float),
    ("planetLodSwitch2", ctypes.c_float),
    ("planetLodSwitch3", ctypes.c_float),
    ("asteroidFadeHeightMin", ctypes.c_float),
    ("asteroidFadeHeightMax", ctypes.c_float),
    ("skyHeight", ctypes.c_float * 0x4),
    ("skyAtmosphereHeight", ctypes.c_float),
    ("horizonBlendHeight", ctypes.c_float),
    ("horizonBlendLength", ctypes.c_float),
    ("skyColourHeight", ctypes.c_float),
    ("skyColourBlendLength", ctypes.c_float),
    ("skyPositionHeight", ctypes.c_float),
    ("skyPositionBlendLength", ctypes.c_float),
    ("solarSystemLUTHeight", ctypes.c_float),
    ("solarSystemLUTBlendLength", ctypes.c_float),
    ("atmosphereStartHeight", ctypes.c_float),
    ("atmosphereEndHeight", ctypes.c_float),
    ("stratosphereHeight", ctypes.c_float),
]


class cGcPlanet(ctypes.Structure):
    class sSentinelCrimeResponse(ctypes.Structure):
        _meCrimeResponse: ctypes.c_int32
        crimeResponseResetTime: float
        sentinelIgnoreCrimeStartTime: float

    sSentinelCrimeResponse._fields_ = [
        ("_meCrimeResponse", ctypes.c_int32),
        ("crimeResponseResetTime", ctypes.c_float),
        ("sentinelIgnoreCrimeStartTime", ctypes.c_float),
    ]


    class sStorm(ctypes.Structure):
        stormStartTime: int
        stormSeed: int
        gravityMultiplier: common.TkSmoothCD[ctypes.c_float]
        targetGravityMultiplier: float
        stormStrength: common.TkSmoothCD[ctypes.c_float]
        stormIndex: int

    sStorm._fields_ = [
        ("stormStartTime", ctypes.c_uint64),
        ("stormSeed", ctypes.c_uint64),
        ("gravityMultiplier", common.TkSmoothCD[ctypes.c_float]),
        ("targetGravityMultiplier", ctypes.c_float),
        ("stormStrength", common.TkSmoothCD[ctypes.c_float]),
        ("stormIndex", ctypes.c_int32),
    ]


    class sClouds(ctypes.Structure):
        cloudCover: common.TkSmoothCD[ctypes.c_float]
        cloudRatio: common.TkSmoothCD[ctypes.c_float]
        stormCloudStrength: common.TkSmoothCD[ctypes.c_float]
        instantCloudsUpdate: bool

    sClouds._fields_ = [
        ("cloudCover", common.TkSmoothCD[ctypes.c_float]),
        ("cloudRatio", common.TkSmoothCD[ctypes.c_float]),
        ("stormCloudStrength", common.TkSmoothCD[ctypes.c_float]),
        ("instantCloudsUpdate", ctypes.c_ubyte),
    ]


    class cGcLocalPaletteTexture(ctypes.Structure):
        _mePalette: ctypes.c_int32
        _meColourAlt: ctypes.c_int32

    cGcLocalPaletteTexture._fields_ = [
        ("_mePalette", ctypes.c_int32),
        ("_meColourAlt", ctypes.c_int32),
    ]


    activePrimaryRegionStates: bytes
    planetDiscoveryData: bytes
    beaconUpdateIndex: int
    planetIndex: int
    planetData: "cGcPlanetData"
    planetGenerationInputData: cGcPlanetGenerationInputData
    planetControls: bytes
    buildings: bytes
    spawnData: bytes
    shipStartBuildingSeed: common.GcSeed
    survivalStartBuildingSeed: common.GcSeed
    isPrimary: bool
    primarySwitched: bool
    finishedGenerating: bool
    isScanned: bool
    sentinelCrimeResponse: "cGcPlanet.sSentinelCrimeResponse"
    regionMap: cGcTerrainRegionMap
    regionNode: common.TkHandle
    regionRadiusSet: int
    node: common.TkHandle
    atmosphereNode: common.TkHandle
    planetMeshNode: common.TkHandle
    ringNode: common.TkHandle
    position: common.Vector3f
    lodSphere: bytes
    waterCollision: bytes
    waterRigidBody: bytes
    terrainMaterial: common.cTkSmartResHandle
    waterMaterial: common.cTkSmartResHandle
    atmosphereMaterial: common.cTkSmartResHandle
    terrainDiffuseRes: common.cTkSmartResHandle
    terrainNormalMapRes: common.cTkSmartResHandle
    overlayDiffuseRes: common.cTkSmartResHandle
    overlayNormalRes: common.cTkSmartResHandle
    overlayMasksRes: common.cTkSmartResHandle
    waterHeavyAirRes: common.cTkSmartResHandle
    weatherHeavyAirRes: common.cTkSmartResHandle
    ringMaterial: common.cTkSmartResHandle
    vertexNodePropertyIndex: int
    useSpaceAtmosphere: bool
    indoorLightingBlend: float
    indoorFogStrength: float
    ringAvoidanceSphereInterpolate: float
    ringAvoidanceSphereRadius: float
    ringAvoidanceSpherePosition: common.Vector3f
    averageColour: bytes
    specularValue: bytes
    filename: common.cTkFixedString[0x100]
    metadataRegistered: bool
    hasRegionData: bool
    pendingCopyRegionVoxelData: bool
    paused: bool
    planetSceneNode: common.TkHandle
    _meTransitionState: ctypes.c_int32
    isGeneratingDuringLoad: bool
    cachedTerrainMaterialPtr: int
    cachedWaterMaterialPtr: int
    cachedAtmosphereMaterial: int
    cachedRingMaterial: int
    storm: "cGcPlanet.sStorm"
    clouds: "cGcPlanet.sClouds"
    portalStartSeed: common.GcSeed
    resourceLoadingRequests: bytes
    loadBalancingTimer: bytes
    planetUniformsJobHandle: bytes
    envProperties: _Pointer["cGcEnvironmentProperties"]
    skyProperties: bytes

cGcPlanet._fields_ = [
    ("activePrimaryRegionStates", ctypes.c_ubyte * 0x7),
    ("padding0x7", ctypes.c_ubyte * 0x1),
    ("planetDiscoveryData", ctypes.c_ubyte * 72),
    ("beaconUpdateIndex", ctypes.c_uint64),
    ("planetIndex", ctypes.c_int32),
    ("padding0x5C", ctypes.c_ubyte * 0x4),
    ("planetData", cGcPlanetData),
    ("planetGenerationInputData", cGcPlanetGenerationInputData),
    ("planetControls", ctypes.c_ubyte * 0x8),
    ("padding0x3F58", ctypes.c_ubyte * 0x8),
    ("buildings", ctypes.c_ubyte * 96),
    ("spawnData", ctypes.c_ubyte * 104),
    ("shipStartBuildingSeed", common.GcSeed),
    ("survivalStartBuildingSeed", common.GcSeed),
    ("isPrimary", ctypes.c_ubyte),
    ("primarySwitched", ctypes.c_ubyte),
    ("finishedGenerating", ctypes.c_ubyte),
    ("isScanned", ctypes.c_ubyte),
    ("sentinelCrimeResponse", cGcPlanet.sSentinelCrimeResponse),
    ("padding0x4058", ctypes.c_ubyte * 0x8),
    ("regionMap", cGcTerrainRegionMap),
    ("regionNode", common.TkHandle),
    ("regionRadiusSet", ctypes.c_int32),
    ("node", common.TkHandle),
    ("atmosphereNode", common.TkHandle),
    ("planetMeshNode", common.TkHandle),
    ("ringNode", common.TkHandle),
    ("padding0xD78C8", ctypes.c_ubyte * 0x8),
    ("position", common.Vector3f),
    ("lodSphere", ctypes.c_ubyte * 6256),
    ("waterCollision", ctypes.c_ubyte * 0x8),
    ("waterRigidBody", ctypes.c_ubyte * 0x8),
    ("terrainMaterial", common.cTkSmartResHandle),
    ("waterMaterial", common.cTkSmartResHandle),
    ("atmosphereMaterial", common.cTkSmartResHandle),
    ("terrainDiffuseRes", common.cTkSmartResHandle),
    ("terrainNormalMapRes", common.cTkSmartResHandle),
    ("overlayDiffuseRes", common.cTkSmartResHandle),
    ("overlayNormalRes", common.cTkSmartResHandle),
    ("overlayMasksRes", common.cTkSmartResHandle),
    ("waterHeavyAirRes", common.cTkSmartResHandle),
    ("weatherHeavyAirRes", common.cTkSmartResHandle),
    ("ringMaterial", common.cTkSmartResHandle),
    ("vertexNodePropertyIndex", ctypes.c_int32),
    ("useSpaceAtmosphere", ctypes.c_ubyte),
    ("padding0xD9191", ctypes.c_ubyte * 0x3),
    ("indoorLightingBlend", ctypes.c_float),
    ("indoorFogStrength", ctypes.c_float),
    ("ringAvoidanceSphereInterpolate", ctypes.c_float),
    ("ringAvoidanceSphereRadius", ctypes.c_float),
    ("padding0xD91A4", ctypes.c_ubyte * 0xC),
    ("ringAvoidanceSpherePosition", common.Vector3f),
    ("averageColour", ctypes.c_ubyte * 0x170),
    ("specularValue", ctypes.c_ubyte * 0x68),
    ("filename", common.cTkFixedString[0x100]),
    ("metadataRegistered", ctypes.c_ubyte),
    ("hasRegionData", ctypes.c_ubyte),
    ("pendingCopyRegionVoxelData", ctypes.c_ubyte),
    ("paused", ctypes.c_ubyte),
    ("planetSceneNode", common.TkHandle),
    ("_meTransitionState", ctypes.c_int32),
    ("isGeneratingDuringLoad", ctypes.c_ubyte),
    ("padding0xD94A5", ctypes.c_ubyte * 0x3),
    ("cachedTerrainMaterialPtr", ctypes.c_void_p),
    ("cachedWaterMaterialPtr", ctypes.c_void_p),
    ("cachedAtmosphereMaterial", ctypes.c_void_p),
    ("cachedRingMaterial", ctypes.c_void_p),
    ("storm", cGcPlanet.sStorm),
    ("clouds", cGcPlanet.sClouds),
    ("padding0xD950C", ctypes.c_ubyte * 0x4),
    ("portalStartSeed", common.GcSeed),
    ("resourceLoadingRequests", ctypes.c_ubyte * 0x8),
    ("loadBalancingTimer", ctypes.c_ubyte * 0x8),
    ("planetUniformsJobHandle", ctypes.c_ubyte * 0x10),
    ("envProperties", ctypes.POINTER(cGcEnvironmentProperties)),
    ("skyProperties", ctypes.c_ubyte * 0x8),
]


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


class cTkCurveType(ctypes.Structure):
    _meCurve: int
    @property
    def curve(self):
        return safe_assign_enum(nms_enums.eCurve, self._meCurve)

cTkCurveType._fields_ = [
    ("_meCurve", ctypes.c_int8),
]


class cGcHUD(ctypes.Structure):
    uIMaterial: common.cTkSmartResHandle
    layers: bytes
    numLayers: int
    images: bytes
    numImages: int
    texts: bytes
    numTexts: int

cGcHUD._fields_ = [
    ("uIMaterial", common.cTkSmartResHandle),
    ("padding0x4", ctypes.c_ubyte * 0xC),
    ("layers", ctypes.c_ubyte * 0x5800),
    ("numLayers", ctypes.c_int32),
    ("padding0x5814", ctypes.c_ubyte * 0xC),
    ("images", ctypes.c_ubyte * 0x6800),
    ("numImages", ctypes.c_int32),
    ("padding0xC024", ctypes.c_ubyte * 0xC),
    ("texts", ctypes.c_ubyte * 0x14000),
    ("numTexts", ctypes.c_int32),
    ("padding0x20030", ctypes.c_ubyte * 0xC),
]


class ITkNGuiDraggable_vtbl(ctypes.Structure):
    Render: bytes
    GetType: bytes

ITkNGuiDraggable_vtbl._fields_ = [
    ("Render", ctypes.c_ubyte * 0x8),
    ("GetType", ctypes.c_ubyte * 0x8),
]


class ITkNGuiDraggable(ctypes.Structure):
    __vftable: _Pointer["ITkNGuiDraggable_vtbl"]

ITkNGuiDraggable._fields_ = [
    ("__vftable", ctypes.POINTER(ITkNGuiDraggable_vtbl)),
]


class cGcVROverride_Layout(ctypes.Structure):
    _meVROverride_Layout: ctypes.c_int32
    floatValue: float

cGcVROverride_Layout._fields_ = [
    ("_meVROverride_Layout", ctypes.c_int32),
    ("floatValue", ctypes.c_float),
]


class cGcAccessibleOverride_Layout(ctypes.Structure):
    _meAccessibleOverride_Layout: ctypes.c_int32
    floatValue: float

cGcAccessibleOverride_Layout._fields_ = [
    ("_meAccessibleOverride_Layout", ctypes.c_int32),
    ("floatValue", ctypes.c_float),
]


class cTkNGuiAlignment(ctypes.Structure):
    _meVertical: int
    _meHorizontal: int

cTkNGuiAlignment._fields_ = [
    ("_meVertical", ctypes.c_int8),
    ("_meHorizontal", ctypes.c_int8),
]


class cGcNGuiLayoutData(ctypes.Structure):
    vROverrides: common.cTkDynamicArray[cGcVROverride_Layout]
    accessibleOverrides: common.cTkDynamicArray[cGcAccessibleOverride_Layout]
    positionX: float
    positionY: float
    width: float
    height: float
    constrainAspect: float
    maxWidth: float
    align: "cTkNGuiAlignment"
    widthPercentage: bool
    heightPercentage: bool
    constrainProportions: bool
    forceAspect: bool
    anchor: bool
    anchorPercent: bool
    sameLine: bool
    slowCursorOnHover: bool

cGcNGuiLayoutData._fields_ = [
    ("vROverrides", common.cTkDynamicArray[cGcVROverride_Layout]),
    ("accessibleOverrides", common.cTkDynamicArray[cGcAccessibleOverride_Layout]),
    ("positionX", ctypes.c_float),
    ("positionY", ctypes.c_float),
    ("width", ctypes.c_float),
    ("height", ctypes.c_float),
    ("constrainAspect", ctypes.c_float),
    ("maxWidth", ctypes.c_float),
    ("align", cTkNGuiAlignment),
    ("widthPercentage", ctypes.c_ubyte),
    ("heightPercentage", ctypes.c_ubyte),
    ("constrainProportions", ctypes.c_ubyte),
    ("forceAspect", ctypes.c_ubyte),
    ("anchor", ctypes.c_ubyte),
    ("anchorPercent", ctypes.c_ubyte),
    ("sameLine", ctypes.c_ubyte),
    ("slowCursorOnHover", ctypes.c_ubyte),
]


class cTkNGuiForcedStyle(ctypes.Structure):
    _meNGuiForcedStyle: int
    @property
    def nGuiForcedStyle(self):
        return safe_assign_enum(nms_enums.eNGuiForcedStyle, self._meNGuiForcedStyle)

cTkNGuiForcedStyle._fields_ = [
    ("_meNGuiForcedStyle", ctypes.c_int32),
]


class cGcNGuiElementData(ctypes.Structure):
    ID: common.TkID[0x10]
    presetID: common.TkID[0x10]
    isHidden: bool
    forcedStyle: "cTkNGuiForcedStyle"
    layout: "cGcNGuiLayoutData"

cGcNGuiElementData._fields_ = [
    ("ID", common.TkID[0x10]),
    ("presetID", common.TkID[0x10]),
    ("isHidden", ctypes.c_ubyte),
    ("padding0x21", ctypes.c_ubyte * 0x3),
    ("forcedStyle", cTkNGuiForcedStyle),
    ("layout", cGcNGuiLayoutData),
]


class cGcNGuiElement(ITkNGuiDraggable, ctypes.Structure):
    class sGcNGuiElementAnimSettings(ctypes.Structure):
        _bf_0: int

    sGcNGuiElementAnimSettings._fields_ = [
        ("_bf_0", ctypes.c_int8),
    ]

    contentBBox: "common.cTkBBox2d"
    parallaxOffset: common.Vector2f
    undoMoveEvent: bytes
    undoResizeEvent: bytes
    undoLayoutEvent: bytes
    parent: _Pointer["cGcNGuiLayer"]
    elementData: _Pointer["cGcNGuiElementData"]
    _meInputThisFrame: int
    _meLayoutChangeEvent: int
    _meRequestAnim: int
    anim: "sGcNGuiElementAnimSettings"


class cTkNGuiGraphicStyleData(ctypes.Structure):
    colour: common.Colour
    iconColour: common.Colour
    strokeColour: common.Colour
    gradientColour: common.Colour
    strokeGradientColour: common.Colour
    paddingX: float
    paddingY: float
    marginX: float
    marginY: float
    gradientStartOffset: float
    gradientEndOffset: float
    cornerRadius: float
    strokeSize: float
    image: int
    icon: int
    desaturation: float
    strokeGradientOffset: float
    strokeGradientFeather: float
    _meShape: int
    _meGradient: int
    solidColour: bool
    hasDropShadow: bool
    hasOuterGradient: bool
    hasInnerGradient: bool
    gradientOffsetPercent: bool
    strokeGradient: bool

cTkNGuiGraphicStyleData._fields_ = [
    ("colour", common.Colour),
    ("iconColour", common.Colour),
    ("strokeColour", common.Colour),
    ("gradientColour", common.Colour),
    ("strokeGradientColour", common.Colour),
    ("paddingX", ctypes.c_float),
    ("paddingY", ctypes.c_float),
    ("marginX", ctypes.c_float),
    ("marginY", ctypes.c_float),
    ("gradientStartOffset", ctypes.c_float),
    ("gradientEndOffset", ctypes.c_float),
    ("cornerRadius", ctypes.c_float),
    ("strokeSize", ctypes.c_float),
    ("image", ctypes.c_int32),
    ("icon", ctypes.c_int32),
    ("desaturation", ctypes.c_float),
    ("strokeGradientOffset", ctypes.c_float),
    ("strokeGradientFeather", ctypes.c_float),
    ("_meShape", ctypes.c_int8),
    ("_meGradient", ctypes.c_int8),
    ("solidColour", ctypes.c_ubyte),
    ("hasDropShadow", ctypes.c_ubyte),
    ("hasOuterGradient", ctypes.c_ubyte),
    ("hasInnerGradient", ctypes.c_ubyte),
    ("gradientOffsetPercent", ctypes.c_ubyte),
    ("strokeGradient", ctypes.c_ubyte),
    ("padding0x8C", ctypes.c_ubyte * 0x4),
]


class cTkNGuiGraphicStyle(ctypes.Structure):
    default: "cTkNGuiGraphicStyleData"
    highlight: "cTkNGuiGraphicStyleData"
    active: "cTkNGuiGraphicStyleData"
    customMinStart: common.Vector2f
    customMaxStart: common.Vector2f
    highlightTime: float
    highlightScale: float
    globalFade: float
    animTime: float
    animSplit: float
    animCurve1: "cTkCurveType"
    animCurve2: "cTkCurveType"
    _meAnimate: int
    inheritStyleFromParentLayer: bool

cTkNGuiGraphicStyle._fields_ = [
    ("default", cTkNGuiGraphicStyleData),
    ("highlight", cTkNGuiGraphicStyleData),
    ("active", cTkNGuiGraphicStyleData),
    ("customMinStart", common.Vector2f),
    ("customMaxStart", common.Vector2f),
    ("highlightTime", ctypes.c_float),
    ("highlightScale", ctypes.c_float),
    ("globalFade", ctypes.c_float),
    ("animTime", ctypes.c_float),
    ("animSplit", ctypes.c_float),
    ("animCurve1", cTkCurveType),
    ("animCurve2", cTkCurveType),
    ("_meAnimate", ctypes.c_int8),
    ("inheritStyleFromParentLayer", ctypes.c_ubyte),
    ("padding0x1D8", ctypes.c_ubyte * 0x8),
]


class cTkNGuiTextStyleData(ctypes.Structure):
    colour: common.Colour
    shadowColour: common.Colour
    outlineColour: common.Colour
    fontHeight: float
    fontSpacing: float
    dropShadowAngle: float
    dropShadowOffset: float
    outlineSize: float
    fontIndex: int
    align: "cTkNGuiAlignment"
    isIndented: bool
    hasDropShadow: bool
    hasOutline: bool
    isParagraph: bool
    allowScroll: bool
    forceUpperCase: bool
    autoAdjustHeight: bool
    autoAdjustFontHeight: bool
    blockAudio: bool

cTkNGuiTextStyleData._fields_ = [
    ("colour", common.Colour),
    ("shadowColour", common.Colour),
    ("outlineColour", common.Colour),
    ("fontHeight", ctypes.c_float),
    ("fontSpacing", ctypes.c_float),
    ("dropShadowAngle", ctypes.c_float),
    ("dropShadowOffset", ctypes.c_float),
    ("outlineSize", ctypes.c_float),
    ("fontIndex", ctypes.c_int32),
    ("align", cTkNGuiAlignment),
    ("isIndented", ctypes.c_ubyte),
    ("hasDropShadow", ctypes.c_ubyte),
    ("hasOutline", ctypes.c_ubyte),
    ("isParagraph", ctypes.c_ubyte),
    ("allowScroll", ctypes.c_ubyte),
    ("forceUpperCase", ctypes.c_ubyte),
    ("autoAdjustHeight", ctypes.c_ubyte),
    ("autoAdjustFontHeight", ctypes.c_ubyte),
    ("blockAudio", ctypes.c_ubyte),
    ("padding0x53", ctypes.c_ubyte * 0xD),
]


class cTkNGuiTextStyle(ctypes.Structure):
    default: "cTkNGuiTextStyleData"
    highlight: "cTkNGuiTextStyleData"
    active: "cTkNGuiTextStyleData"

cTkNGuiTextStyle._fields_ = [
    ("default", cTkNGuiTextStyleData),
    ("highlight", cTkNGuiTextStyleData),
    ("active", cTkNGuiTextStyleData),
]


class cGcVROverride_Text(ctypes.Structure):
    _meVROverride_Text: ctypes.c_int32
    intValue: int
    floatValue: float

cGcVROverride_Text._fields_ = [
    ("_meVROverride_Text", ctypes.c_int32),
    ("intValue", ctypes.c_int32),
    ("floatValue", ctypes.c_float),
]


class cGcAccessibleOverride_Text(ctypes.Structure):
    _meAccessibleOverride_Text: ctypes.c_int32
    floatValue: float

cGcAccessibleOverride_Text._fields_ = [
    ("_meAccessibleOverride_Text", ctypes.c_int32),
    ("floatValue", ctypes.c_float),
]



class cGcNGuiTextData(ctypes.Structure):
    elementData: "cGcNGuiElementData"
    style: "cTkNGuiTextStyle"
    graphicStyle: "cTkNGuiGraphicStyle"
    text: common.cTkFixedString[0x200]
    image: common.cTkFixedString[0x80]
    forcedOffset: float
    vROverrides: common.cTkDynamicArray[cGcVROverride_Text]
    accessibleOverrides: common.cTkDynamicArray[cGcAccessibleOverride_Text]
    special: bool
    forcedAllowScroll: bool

cGcNGuiTextData._fields_ = [
    ("elementData", cGcNGuiElementData),
    ("style", cTkNGuiTextStyle),
    ("graphicStyle", cTkNGuiGraphicStyle),
    ("text", common.cTkFixedString[0x200]),
    ("image", common.cTkFixedString[0x80]),
    ("forcedOffset", ctypes.c_float),
    ("padding0x5F4", ctypes.c_ubyte * 0x4),
    ("vROverrides", common.cTkDynamicArray[cGcVROverride_Text]),
    ("accessibleOverrides", common.cTkDynamicArray[cGcAccessibleOverride_Text]),
    ("special", ctypes.c_ubyte),
    ("forcedAllowScroll", ctypes.c_ubyte),
]


class cGcNGuiLayerData(ctypes.Structure):
    elementData: "cGcNGuiElementData"
    style: "cTkNGuiGraphicStyle"
    image: common.cTkFixedString[0x80]
    children: common.cTkDynamicArray[common.cTkClassPointer]
    dataFilename: common.cTkFixedString[0x80]
    _meAltMode: ctypes.c_int32

cGcNGuiLayerData._fields_ = [
    ("elementData", cGcNGuiElementData),
    ("style", cTkNGuiGraphicStyle),
    ("image", common.cTkFixedString[0x80]),
    ("children", common.cTkDynamicArray[common.cTkClassPointer]),
    ("dataFilename", common.cTkFixedString[0x80]),
    ("_meAltMode", ctypes.c_int32),
]


class cTkHashedNGuiElement(ctypes.Structure):
    ID: common.TkID[0x10]
    hash: int

cTkHashedNGuiElement._fields_ = [
    ("ID", common.TkID[0x10]),
    ("hash", ctypes.c_uint64),
]


class cGcNGuiText(ctypes.Structure):
    baseclass_0: cGcNGuiElement
    locBlinkText: common.cTkFixedString[0x80]
    previousTextStyle: "cTkNGuiTextStyleData"
    previousGraphicStyle: "cTkNGuiGraphicStyleData"
    textData: _Pointer["cGcNGuiTextData"]
    locTextBlinkBaseTime: int
    _anonymous_ = ("baseclass_0", )


class cGcNGuiLayer(ctypes.Structure):
    baseclass_0: cGcNGuiElement
    elements: std.vector[_Pointer["cGcNGuiElement"]]
    layerElements: std.vector[_Pointer["cGcNGuiLayer"]]
    pinnedPositions: std.vector[common.Vector2f]
    previousGraphicsStyle: "cTkNGuiGraphicStyleData"
    renderFunction: bytes
    renderFunctionData: int
    layerData: _Pointer["cGcNGuiLayerData"]
    elementHashTable: _Pointer[common.cTkLinearHashTable[cTkHashedNGuiElement, _Pointer["cGcNGuiElement"]]]
    uniqueID: int
    expanded: bool
    _anonymous_ = ("baseclass_0", )


cGcNGuiElement._fields_ = [
    ("contentBBox", common.cTkBBox2d),
    ("parallaxOffset", common.Vector2f),
    ("undoMoveEvent", ctypes.c_ubyte * 0x8),
    ("undoResizeEvent", ctypes.c_ubyte * 0x8),
    ("undoLayoutEvent", ctypes.c_ubyte * 0x8),
    ("parent", ctypes.POINTER(cGcNGuiLayer)),
    ("elementData", ctypes.POINTER(cGcNGuiElementData)),
    ("_meInputThisFrame", ctypes.c_int8),
    ("_meLayoutChangeEvent", ctypes.c_int8),
    ("_meRequestAnim", ctypes.c_int8),
    ("anim", cGcNGuiElement.sGcNGuiElementAnimSettings),
    ("padding0x4C", ctypes.c_ubyte * 0x4),
]


cGcNGuiLayer._fields_ = [
    ("baseclass_0", cGcNGuiElement),
    ("elements", std.vector[ctypes.POINTER(cGcNGuiElement)]),
    ("layerElements", std.vector[ctypes.POINTER(cGcNGuiLayer)]),
    ("pinnedPositions", std.vector[common.Vector2f]),
    ("padding0x98", ctypes.c_ubyte * 0x8),
    ("previousGraphicsStyle", cTkNGuiGraphicStyleData),
    ("renderFunction", ctypes.c_ubyte * 0x8),
    ("renderFunctionData", ctypes.c_void_p),
    ("layerData", ctypes.POINTER(cGcNGuiLayerData)),
    ("elementHashTable", ctypes.POINTER(common.cTkLinearHashTable[cTkHashedNGuiElement, ctypes.POINTER(cGcNGuiElement)])),
    ("uniqueID", ctypes.c_uint64),
    ("expanded", ctypes.c_ubyte),
]


cGcNGuiText._fields_ = [
    ("baseclass_0", cGcNGuiElement),
    ("locBlinkText", common.cTkFixedString[0x80]),
    ("previousTextStyle", cTkNGuiTextStyleData),
    ("previousGraphicStyle", cTkNGuiGraphicStyleData),
    ("textData", ctypes.POINTER(cGcNGuiTextData)),
    ("locTextBlinkBaseTime", ctypes.c_uint64),
]


class cTk2dObject_vtbl(ctypes.Structure):
    Construct: bytes
    Prepare: bytes
    Update: bytes
    Render: bytes
    Release: bytes
    Destruct: bytes
    SetPosition: bytes
    GetPosition: bytes
    GetPosition_40: bytes
    GetWorldTopLeft: bytes
    SetSize: bytes
    GetSize: bytes
    SetColour: bytes
    GetColour: bytes
    SetAlignment: bytes
    GetAlignment: bytes
    RemoveAllObjects: bytes

cTk2dObject_vtbl._fields_ = [
    ("Construct", ctypes.c_ubyte * 0x8),
    ("Prepare", ctypes.c_ubyte * 0x8),
    ("Update", ctypes.c_ubyte * 0x8),
    ("Render", ctypes.c_ubyte * 0x8),
    ("Release", ctypes.c_ubyte * 0x8),
    ("Destruct", ctypes.c_ubyte * 0x8),
    ("SetPosition", ctypes.c_ubyte * 0x8),
    ("GetPosition", ctypes.c_ubyte * 0x8),
    ("GetPosition_40", ctypes.c_ubyte * 0x8),
    ("GetWorldTopLeft", ctypes.c_ubyte * 0x8),
    ("SetSize", ctypes.c_ubyte * 0x8),
    ("GetSize", ctypes.c_ubyte * 0x8),
    ("SetColour", ctypes.c_ubyte * 0x8),
    ("GetColour", ctypes.c_ubyte * 0x8),
    ("SetAlignment", ctypes.c_ubyte * 0x8),
    ("GetAlignment", ctypes.c_ubyte * 0x8),
    ("RemoveAllObjects", ctypes.c_ubyte * 0x8),
]


class cTk2dObject(ctypes.Structure):
    __vftable: _Pointer["cTk2dObject_vtbl"]
    colour: common.Colour
    position: common.Vector2f
    size: common.Vector2f
    alignment: common.Vector2f
    nextSibling: _Pointer["cTk2dObject"]

cTk2dObject._fields_ = [
    ("__vftable", ctypes.POINTER(cTk2dObject_vtbl)),
    ("padding0x8", ctypes.c_ubyte * 0x8),
    ("colour", common.Colour),
    ("position", common.Vector2f),
    ("size", common.Vector2f),
    ("alignment", common.Vector2f),
    ("nextSibling", ctypes.POINTER(cTk2dObject)),
]


class cTk2dLayer(cTk2dObject, ctypes.Structure):
    bitArray: common.cTkBitArray[ctypes.c_uint64, 512]
    _meBlendMode: int
    firstChild: _Pointer["cTk2dObject"]
    isVisible: bool
    dynamicSize: bool
    scale: common.Vector2f
    angle: float

cTk2dLayer._fields_ = [
    ("bitArray", common.cTkBitArray[ctypes.c_uint64, 512]),
    ("_meBlendMode", ctypes.c_int8),
    ("padding0x84", ctypes.c_ubyte * 0x4),
    ("firstChild", ctypes.POINTER(cTk2dObject)),
    ("isVisible", ctypes.c_ubyte),
    ("dynamicSize", ctypes.c_ubyte),
    ("padding0x92", ctypes.c_ubyte * 0x2),
    ("scale", common.Vector2f),
    ("angle", ctypes.c_float),
]


class cTk3dLayer(cTk2dLayer, ctypes.Structure):
    worldPosition: common.Vector3f
    screenPosition: common.Vector4f
    screenPositionLeft: common.Vector4f
    screenPositionRight: common.Vector4f
    screenDepth: float
    defaultDistToCamera: float
    minScale: float
    maxScale: float
    _meTestZ: ctypes.c_int32
    enable3d: bool
    scale3d: bool

cTk3dLayer._fields_ = [
    ("worldPosition", common.Vector3f),
    ("screenPosition", common.Vector4f),
    ("screenPositionLeft", common.Vector4f),
    ("screenPositionRight", common.Vector4f),
    ("screenDepth", ctypes.c_float),
    ("defaultDistToCamera", ctypes.c_float),
    ("minScale", ctypes.c_float),
    ("maxScale", ctypes.c_float),
    ("_meTestZ", ctypes.c_int32),
    ("enable3d", ctypes.c_ubyte),
    ("scale3d", ctypes.c_ubyte),
    ("padding0xF6", ctypes.c_ubyte * 0xA)
]


class cTkNGuiInput(ctypes.Structure):
    controlHeld: bool
    shiftHeld: bool
    altHeld: bool
    rightStickX: float
    rightStickY: float
    cursorX: float
    cursorY: float
    cursorDeltaX: float
    cursorDeltaY: float
    cursorSpeedModifierX: float
    cursorSpeedModifierY: float
    mousePosX: float
    mousePosY: float
    mouseScroll: float
    _meMouseButtonState: ctypes.c_int32
    _meMouse2ButtonState: ctypes.c_int32
    _meRightThumbState: ctypes.c_int32
    _meTransferButtonState: ctypes.c_int32
    _meUploadButtonState: ctypes.c_int32
    _meDiscoveryUploadButtonState: ctypes.c_int32
    cursorIsMouse: bool
    padOnly: bool
    elementsPressed: bytes
    elementsPressed2: bytes
    KeyMap: bytes
    KeyCtrl: bool
    KeyShift: bool
    KeyAlt: bool
    keysDown: bytes
    inputCharacters: bytes
    padActive: bool
    dragObject: _Pointer["ITkNGuiDraggable"]

cTkNGuiInput._fields_ = [
    ("controlHeld", ctypes.c_ubyte),
    ("shiftHeld", ctypes.c_ubyte),
    ("altHeld", ctypes.c_ubyte),
    ("padding0x3", ctypes.c_ubyte * 0x1),
    ("rightStickX", ctypes.c_float),
    ("rightStickY", ctypes.c_float),
    ("cursorX", ctypes.c_float),
    ("cursorY", ctypes.c_float),
    ("cursorDeltaX", ctypes.c_float),
    ("cursorDeltaY", ctypes.c_float),
    ("cursorSpeedModifierX", ctypes.c_float),
    ("cursorSpeedModifierY", ctypes.c_float),
    ("mousePosX", ctypes.c_float),
    ("mousePosY", ctypes.c_float),
    ("mouseScroll", ctypes.c_float),
    ("_meMouseButtonState", ctypes.c_int32),
    ("_meMouse2ButtonState", ctypes.c_int32),
    ("_meRightThumbState", ctypes.c_int32),
    ("_meTransferButtonState", ctypes.c_int32),
    ("_meUploadButtonState", ctypes.c_int32),
    ("_meDiscoveryUploadButtonState", ctypes.c_int32),
    ("cursorIsMouse", ctypes.c_ubyte),
    ("padOnly", ctypes.c_ubyte),
    ("padding0x4A", ctypes.c_ubyte * 0x6),
    ("elementsPressed", ctypes.c_ubyte * 0x18),
    ("elementsPressed2", ctypes.c_ubyte * 0x18),
    ("KeyMap", ctypes.c_ubyte * 0x4C),
    ("KeyCtrl", ctypes.c_ubyte),
    ("KeyShift", ctypes.c_ubyte),
    ("KeyAlt", ctypes.c_ubyte),
    ("keysDown", ctypes.c_ubyte * 0x200),
    ("inputCharacters", ctypes.c_ubyte * 0x11),
    ("padActive", ctypes.c_ubyte),
    ("padding0x2E1", ctypes.c_ubyte * 0x7),
    ("dragObject", ctypes.POINTER(ITkNGuiDraggable)),
]


class cTkTextureBase(ctypes.Structure):
    _meType: int
    format: bytes
    _meTextureAddressMode: int
    _meTextureFilterMode: int
    _meTextureReductionMode: int
    isSRGB: bool
    isShadowMap: bool
    width: int
    height: int
    depth: int
    numMips: int
    anisotropy: int
    dataSize: int
    memorySize: int
    mipStatsCounterIndex: bytes
    finestResidentPixelCount: int
    finestMipVisible: int
    numClampedPixels: int
    lastFetchedFrame: int
    fileStartOffset: int
    streamFuncs: bytes
    streamFuncContext: int
    mipZeroSize: int
    evictedSize: int
    evictableMips: int
    evictedMips: int
    allocatedFromStreamingStore: bool
    allocatedWithMipBias: bool
    evictionCountdown: int

cTkTextureBase._fields_ = [
    ("_meType", ctypes.c_int8),
    ("format", ctypes.c_ubyte * 0x1),
    ("padding0x2", ctypes.c_ubyte * 0x2),
    ("_meTextureAddressMode", ctypes.c_int32),
    ("_meTextureFilterMode", ctypes.c_int32),
    ("_meTextureReductionMode", ctypes.c_int8),
    ("isSRGB", ctypes.c_ubyte),
    ("isShadowMap", ctypes.c_ubyte),
    ("padding0xF", ctypes.c_ubyte * 0x1),
    ("width", ctypes.c_int32),
    ("height", ctypes.c_int32),
    ("depth", ctypes.c_int32),
    ("numMips", ctypes.c_int16),
    ("anisotropy", ctypes.c_int16),
    ("dataSize", ctypes.c_int32),
    ("memorySize", ctypes.c_int32),
    ("mipStatsCounterIndex", ctypes.c_ubyte * 0x8),
    ("finestResidentPixelCount", ctypes.c_int32),
    ("finestMipVisible", ctypes.c_int32),
    ("numClampedPixels", ctypes.c_int32),
    ("lastFetchedFrame", ctypes.c_int32),
    ("fileStartOffset", ctypes.c_int32),
    ("padding0x44", ctypes.c_ubyte * 0x4),
    ("streamFuncs", ctypes.c_ubyte * 0x8),
    ("streamFuncContext", ctypes.c_void_p),
    ("mipZeroSize", ctypes.c_int32),
    ("evictedSize", ctypes.c_int32),
    ("evictableMips", ctypes.c_int16),
    ("evictedMips", ctypes.c_int16),
    ("allocatedFromStreamingStore", ctypes.c_ubyte),
    ("allocatedWithMipBias", ctypes.c_ubyte),
    ("evictionCountdown", ctypes.c_uint8),
]


class cTkTexture(cTkTextureBase, ctypes.Structure):
    textureData: int
    texture: bytes
    imageDesc: bytes
    textureMemory: bytes
    textureSrvMips: bytes
    resourceState: bytes
    depthOnly: bool
    textureSrv: bytes
    textureUav: bytes
    sampler: bytes
    lodClamp: float
    mapping: None
    evictableMipPageCount: bytes
    mipStartPage: bytes
    tailOffset: int
    tailArrayStride: int
    ultraMips: int
    detailableMips: int
    lodBias: float
    numPages: int
    evictedPages: int
    mipZeroPages: int
    mipZeroUnusedPages: int
    isPartiallyResident: bool

cTkTexture._fields_ = [
    ("textureData", ctypes.c_void_p),
    ("texture", ctypes.c_ubyte * 0x8),
    ("imageDesc", ctypes.c_ubyte * 88),
    ("textureMemory", ctypes.c_ubyte * 24),
    ("textureSrvMips", ctypes.c_ubyte * 0x70),
    ("resourceState", ctypes.c_ubyte * 0x38),
    ("depthOnly", ctypes.c_ubyte),
    ("padding0x191", ctypes.c_ubyte * 0x7),
    ("textureSrv", ctypes.c_ubyte * 0x8),
    ("textureUav", ctypes.c_ubyte * 0x8),
    ("sampler", ctypes.c_ubyte * 0x8),
    ("lodClamp", ctypes.c_float),
    ("padding0x1B4", ctypes.c_ubyte * 0x4),
    ("mapping", ctypes.POINTER(ctypes.c_uint16)),
    ("evictableMipPageCount", ctypes.c_ubyte * 0x20),
    ("mipStartPage", ctypes.c_ubyte * 0x20),
    ("tailOffset", ctypes.c_uint64),
    ("tailArrayStride", ctypes.c_uint64),
    ("ultraMips", ctypes.c_uint16),
    ("detailableMips", ctypes.c_uint16),
    ("lodBias", ctypes.c_float),
    ("numPages", ctypes.c_int32),
    ("evictedPages", ctypes.c_int32),
    ("mipZeroPages", ctypes.c_int16),
    ("mipZeroUnusedPages", ctypes.c_int16),
    ("isPartiallyResident", ctypes.c_ubyte),
]


class cTkDynamicTexture(ctypes.Structure):
    renderTarget: common.cTkSmartResHandle
    width: int
    height: int

cTkDynamicTexture._fields_ = [
    ("renderTarget", common.cTkSmartResHandle),
    ("width", ctypes.c_int32),
    ("height", ctypes.c_int32),
]


class cTk2dImage(cTk2dObject, ctypes.Structure):
    uVs: list[common.Vector2f]
    texture: _Pointer["cTkTexture"]
    dynamicTexture: _Pointer["cTkDynamicTexture"]
    textureMipLevel: float
    visible: bool
    tiledUV: bool
    isRenderTarget: bool

cTk2dImage._fields_ = [
    ("uVs", common.Vector2f * 0x4),
    ("texture", ctypes.POINTER(cTkTexture)),
    ("dynamicTexture", ctypes.POINTER(cTkDynamicTexture)),
    ("textureMipLevel", ctypes.c_float),
    ("visible", ctypes.c_ubyte),
    ("tiledUV", ctypes.c_ubyte),
    ("isRenderTarget", ctypes.c_ubyte),
    ("padding0x77", ctypes.c_ubyte * 0x9)
]


class cGcNGui(ctypes.Structure):
    root: "cGcNGuiLayer"
    input: "cTkNGuiInput"
    useInput: bool
    pixelRatio: float
    fullscreen: bool
    customSize: common.Vector2f
    hasCustomSize: bool
    isInWorld: bool
    tk3dLayer: "cTk3dLayer"
    tk2dImage: "cTk2dImage"

cGcNGui._fields_ = [
    ("root", cGcNGuiLayer),
    ("input", cTkNGuiInput),
    ("useInput", ctypes.c_ubyte),
    ("padding0x451", ctypes.c_ubyte * 0x3),
    ("pixelRatio", ctypes.c_float),
    ("fullscreen", ctypes.c_ubyte),
    ("padding0x459", ctypes.c_ubyte * 0x3),
    ("customSize", common.Vector2f),
    ("hasCustomSize", ctypes.c_ubyte),
    ("isInWorld", ctypes.c_ubyte),
    ("padding0x466", ctypes.c_ubyte * 0xA),
    ("tk3dLayer", cTk3dLayer),
    ("tk2dImage", cTk2dImage),
]


class cTk2dImageEx(cTk2dImage, ctypes.Structure):
    resource: common.cTkSmartResHandle

cTk2dImageEx._fields_ = [
    ("resource", common.cTkSmartResHandle),
    ("padding0x84", ctypes.c_ubyte * 0xC)
]


class cGcShipHUD(cGcHUD, ctypes.Structure):
    class cGcVehicleScreen(ctypes.Structure):
        screenTexture: "cTkDynamicTexture"
        screenGUI: "cGcNGui"
        valid: bool

    cGcVehicleScreen._fields_ = [
        ("screenTexture", cTkDynamicTexture),
        ("padding0xC", ctypes.c_ubyte * 0x4),
        ("screenGUI", cGcNGui),
        ("valid", ctypes.c_ubyte),
        ("padding0x601", ctypes.c_ubyte * 0xF),
    ]

    hUDLayer: "cTk2dLayer"
    crosshairOuterCircleLarge: "cTk2dImageEx"
    crosshairOuterCircleLargeLayer: "cTk3dLayer"
    crosshairOuterCircleSmall: "cTk2dImageEx"
    crosshairOuterCircleSmallLayer: "cTk3dLayer"
    mouseArrowLayer: "cTk2dLayer"
    mouseArrowIcon: "cTk2dImageEx"
    shipForwardScreenPos: common.Vector3f
    shipAngle: float
    shipPitch: float
    landingEffect: bytes
    trackArrows: bytes
    shootList: std.vector[ctypes.c_uint64]
    selectedPlanet: int
    _meSelectedPlanetLabelState: int
    selectedPlanetPanelTime: float
    selectedPlanetPanelFadeTime: float
    selectedPlanetPanelVisible: bool
    selectedPlanetIsTargeted: bool
    lastKnownScanTime: float
    scanRevealTimer: float
    _meMiniJumpState: ctypes.c_int32
    hasPulseEncounterOnHUD: bool
    screens: bytes
    currentScreen: int
    sideScreenTextures: bytes
    sideScreenGUI: bytes
    sideScreenCursor: bytes
    sideScreenActive: bool
    sideScreenMeshes: bytes
    currentCockpit: common.TkHandle
    vehicleScreens: list[cGcVehicleScreen]
    speedoReverseMesh: common.TkHandle
    speedoPulseMesh: common.TkHandle
    speedoBarsMeshes: bytes
    currentSpeedoBar: int
    finalSpeedReadout: int
    mainScreenTexture: "cTkDynamicTexture"
    mainScreenGUI: "cGcNGui"
    targetProcName: common.cTkFixedString[0x7F]
    planetWorldPositions: bytes
    planetScreenPositions: bytes
    headsUpGUI: "cGcNGui"
    headsUpScreenHandle: int
    enemyTargetSceneRes: common.cTkSmartResHandle
    boostMultiplier: float
    @property
    def selectedPlanetLabelState(self):
        return safe_assign_enum(nms_enums.ePlanetLabelState, self._meSelectedPlanetLabelState)

cGcShipHUD._fields_ = [
    ("hUDLayer", cTk2dLayer),
    ("crosshairOuterCircleLarge", cTk2dImageEx),
    ("crosshairOuterCircleLargeLayer", cTk3dLayer),
    ("crosshairOuterCircleSmall", cTk2dImageEx),
    ("crosshairOuterCircleSmallLayer", cTk3dLayer),
    ("mouseArrowLayer", cTk2dLayer),
    ("mouseArrowIcon", cTk2dImageEx),
    ("shipForwardScreenPos", common.Vector3f),
    ("shipAngle", ctypes.c_float),
    ("shipPitch", ctypes.c_float),
    ("landingEffect", ctypes.c_ubyte * 24),
    ("trackArrows", ctypes.c_ubyte * 0x3100),
    ("shootList", std.vector[ctypes.c_uint64]),
    ("selectedPlanet", ctypes.c_int32),
    ("_meSelectedPlanetLabelState", ctypes.c_int32),
    ("selectedPlanetPanelTime", ctypes.c_float),
    ("selectedPlanetPanelFadeTime", ctypes.c_float),
    ("selectedPlanetPanelVisible", ctypes.c_ubyte),
    ("selectedPlanetIsTargeted", ctypes.c_ubyte),
    ("padding0x2368A", ctypes.c_ubyte * 0x2),
    ("lastKnownScanTime", ctypes.c_float),
    ("scanRevealTimer", ctypes.c_float),
    ("_meMiniJumpState", ctypes.c_int32),
    ("hasPulseEncounterOnHUD", ctypes.c_ubyte),
    ("padding0x23699", ctypes.c_ubyte * 0x7),
    ("screens", ctypes.c_ubyte * 0x10),
    ("currentScreen", ctypes.c_int32),
    ("sideScreenTextures", ctypes.c_ubyte * 0x30),
    ("padding0x236E4", ctypes.c_ubyte * 0xC),
    ("sideScreenGUI", ctypes.c_ubyte * 0x17C0),
    ("sideScreenCursor", ctypes.c_ubyte * 0x20),
    ("sideScreenActive", ctypes.c_ubyte),
    ("padding0x24ED1", ctypes.c_ubyte * 0x3),
    ("sideScreenMeshes", ctypes.c_ubyte * 0x10),
    ("currentCockpit", common.TkHandle),
    ("padding0x24EE8", ctypes.c_ubyte * 0x8),
    ("vehicleScreens", cGcShipHUD.cGcVehicleScreen * 0x7),
    ("speedoReverseMesh", common.TkHandle),
    ("speedoPulseMesh", common.TkHandle),
    ("speedoBarsMeshes", ctypes.c_ubyte * 0x14),
    ("currentSpeedoBar", ctypes.c_int32),
    ("finalSpeedReadout", ctypes.c_int32),
    ("mainScreenTexture", cTkDynamicTexture),
    ("mainScreenGUI", cGcNGui),
    ("targetProcName", common.cTkFixedString[0x7F]),
    ("padding0x27FFF", ctypes.c_ubyte * 0x1),
    ("planetWorldPositions", common.Vector3f * 0x6),
    ("planetScreenPositions", common.Vector3f * 0x6),
    ("headsUpGUI", cGcNGui),
    ("headsUpScreenHandle", ctypes.c_uint64),
    ("enemyTargetSceneRes", common.cTkSmartResHandle),
    ("boostMultiplier", ctypes.c_float),
]

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
    ("mu64UA",  ctypes.c_ulonglong),
    ("miNearestPlanetIndex", ctypes.c_int32),
    ("mfDistanceFromPlanet", ctypes.c_float),
    ("mfNearestPlanetSealevel", ctypes.c_float),
    ("_dummy0x64", ctypes.c_ubyte * 0xC),
    ("mNearestPlanetPos", common.Vector3f),
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


class sTkInputBinding(ctypes.Structure):
    _fields_ = [
        ("actionId", ctypes.c_int32),
        ("digitalBinding", ctypes.c_int32),
        ("analogueBinding", ctypes.c_int32),
    ]
    actionId: int
    digitalBinding: int
    analogueBinding: int


class sTkInputBindingsActionSet(ctypes.Structure):
    _fields_ = [
        ("actionSetId", ctypes.c_int32),
        ("_padding0x4", ctypes.c_ubyte * 0x4),
        ("bindings", std.vector[sTkInputBinding])
    ]
    actionSetId: int
    bindings: std.vector[sTkInputBinding]


class sTkInputBindings(ctypes.Structure):
    _fields_ = [
        ("actionSetBindings", std.vector[ctypes.POINTER(sTkInputBindingsActionSet)])
    ]
    actionSetBindings: std.vector[_Pointer[sTkInputBindingsActionSet]]


class sTkActionState(ctypes.Structure):
    _fields_ = [
        ("miDigitalFirstSet", ctypes.c_int32),
        ("miDigitalLastSet", ctypes.c_int32),
        ("miAnalogueLastSet", ctypes.c_int32),
        ("mfAnalogueValue", ctypes.c_float),
        ("mbAnalogueSource", ctypes.c_ubyte),
        ("miActionSetContinuity", ctypes.c_int32),
    ]
    miDigitalFirstSet: int
    miDigitalLastSet: int
    miAnalogueLastSet: int
    mfAnalogueValue: float
    mbAnalogueSource: bool
    miActionSetContinuity: int


class cTkInputPort(ctypes.Structure):
    _fields_ = [
        ("inputManager", ctypes.c_longlong),
        ("port", ctypes.c_int32),
        ("_padding0xC", ctypes.c_ubyte * 0x4),
        ("actionStates", common.cTkDynamicArray[sTkActionState]),
        ("now", ctypes.c_int32),
        ("_padding0x24", ctypes.c_ubyte * 0xC4),
        ("buttons", common.cTkBitArray[ctypes.c_uint64, 512]),
        ("buttonsPrev", common.cTkBitArray[ctypes.c_uint64, 512]),
        # TODO: Add more...
        ("rest", ctypes.c_ubyte * 0x278),
    ]

    inputManager: int
    port: int
    actionStates: common.cTkDynamicArray[sTkActionState]
    buttons: common.cTkBitArray[ctypes.c_uint64, 512]
    buttonsPrev: common.cTkBitArray[ctypes.c_uint64, 512]

    def SetButton(self, leIndex: nms_enums.eInputButton) -> None:
        """ Set the provided button as pressed. """
        this = ctypes.addressof(self)
        return call_function("cTkInputPort::SetButton", this, leIndex)

    @staticmethod
    def SetButton_(this: int, leIndex: nms_enums.eInputButton) -> None:
        """ Set the provided button as pressed for the provided instance. """
        return call_function("cTkInputPort::SetButton", this, leIndex)


class cTkInputManager(ctypes.Structure):
    _fields_ = [
        ("_padding", ctypes.c_ubyte * 0x2F0),
        ("bindings", std.vector[ctypes.POINTER(sTkInputBindings)]),
        ("_padding0x308", ctypes.c_ubyte * 0x18),
        ("portArray", std.array[cTkInputPort, 6])
    ]
    bindings: std.vector[_Pointer[sTkInputBindings]]
    portArray: std.array[cTkInputPort, 6]


class cTkDynamicGravityControl(ctypes.Structure):
    class cTkGravityPoint(ctypes.Structure):
        centre: common.Vector3f
        strength: float
        falloffRadiusSqr: float
        maxStrength: float

    cTkGravityPoint._fields_ = [
        ("centre", common.Vector3f),
        ("strength", ctypes.c_float),
        ("falloffRadiusSqr", ctypes.c_float),
        ("maxStrength", ctypes.c_float),
        ("padding0x1C", ctypes.c_ubyte * 0x4),
    ]

    class cTkGravityOBB(ctypes.Structure):
        up: common.Vector3f
        constantStrength: float
        falloffStrength: float
        transformInverse: common.cTkMatrix34
        untransformedCentre: common.Vector3f
        OBB: common.cTkAABB
        falloffRadiusSqr: float

    cTkGravityOBB._fields_ = [
        ("up", common.Vector3f),
        ("constantStrength", ctypes.c_float),
        ("falloffStrength", ctypes.c_float),
        # TODO: Add padding
        ("transformInverse", common.cTkMatrix34),
        ("untransformedCentre", common.Vector3f),
        ("OBB", common.cTkAABB),
        ("falloffRadiusSqr", ctypes.c_float),
    ]

    gravityPoints: list[cTkDynamicGravityControl.cTkGravityPoint]
    numGravityPoints: int
    gravityOBBs: bytes

cTkDynamicGravityControl._fields_ = [
    ("gravityPoints", cTkDynamicGravityControl.cTkGravityPoint * 0x9),
    ("numGravityPoints", ctypes.c_int32),
    ("gravityOBBs", common.cTkClassPool[cTkDynamicGravityControl.cTkGravityOBB, 0x40]),
]


class cGcApplication(cTkFSM, ctypes.Structure):
    """The Main Application structure"""
    class Data(ctypes.Structure):
        """Much of the associated application data"""
        FirstBootContext: cGcFirstBootContext
        TkMcQmcLFSRStore: bytes
        RealityManager: cGcRealityManager
        Simulation: cGcSimulation

    data: _Pointer[Data]
    playerSaveSlot: int
    gameMode: int
    seasonalGameMode: int
    savingEnabled: bool
    fullyBooted: bool
    lastRenderTimeMS: float
    paused: bool
    tkPaused: bool
    stepOneFrame: bool
    multiplayerActive: bool
    windowFocused: bool
    hasFocus: bool


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
    ("data", ctypes.POINTER(cGcApplication.Data)),
    ("playerSaveSlot", ctypes.c_uint32),
    ("gameMode", ctypes.c_uint32),
    ("seasonalGameMode", ctypes.c_uint32),
    ("savingEnabled", ctypes.c_ubyte),
    ("fullyBooted", ctypes.c_ubyte),
    ("_padding0x4E", ctypes.c_ubyte * 0x6A),
    ("lastRenderTimeMS", ctypes.c_longdouble),
    ("_padding0xC0", ctypes.c_ubyte * 0x8A84),
    ("paused", ctypes.c_ubyte),
    ("tkPaused", ctypes.c_ubyte),
    ("stepOneFrame", ctypes.c_ubyte),
    ("multiplayerActive", ctypes.c_ubyte),
    ("windowFocused", ctypes.c_ubyte),  # + 0x8B48
    ("hasFocus", ctypes.c_ubyte),
]