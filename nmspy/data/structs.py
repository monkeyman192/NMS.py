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


class cTkModelResource(ctypes.Structure):
    _fields_ = [
        ("macFilename", common.cTkFixedString[0x80]),
        ("mResHandle", common.cTkSmartResHandle),
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


class cGcPlanetData(ctypes.Structure):
    name: common.cTkFixedString[0x80]
    life: "cGcPlanetLife"
    creatureLife: "cGcPlanetLife"
    hazard: "cGcPlanetHazardData"
    _meResourceLevel: ctypes.c_int32
    buildingLevel: "cGcBuildingDensityLevels"
    commonSubstanceID: common.TkID[0x10]
    uncommonSubstanceID: common.TkID[0x10]
    rareSubstanceID: common.TkID[0x10]
    extraResourceHints: common.cTkDynamicArray[cGcPlanetDataResourceHint]
    colours: "cGcPlanetColourData"
    tileColours: bytes
    weather: "cGcPlanetWeatherData"
    clouds: "cGcPlanetCloudProperties"
    water: "cGcPlanetWaterData"
    terrainFile: common.cTkFixedString[0x80]
    terrain: "cTkVoxelGeneratorData"
    tileTypeSet: int
    tileTypeIndices: common.cTkDynamicArray[ctypes.c_int32]
    spawnData: "cGcEnvironmentSpawnData"
    inhabitingRace: "cGcAlienRace"
    buildingData: "cGcPlanetBuildingData"
    generationData: "cGcPlanetGenerationIntermediateData"
    sentinelTimer: common.Vector2f
    flybyTimer: common.Vector2f
    planetInfo: "cGcPlanetInfo"
    sentinelData: "cGcPlanetSentinelData"
    rings: "cGcPlanetRingData"
    inEmptySystem: bool
    inAbandonedSystem: bool
    fuelMultiplier: float


class cGcPlanetLife(ctypes.Structure):
    _meLifeSetting: ctypes.c_int32

cGcPlanetLife._fields_ = [
    ("_meLifeSetting", ctypes.c_int32),
]


class cGcPlanetHazardData(ctypes.Structure):
    temperature: list[float]
    toxicity: list[float]
    radiation: list[float]
    lifeSupportDrain: list[float]

cGcPlanetHazardData._fields_ = [
    ("temperature", ctypes.c_float * 0x5),
    ("toxicity", ctypes.c_float * 0x5),
    ("radiation", ctypes.c_float * 0x5),
    ("lifeSupportDrain", ctypes.c_float * 0x5),
]


class cGcBuildingDensityLevels(ctypes.Structure):
    _meBuildingDensity: ctypes.c_int32

cGcBuildingDensityLevels._fields_ = [
    ("_meBuildingDensity", ctypes.c_int32),
]


class cGcPlanetDataResourceHint(ctypes.Structure):
    hint: common.TkID[0x10]
    icon: common.TkID[0x10]

cGcPlanetDataResourceHint._fields_ = [
    ("hint", common.TkID[0x10]),
    ("icon", common.TkID[0x10]),
]


class cGcPlanetColourData(ctypes.Structure):
    palettes: bytes

cGcPlanetColourData._fields_ = [
    ("palettes", ctypes.c_ubyte * 0x1960),
]


class cGcWeatherOptions(ctypes.Structure):
    _meWeather: ctypes.c_int32

cGcWeatherOptions._fields_ = [
    ("_meWeather", ctypes.c_int32),
]


class cGcPlanetHeavyAirData(ctypes.Structure):
    filename: common.cTkFixedString[0x80]
    colours: bytes

cGcPlanetHeavyAirData._fields_ = [
    ("filename", common.cTkFixedString[0x80]),
    ("colours", ctypes.c_ubyte * 0xA0),
]


class cGcScreenFilters(ctypes.Structure):
    _meScreenFilter: ctypes.c_int32

cGcScreenFilters._fields_ = [
    ("_meScreenFilter", ctypes.c_int32),
]


class cGcRainbowType(ctypes.Structure):
    _meRainbowType: ctypes.c_int32

cGcRainbowType._fields_ = [
    ("_meRainbowType", ctypes.c_int32),
]


class cGcPlanetWeatherData(ctypes.Structure):
    weatherType: "cGcWeatherOptions"
    heavyAir: "cGcPlanetHeavyAirData"
    _meWeatherIntensity: ctypes.c_int32
    _meStormFrequency: ctypes.c_int32
    _meAtmosphereType: ctypes.c_int32
    dayColourIndex: int
    duskColourIndex: int
    screenFilter: "cGcScreenFilters"
    stormScreenFilter: "cGcScreenFilters"
    rainbowType: "cGcRainbowType"
    nightColourIndex: int

cGcPlanetWeatherData._fields_ = [
    ("weatherType", cGcWeatherOptions),
    ("padding0x4", ctypes.c_ubyte * 0xC),
    ("heavyAir", cGcPlanetHeavyAirData),
    ("_meWeatherIntensity", ctypes.c_int32),
    ("_meStormFrequency", ctypes.c_int32),
    ("_meAtmosphereType", ctypes.c_int32),
    ("dayColourIndex", ctypes.c_int32),
    ("duskColourIndex", ctypes.c_int32),
    ("screenFilter", cGcScreenFilters),
    ("stormScreenFilter", cGcScreenFilters),
    ("rainbowType", cGcRainbowType),
    ("nightColourIndex", ctypes.c_int32),
    ("endpadding", ctypes.c_ubyte * 0xC),
]


class cGcPlanetCloudProperties(ctypes.Structure):
    seed: common.GcSeed
    coverage1: float
    coverage2: float
    coverage3: float
    offset1: float
    offset2: float
    offset3: float
    coverExtremes: common.Vector2f
    ratio: float
    rateOfChange: float
    secondaryRateOfChange: float
    _meCloudiness: ctypes.c_int32

cGcPlanetCloudProperties._fields_ = [
    ("seed", common.GcSeed),
    ("coverage1", ctypes.c_float),
    ("coverage2", ctypes.c_float),
    ("coverage3", ctypes.c_float),
    ("offset1", ctypes.c_float),
    ("offset2", ctypes.c_float),
    ("offset3", ctypes.c_float),
    ("coverExtremes", common.Vector2f),
    ("ratio", ctypes.c_float),
    ("rateOfChange", ctypes.c_float),
    ("secondaryRateOfChange", ctypes.c_float),
    ("_meCloudiness", ctypes.c_int32),
]


class cGcPlanetWaterData(ctypes.Structure):
    colourIndex: int
    waterStrength: float
    waterColourStrength: float
    waterMultiplyStrength: float
    waterMultiplyMax: float
    waterRoughness: float
    fresnelPower: float
    fresnelMin: float
    fresnelMax: float
    wave1Scale: float
    wave1Height: float
    wave1Speed: float
    wave2Scale: float
    wave2Height: float
    wave2Speed: float
    normalMap1Scale: float
    normalMap1Speed: float
    normalMap2Scale: float
    normalMap2Speed: float
    foamFadeHeight: float
    foam1Scale: float
    foam1Speed: float
    foam2Scale: float
    foam2Speed: float
    heavyAir: "cGcPlanetHeavyAirData"

cGcPlanetWaterData._fields_ = [
    ("colourIndex", ctypes.c_int32),
    ("waterStrength", ctypes.c_float),
    ("waterColourStrength", ctypes.c_float),
    ("waterMultiplyStrength", ctypes.c_float),
    ("waterMultiplyMax", ctypes.c_float),
    ("waterRoughness", ctypes.c_float),
    ("fresnelPower", ctypes.c_float),
    ("fresnelMin", ctypes.c_float),
    ("fresnelMax", ctypes.c_float),
    ("wave1Scale", ctypes.c_float),
    ("wave1Height", ctypes.c_float),
    ("wave1Speed", ctypes.c_float),
    ("wave2Scale", ctypes.c_float),
    ("wave2Height", ctypes.c_float),
    ("wave2Speed", ctypes.c_float),
    ("normalMap1Scale", ctypes.c_float),
    ("normalMap1Speed", ctypes.c_float),
    ("normalMap2Scale", ctypes.c_float),
    ("normalMap2Speed", ctypes.c_float),
    ("foamFadeHeight", ctypes.c_float),
    ("foam1Scale", ctypes.c_float),
    ("foam1Speed", ctypes.c_float),
    ("foam2Scale", ctypes.c_float),
    ("foam2Speed", ctypes.c_float),
    ("heavyAir", cGcPlanetHeavyAirData),
]

class cTkNoiseVoxelTypeEnum(ctypes.Structure):
    _meNoiseVoxelType: ctypes.c_int32

cTkNoiseVoxelTypeEnum._fields_ = [
    ("_meNoiseVoxelType", ctypes.c_int32),
]


class cTkVoxelGeneratorData(ctypes.Structure):
    baseSeed: common.GcSeed
    seaLevel: float
    beachHeight: float
    noSeaBaseLevel: float
    buildingVoxelType: "cTkNoiseVoxelTypeEnum"
    resourceVoxelType: "cTkNoiseVoxelTypeEnum"
    noiseLayers: bytes
    gridLayers: bytes
    features: bytes
    caves: bytes
    minimumCaveDepth: float
    caveRoofSmoothingDist: float
    maximumSeaLevelCaveDepth: float
    buildingTextureRadius: float
    buildingSmoothingRadius: float
    buildingSmoothingHeight: float
    waterFadeInDistance: float

cTkVoxelGeneratorData._fields_ = [
    ("baseSeed", common.GcSeed),
    ("seaLevel", ctypes.c_float),
    ("beachHeight", ctypes.c_float),
    ("noSeaBaseLevel", ctypes.c_float),
    ("buildingVoxelType", cTkNoiseVoxelTypeEnum),
    ("resourceVoxelType", cTkNoiseVoxelTypeEnum),
    ("noiseLayers", ctypes.c_ubyte * 0x440),
    ("gridLayers", ctypes.c_ubyte * 0xEE8),
    ("features", ctypes.c_ubyte * 0x1DC),
    ("caves", ctypes.c_ubyte * 0x88),
    ("minimumCaveDepth", ctypes.c_float),
    ("caveRoofSmoothingDist", ctypes.c_float),
    ("maximumSeaLevelCaveDepth", ctypes.c_float),
    ("buildingTextureRadius", ctypes.c_float),
    ("buildingSmoothingRadius", ctypes.c_float),
    ("buildingSmoothingHeight", ctypes.c_float),
    ("waterFadeInDistance", ctypes.c_float),
    ("endpadding", ctypes.c_ubyte * 0x4),
]


class cTkPaletteTexture(ctypes.Structure):
    _mePalette: ctypes.c_int32
    _meColourAlt: ctypes.c_int32

cTkPaletteTexture._fields_ = [
    ("_mePalette", ctypes.c_int32),
    ("_meColourAlt", ctypes.c_int32),
]


class cTkProceduralTextureChosenOption(ctypes.Structure):
    layer: common.TkID[0x10]
    group: common.TkID[0x10]
    palette: "cTkPaletteTexture"
    overrideColour: bool
    colour: common.Colour
    optionName: common.TkID[0x20]

cTkProceduralTextureChosenOption._fields_ = [
    ("layer", common.TkID[0x10]),
    ("group", common.TkID[0x10]),
    ("palette", cTkPaletteTexture),
    ("overrideColour", ctypes.c_ubyte),
    ("padding0x29", ctypes.c_ubyte * 0x7),
    ("colour", common.Colour),
    ("optionName", common.TkID[0x20]),
]


class cTkProceduralTextureChosenOptionSampler(ctypes.Structure):
    options: common.cTkDynamicArray[cTkProceduralTextureChosenOption]

cTkProceduralTextureChosenOptionSampler._fields_ = [
    ("options", common.cTkDynamicArray[cTkProceduralTextureChosenOption]),
]


class cTkProceduralTextureChosenOptionList(ctypes.Structure):
    samplers: common.cTkDynamicArray[cTkProceduralTextureChosenOptionSampler]

cTkProceduralTextureChosenOptionList._fields_ = [
    ("samplers", common.cTkDynamicArray[cTkProceduralTextureChosenOptionSampler]),
]


class cGcResourceElement(ctypes.Structure):
    filename: common.cTkFixedString[0x80]
    resHandle: common.cTkSmartResHandle
    seed: common.GcSeed
    altId: common.cTkFixedString[0x200]
    proceduralTexture: "cTkProceduralTextureChosenOptionList"

cGcResourceElement._fields_ = [
    ("filename", common.cTkFixedString[0x80]),
    ("resHandle", common.cTkSmartResHandle),
    ("padding0x84", ctypes.c_ubyte * 0x4),
    ("seed", common.GcSeed),
    ("altId", common.cTkFixedString[0x200]),
    ("proceduralTexture", cTkProceduralTextureChosenOptionList),
]


class cGcTerrainTileType(ctypes.Structure):
    _meTileType: ctypes.c_int32

cGcTerrainTileType._fields_ = [
    ("_meTileType", ctypes.c_int32),
]


class cGcCreatureTypes(ctypes.Structure):
    _meCreatureType: ctypes.c_int32

cGcCreatureTypes._fields_ = [
    ("_meCreatureType", ctypes.c_int32),
]


class cGcCreatureRoles(ctypes.Structure):
    _meCreatureRole: ctypes.c_int32

cGcCreatureRoles._fields_ = [
    ("_meCreatureRole", ctypes.c_int32),
]


class cGcCreatureHemiSphere(ctypes.Structure):
    _meCreatureHemiSphere: ctypes.c_int32

cGcCreatureHemiSphere._fields_ = [
    ("_meCreatureHemiSphere", ctypes.c_int32),
]


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


class cGcCreatureSpawnData(ctypes.Structure):
    resource: "cGcResourceElement"
    femaleResource: "cGcResourceElement"
    extraResource: "cGcResourceElement"
    tileType: "cGcTerrainTileType"
    swapPrimaryForSecondaryColour: bool
    swapPrimaryForRandomColour: bool
    minScale: float
    maxScale: float
    creatureID: common.TkID[0x10]
    creatureType: "cGcCreatureTypes"
    creatureRole: "cGcCreatureRoles"
    filter: common.TkID[0x20]
    creatureMinGroupSize: int
    creatureMaxGroupSize: int
    creatureGroupsPerSquareKm: float
    hemiSphere: "cGcCreatureHemiSphere"
    creatureSpawnDistance: float
    creatureDespawnDistance: float
    creatureActiveInDayChance: float
    creatureActiveInNightChance: float
    rarity: "cGcRarity"
    allowFur: bool
    herd: bool
    roleDataIndex: int

cGcCreatureSpawnData._fields_ = [
    ("resource", cGcResourceElement),
    ("femaleResource", cGcResourceElement),
    ("extraResource", cGcResourceElement),
    ("tileType", cGcTerrainTileType),
    ("swapPrimaryForSecondaryColour", ctypes.c_ubyte),
    ("swapPrimaryForRandomColour", ctypes.c_ubyte),
    ("padding0x7FE", ctypes.c_ubyte * 0x2),
    ("minScale", ctypes.c_float),
    ("maxScale", ctypes.c_float),
    ("creatureID", common.TkID[0x10]),
    ("creatureType", cGcCreatureTypes),
    ("creatureRole", cGcCreatureRoles),
    ("filter", common.TkID[0x20]),
    ("creatureMinGroupSize", ctypes.c_int32),
    ("creatureMaxGroupSize", ctypes.c_int32),
    ("creatureGroupsPerSquareKm", ctypes.c_float),
    ("hemiSphere", cGcCreatureHemiSphere),
    ("creatureSpawnDistance", ctypes.c_float),
    ("creatureDespawnDistance", ctypes.c_float),
    ("creatureActiveInDayChance", ctypes.c_float),
    ("creatureActiveInNightChance", ctypes.c_float),
    ("rarity", cGcRarity),
    ("allowFur", ctypes.c_ubyte),
    ("herd", ctypes.c_ubyte),
    ("padding0x866", ctypes.c_ubyte * 0x2),
    ("roleDataIndex", ctypes.c_int32),
]


class cGcObjectSpawnDataVariant(ctypes.Structure):
    ID: common.TkID[0x10]
    coverage: float
    flatDensity: float
    slopeDensity: float
    slopeMultiplier: float
    maxRegionRadius: int
    maxImposterRadius: int
    fadeOutStartDistance: float
    fadeOutEndDistance: float
    fadeOutOffsetDistance: float
    lodDistances: bytes

cGcObjectSpawnDataVariant._fields_ = [
    ("ID", common.TkID[0x10]),
    ("coverage", ctypes.c_float),
    ("flatDensity", ctypes.c_float),
    ("slopeDensity", ctypes.c_float),
    ("slopeMultiplier", ctypes.c_float),
    ("maxRegionRadius", ctypes.c_int32),
    ("maxImposterRadius", ctypes.c_int32),
    ("fadeOutStartDistance", ctypes.c_float),
    ("fadeOutEndDistance", ctypes.c_float),
    ("fadeOutOffsetDistance", ctypes.c_float),
    ("lodDistances", ctypes.c_ubyte * 0x14),
]


class cGcObjectSpawnData(ctypes.Structure):
    debugName: common.TkID[0x10]
    _meType: ctypes.c_int32
    resource: "cGcResourceElement"
    altResources: common.cTkDynamicArray[cGcResourceElement]
    extraTileTypes: common.cTkDynamicArray[cGcTerrainTileType]
    placement: common.TkID[0x10]
    seed: common.GcSeed
    _mePlacementPriority: ctypes.c_int32
    _meLargeObjectCoverage: ctypes.c_int32
    _meOverlapStyle: ctypes.c_int32
    minHeight: float
    maxHeight: float
    relativeToSeaLevel: bool
    minAngle: float
    maxAngle: float
    matchGroundColour: bool
    _meGroundColourIndex: ctypes.c_int32
    swapPrimaryForSecondaryColour: bool
    swapPrimaryForRandomColour: bool
    alignToNormal: bool
    minScale: float
    maxScale: float
    minScaleY: float
    maxScaleY: float
    slopeScaling: float
    patchEdgeScaling: float
    maxXZRotation: float
    autoCollision: bool
    collideWithPlayer: bool
    collideWithPlayerVehicle: bool
    destroyedByPlayerVehicle: bool
    destroyedByPlayerShip: bool
    destroyedByTerrainEdit: bool
    invisibleToCamera: bool
    creaturesCanEat: bool
    shearWindStrength: float
    destroyedByVehicleEffect: common.TkID[0x10]
    qualityVariantData: "cGcObjectSpawnDataVariant"
    qualityVariants: common.cTkDynamicArray[cGcObjectSpawnDataVariant]

cGcObjectSpawnData._fields_ = [
    ("debugName", common.TkID[0x10]),
    ("_meType", ctypes.c_int32),
    ("padding0x14", ctypes.c_ubyte * 0x4),
    ("resource", cGcResourceElement),
    ("altResources", common.cTkDynamicArray[cGcResourceElement]),
    ("extraTileTypes", common.cTkDynamicArray[cGcTerrainTileType]),
    ("placement", common.TkID[0x10]),
    ("seed", common.GcSeed),
    ("_mePlacementPriority", ctypes.c_int32),
    ("_meLargeObjectCoverage", ctypes.c_int32),
    ("_meOverlapStyle", ctypes.c_int32),
    ("minHeight", ctypes.c_float),
    ("maxHeight", ctypes.c_float),
    ("relativeToSeaLevel", ctypes.c_ubyte),
    ("padding0x315", ctypes.c_ubyte * 0x3),
    ("minAngle", ctypes.c_float),
    ("maxAngle", ctypes.c_float),
    ("matchGroundColour", ctypes.c_ubyte),
    ("padding0x321", ctypes.c_ubyte * 0x3),
    ("_meGroundColourIndex", ctypes.c_int32),
    ("swapPrimaryForSecondaryColour", ctypes.c_ubyte),
    ("swapPrimaryForRandomColour", ctypes.c_ubyte),
    ("alignToNormal", ctypes.c_ubyte),
    ("padding0x32B", ctypes.c_ubyte * 0x1),
    ("minScale", ctypes.c_float),
    ("maxScale", ctypes.c_float),
    ("minScaleY", ctypes.c_float),
    ("maxScaleY", ctypes.c_float),
    ("slopeScaling", ctypes.c_float),
    ("patchEdgeScaling", ctypes.c_float),
    ("maxXZRotation", ctypes.c_float),
    ("autoCollision", ctypes.c_ubyte),
    ("collideWithPlayer", ctypes.c_ubyte),
    ("collideWithPlayerVehicle", ctypes.c_ubyte),
    ("destroyedByPlayerVehicle", ctypes.c_ubyte),
    ("destroyedByPlayerShip", ctypes.c_ubyte),
    ("destroyedByTerrainEdit", ctypes.c_ubyte),
    ("invisibleToCamera", ctypes.c_ubyte),
    ("creaturesCanEat", ctypes.c_ubyte),
    ("shearWindStrength", ctypes.c_float),
    ("padding0x354", ctypes.c_ubyte * 0x4),
    ("destroyedByVehicleEffect", common.TkID[0x10]),
    ("qualityVariantData", cGcObjectSpawnDataVariant),
    ("qualityVariants", common.cTkDynamicArray[cGcObjectSpawnDataVariant]),
]


class cGcSelectableObjectSpawnData(ctypes.Structure):
    resource: "cGcResourceElement"

cGcSelectableObjectSpawnData._fields_ = [
    ("resource", cGcResourceElement),
]


class cGcSelectableObjectSpawnList(ctypes.Structure):
    name: common.TkID[0x10]
    objects: common.cTkDynamicArray[cGcSelectableObjectSpawnData]

cGcSelectableObjectSpawnList._fields_ = [
    ("name", common.TkID[0x10]),
    ("objects", common.cTkDynamicArray[cGcSelectableObjectSpawnData]),
]


class cGcEnvironmentSpawnData(ctypes.Structure):
    creatures: common.cTkDynamicArray[cGcCreatureSpawnData]
    distantObjects: common.cTkDynamicArray[cGcObjectSpawnData]
    landmarks: common.cTkDynamicArray[cGcObjectSpawnData]
    objects: common.cTkDynamicArray[cGcObjectSpawnData]
    detailObjects: common.cTkDynamicArray[cGcObjectSpawnData]
    selectableObjects: common.cTkDynamicArray[cGcSelectableObjectSpawnList]

cGcEnvironmentSpawnData._fields_ = [
    ("creatures", common.cTkDynamicArray[cGcCreatureSpawnData]),
    ("distantObjects", common.cTkDynamicArray[cGcObjectSpawnData]),
    ("landmarks", common.cTkDynamicArray[cGcObjectSpawnData]),
    ("objects", common.cTkDynamicArray[cGcObjectSpawnData]),
    ("detailObjects", common.cTkDynamicArray[cGcObjectSpawnData]),
    ("selectableObjects", common.cTkDynamicArray[cGcSelectableObjectSpawnList]),
]


class cGcBuildingSpawnSlot(ctypes.Structure):
    hasBuilding: bool
    buildingDataIndex: int
    probability: float

cGcBuildingSpawnSlot._fields_ = [
    ("hasBuilding", ctypes.c_ubyte),
    ("padding0x1", ctypes.c_ubyte * 0x3),
    ("buildingDataIndex", ctypes.c_int32),
    ("probability", ctypes.c_float),
]


class cGcBuildingClassification(ctypes.Structure):
    _meBuildingClass: ctypes.c_int32

cGcBuildingClassification._fields_ = [
    ("_meBuildingClass", ctypes.c_int32),
]


class cTkNoiseFlattenOptions(ctypes.Structure):
    _meFlattening: ctypes.c_int32
    _meWaterPlacement: ctypes.c_int32

cTkNoiseFlattenOptions._fields_ = [
    ("_meFlattening", ctypes.c_int32),
    ("_meWaterPlacement", ctypes.c_int32),
]


class cGcBuildingSpawnData(ctypes.Structure):
    density: float
    resource: "cGcResourceElement"
    lSystemID: int
    wFCModuleSet: int
    wFCBuildingPreset: int
    autoCollision: bool
    seed: common.GcSeed
    classification: "cGcBuildingClassification"
    clusterLayouts: bytes
    clusterLayoutCount: int
    clusterSpacing: float
    flattenType: "cTkNoiseFlattenOptions"
    givesShelter: bool
    alignToNormal: bool
    lowerIntoGround: bool
    scale: float
    maxXZRotation: float
    radius: float
    minHeight: float
    maxHeight: float
    instanceID: int
    aABBMin: common.Vector3f
    aABBMax: common.Vector3f
    buildingSizeCalculated: bool
    ignoreParticlesAABB: bool

cGcBuildingSpawnData._fields_ = [
    ("density", ctypes.c_float),
    ("padding0x4", ctypes.c_ubyte * 0x4),
    ("resource", cGcResourceElement),
    ("lSystemID", ctypes.c_int32),
    ("wFCModuleSet", ctypes.c_int32),
    ("wFCBuildingPreset", ctypes.c_int32),
    ("autoCollision", ctypes.c_ubyte),
    ("padding0x2BD", ctypes.c_ubyte * 0x3),
    ("seed", common.GcSeed),
    ("classification", cGcBuildingClassification),
    ("clusterLayouts", ctypes.c_ubyte * 0x20),
    ("clusterLayoutCount", ctypes.c_int32),
    ("clusterSpacing", ctypes.c_float),
    ("flattenType", cTkNoiseFlattenOptions),
    ("givesShelter", ctypes.c_ubyte),
    ("alignToNormal", ctypes.c_ubyte),
    ("lowerIntoGround", ctypes.c_ubyte),
    ("padding0x307", ctypes.c_ubyte * 0x1),
    ("scale", ctypes.c_float),
    ("maxXZRotation", ctypes.c_float),
    ("radius", ctypes.c_float),
    ("minHeight", ctypes.c_float),
    ("maxHeight", ctypes.c_float),
    ("instanceID", ctypes.c_int32),
    ("aABBMin", common.Vector3f),
    ("aABBMax", common.Vector3f),
    ("buildingSizeCalculated", ctypes.c_ubyte),
    ("ignoreParticlesAABB", ctypes.c_ubyte),
]


class cGcBuildingOverrideData(ctypes.Structure):
    seed: common.GcSeed
    position: common.Vector3f
    index: int

cGcBuildingOverrideData._fields_ = [
    ("seed", common.GcSeed),
    ("position", common.Vector3f),
    ("index", ctypes.c_int32),
]


class cGcPlanetBuildingData(ctypes.Structure):
    buildingSlots: common.cTkDynamicArray[cGcBuildingSpawnSlot]
    buildings: common.cTkDynamicArray[cGcBuildingSpawnData]
    overrideBuildings: common.cTkDynamicArray[cGcBuildingOverrideData]
    spacing: float
    planetRadius: float
    voronoiPointDivisions: float
    voronoiSectorSeed: int
    voronoiPointSeed: int
    initialBuildingsPlaced: bool
    isPrime: bool

cGcPlanetBuildingData._fields_ = [
    ("buildingSlots", common.cTkDynamicArray[cGcBuildingSpawnSlot]),
    ("buildings", common.cTkDynamicArray[cGcBuildingSpawnData]),
    ("overrideBuildings", common.cTkDynamicArray[cGcBuildingOverrideData]),
    ("spacing", ctypes.c_float),
    ("planetRadius", ctypes.c_float),
    ("voronoiPointDivisions", ctypes.c_float),
    ("voronoiSectorSeed", ctypes.c_int32),
    ("voronoiPointSeed", ctypes.c_int32),
    ("initialBuildingsPlaced", ctypes.c_ubyte),
    ("isPrime", ctypes.c_ubyte),
]


class cGcCreatureSizeClasses(ctypes.Structure):
    _meCreatureSizeClass: ctypes.c_int32

cGcCreatureSizeClasses._fields_ = [
    ("_meCreatureSizeClass", ctypes.c_int32),
]


class cGcCreatureGenerationDensity(ctypes.Structure):
    _meDensity: ctypes.c_int32

cGcCreatureGenerationDensity._fields_ = [
    ("_meDensity", ctypes.c_int32),
]


class cGcCreatureActiveTime(ctypes.Structure):
    _meCreatureActiveTime: ctypes.c_int32

cGcCreatureActiveTime._fields_ = [
    ("_meCreatureActiveTime", ctypes.c_int32),
]


class cGcCreatureRoleDescription(ctypes.Structure):
    role: "cGcCreatureRoles"
    forceType: "cGcCreatureTypes"
    forceID: common.TkID[0x10]
    requireTag: common.TkID[0x10]
    minSize: "cGcCreatureSizeClasses"
    maxSize: "cGcCreatureSizeClasses"
    minGroupSize: int
    maxGroupSize: int
    density: "cGcCreatureGenerationDensity"
    activeTime: "cGcCreatureActiveTime"
    probabilityOfBeingEnabled: float
    increasedSpawnDistance: float
    filter: common.TkID[0x20]

cGcCreatureRoleDescription._fields_ = [
    ("role", cGcCreatureRoles),
    ("forceType", cGcCreatureTypes),
    ("forceID", common.TkID[0x10]),
    ("requireTag", common.TkID[0x10]),
    ("minSize", cGcCreatureSizeClasses),
    ("maxSize", cGcCreatureSizeClasses),
    ("minGroupSize", ctypes.c_int32),
    ("maxGroupSize", ctypes.c_int32),
    ("density", cGcCreatureGenerationDensity),
    ("activeTime", cGcCreatureActiveTime),
    ("probabilityOfBeingEnabled", ctypes.c_float),
    ("increasedSpawnDistance", ctypes.c_float),
    ("filter", common.TkID[0x20]),
]


class cGcCreatureInfo(ctypes.Structure):
    _meAge: ctypes.c_int32
    gender1: common.cTkFixedString[0x80]
    gender2: common.cTkFixedString[0x80]
    temperament: common.cTkFixedString[0x80]
    diet: common.cTkFixedString[0x80]
    weight1: common.cTkFixedString[0x80]
    height1: common.cTkFixedString[0x80]
    weight2: common.cTkFixedString[0x80]
    height2: common.cTkFixedString[0x80]
    weight1: float
    height1: float
    weight2: float
    height2: float
    notes: common.cTkFixedString[0x80]
    rarity: "cGcRarity"
    biomeDesc: common.TkID[0x20]
    tempermentDesc: common.TkID[0x20]
    dietDesc: common.TkID[0x20]
    notesDesc: common.TkID[0x20]

cGcCreatureInfo._fields_ = [
    ("_meAge", ctypes.c_int32),
    ("gender1", common.cTkFixedString[0x80]),
    ("gender2", common.cTkFixedString[0x80]),
    ("temperament", common.cTkFixedString[0x80]),
    ("diet", common.cTkFixedString[0x80]),
    ("weight1", common.cTkFixedString[0x80]),
    ("height1", common.cTkFixedString[0x80]),
    ("weight2", common.cTkFixedString[0x80]),
    ("height2", common.cTkFixedString[0x80]),
    ("weight1", ctypes.c_float),
    ("height1", ctypes.c_float),
    ("weight2", ctypes.c_float),
    ("height2", ctypes.c_float),
    ("notes", common.cTkFixedString[0x80]),
    ("rarity", cGcRarity),
    ("biomeDesc", common.TkID[0x20]),
    ("tempermentDesc", common.TkID[0x20]),
    ("dietDesc", common.TkID[0x20]),
    ("notesDesc", common.TkID[0x20]),
]


class cGcCreatureDiet(ctypes.Structure):
    _meDiet: ctypes.c_int32

cGcCreatureDiet._fields_ = [
    ("_meDiet", ctypes.c_int32),
]


class cGcCreatureRoleData(ctypes.Structure):
    seed: common.GcSeed
    type: "cGcCreatureTypes"
    creatureId: common.TkID[0x10]
    description: "cGcCreatureRoleDescription"
    info: "cGcCreatureInfo"
    tileType: "cGcTerrainTileType"
    diet: "cGcCreatureDiet"
    groupsPerSquareKm: float
    hemiSphere: "cGcCreatureHemiSphere"
    filter: common.TkID[0x20]

cGcCreatureRoleData._fields_ = [
    ("seed", common.GcSeed),
    ("type", cGcCreatureTypes),
    ("padding0x14", ctypes.c_ubyte * 0x4),
    ("creatureId", common.TkID[0x10]),
    ("description", cGcCreatureRoleDescription),
    ("info", cGcCreatureInfo),
    ("tileType", cGcTerrainTileType),
    ("diet", cGcCreatureDiet),
    ("groupsPerSquareKm", ctypes.c_float),
    ("hemiSphere", cGcCreatureHemiSphere),
    ("filter", common.TkID[0x20]),
]


class cGcCreatureRoleDataTable(ctypes.Structure):
    availableRoles: common.cTkDynamicArray[cGcCreatureRoleData]
    maxProportionFlying: float
    hasSandWorms: bool
    sandWormFrequency: float

cGcCreatureRoleDataTable._fields_ = [
    ("availableRoles", common.cTkDynamicArray[cGcCreatureRoleData]),
    ("maxProportionFlying", ctypes.c_float),
    ("hasSandWorms", ctypes.c_ubyte),
    ("padding0x15", ctypes.c_ubyte * 0x3),
    ("sandWormFrequency", ctypes.c_float),
    ("endpadding", ctypes.c_ubyte * 0x4),
]


class cGcTerrainControls(ctypes.Structure):
    noiseLayers: bytes
    gridLayers: bytes
    features: bytes
    caves: bytes
    waterActiveFrequency: float
    highWaterActiveFrequency: float
    rockTileFrequency: float
    substanceTileFrequency: float
    forceContinentalNoise: bool

cGcTerrainControls._fields_ = [
    ("noiseLayers", ctypes.c_ubyte * 0x20),
    ("gridLayers", ctypes.c_ubyte * 0x24),
    ("features", ctypes.c_ubyte * 0x1C),
    ("caves", ctypes.c_ubyte * 0x4),
    ("waterActiveFrequency", ctypes.c_float),
    ("highWaterActiveFrequency", ctypes.c_float),
    ("rockTileFrequency", ctypes.c_float),
    ("substanceTileFrequency", ctypes.c_float),
    ("forceContinentalNoise", ctypes.c_ubyte),
]


class cGcExternalObjectListOptions(ctypes.Structure):
    name: common.TkID[0x10]
    resourceHint: common.TkID[0x10]
    resourceHintIcon: common.TkID[0x10]
    probability: float
    seasonalProbabilityOverride: float
    tileType: "cGcTerrainTileType"
    allowLimiting: bool
    chooseUsingLifeLevel: bool
    options: common.cTkDynamicArray[common.cTkFixedString[0x80]]

cGcExternalObjectListOptions._fields_ = [
    ("name", common.TkID[0x10]),
    ("resourceHint", common.TkID[0x10]),
    ("resourceHintIcon", common.TkID[0x10]),
    ("probability", ctypes.c_float),
    ("seasonalProbabilityOverride", ctypes.c_float),
    ("tileType", cGcTerrainTileType),
    ("allowLimiting", ctypes.c_ubyte),
    ("chooseUsingLifeLevel", ctypes.c_ubyte),
    ("padding0x3E", ctypes.c_ubyte * 0x2),
    ("options", common.cTkDynamicArray[common.cTkFixedString[0x80]]),
]


class cGcPlanetGenerationIntermediateData(ctypes.Structure):
    seed: common.GcSeed
    terrainSettingIndex: int
    starType: "cGcGalaxyStarTypes"
    class_: "cGcPlanetClass"
    size: "cGcPlanetSize"
    creatureRoles: "cGcCreatureRoleDataTable"
    terrain: "cGcTerrainControls"
    biome: "cGcBiomeType"
    biomeSubType: "cGcBiomeSubType"
    terrainFile: common.cTkFixedString[0x80]
    creatureLandFile: common.cTkFixedString[0x80]
    creatureCaveFile: common.cTkFixedString[0x80]
    creatureWaterFile: common.cTkFixedString[0x80]
    creatureExtraWaterFile: common.cTkFixedString[0x80]
    creatureAirFile: common.cTkFixedString[0x80]
    creatureRobotFile: common.cTkFixedString[0x80]
    externalObjectLists: common.cTkDynamicArray[cGcExternalObjectListOptions]
    externalObjectListIndices: common.cTkDynamicArray[ctypes.c_int32]
    prime: bool

cGcPlanetGenerationIntermediateData._fields_ = [
    ("seed", common.GcSeed),
    ("terrainSettingIndex", ctypes.c_int32),
    ("starType", cGcGalaxyStarTypes),
    ("class_", cGcPlanetClass),
    ("size", cGcPlanetSize),
    ("creatureRoles", cGcCreatureRoleDataTable),
    ("terrain", cGcTerrainControls),
    ("biome", cGcBiomeType),
    ("biomeSubType", cGcBiomeSubType),
    ("terrainFile", common.cTkFixedString[0x80]),
    ("creatureLandFile", common.cTkFixedString[0x80]),
    ("creatureCaveFile", common.cTkFixedString[0x80]),
    ("creatureWaterFile", common.cTkFixedString[0x80]),
    ("creatureExtraWaterFile", common.cTkFixedString[0x80]),
    ("creatureAirFile", common.cTkFixedString[0x80]),
    ("creatureRobotFile", common.cTkFixedString[0x80]),
    ("externalObjectLists", common.cTkDynamicArray[cGcExternalObjectListOptions]),
    ("externalObjectListIndices", common.cTkDynamicArray[ctypes.c_int32]),
    ("prime", ctypes.c_ubyte),
]


class cGcPlanetInfo(ctypes.Structure):
    planetDescription: common.cTkFixedString[0x80]
    planetType: common.cTkFixedString[0x80]
    weather: common.cTkFixedString[0x80]
    resources: common.cTkFixedString[0x80]
    flora: common.cTkFixedString[0x80]
    fauna: common.cTkFixedString[0x80]
    sentinels: common.cTkFixedString[0x80]
    isWeatherExtreme: bool
    areSentinelsExtreme: bool
    areSentinelsModerate: bool

cGcPlanetInfo._fields_ = [
    ("planetDescription", common.cTkFixedString[0x80]),
    ("planetType", common.cTkFixedString[0x80]),
    ("weather", common.cTkFixedString[0x80]),
    ("resources", common.cTkFixedString[0x80]),
    ("flora", common.cTkFixedString[0x80]),
    ("fauna", common.cTkFixedString[0x80]),
    ("sentinels", common.cTkFixedString[0x80]),
    ("isWeatherExtreme", ctypes.c_ubyte),
    ("areSentinelsExtreme", ctypes.c_ubyte),
    ("areSentinelsModerate", ctypes.c_ubyte),
]


class cGcPlanetSentinelData(ctypes.Structure):
    _meSentinelLevel: ctypes.c_int32
    maxActiveDrones: int

cGcPlanetSentinelData._fields_ = [
    ("_meSentinelLevel", ctypes.c_int32),
    ("maxActiveDrones", ctypes.c_int32),
]


class cGcPlanetRingData(ctypes.Structure):
    hasRings: bool
    up: common.Vector3f
    colour1: common.Colour
    colour2: common.Colour
    largeScale1: float
    largeScale2: float
    midScale: float
    smallScale: float
    midStrength: float
    offset: float
    depth: float
    alphaMultiplier: float

cGcPlanetRingData._fields_ = [
    ("hasRings", ctypes.c_ubyte),
    ("padding0x1", ctypes.c_ubyte * 0xF),
    ("up", common.Vector3f),
    ("colour1", common.Colour),
    ("colour2", common.Colour),
    ("largeScale1", ctypes.c_float),
    ("largeScale2", ctypes.c_float),
    ("midScale", ctypes.c_float),
    ("smallScale", ctypes.c_float),
    ("midStrength", ctypes.c_float),
    ("offset", ctypes.c_float),
    ("depth", ctypes.c_float),
    ("alphaMultiplier", ctypes.c_float),
]


cGcPlanetData._fields_ = [
    ("name", common.cTkFixedString[0x80]),
    ("life", cGcPlanetLife),
    ("creatureLife", cGcPlanetLife),
    ("hazard", cGcPlanetHazardData),
    ("_meResourceLevel", ctypes.c_int32),
    ("buildingLevel", cGcBuildingDensityLevels),
    ("commonSubstanceID", common.TkID[0x10]),
    ("uncommonSubstanceID", common.TkID[0x10]),
    ("rareSubstanceID", common.TkID[0x10]),
    ("extraResourceHints", common.cTkDynamicArray[cGcPlanetDataResourceHint]),
    ("colours", cGcPlanetColourData),
    ("tileColours", ctypes.c_ubyte * 0x170),
    ("weather", cGcPlanetWeatherData),
    ("clouds", cGcPlanetCloudProperties),
    ("water", cGcPlanetWaterData),
    ("terrainFile", common.cTkFixedString[0x80]),
    ("terrain", cTkVoxelGeneratorData),
    ("tileTypeSet", ctypes.c_int32),
    ("padding0x3564", ctypes.c_ubyte * 0x4),
    ("tileTypeIndices", common.cTkDynamicArray[ctypes.c_int32]),
    ("spawnData", cGcEnvironmentSpawnData),
    ("inhabitingRace", cGcAlienRace),
    ("padding0x35DC", ctypes.c_ubyte * 0x4),
    ("buildingData", cGcPlanetBuildingData),
    ("generationData", cGcPlanetGenerationIntermediateData),
    ("sentinelTimer", common.Vector2f),
    ("flybyTimer", common.Vector2f),
    ("planetInfo", cGcPlanetInfo),
    ("padding0x3E23", ctypes.c_ubyte * 0x1),
    ("sentinelData", cGcPlanetSentinelData),
    ("padding0x3E2C", ctypes.c_ubyte * 0x4),
    ("rings", cGcPlanetRingData),
    ("inEmptySystem", ctypes.c_ubyte),
    ("inAbandonedSystem", ctypes.c_ubyte),
    ("padding0x3E92", ctypes.c_ubyte * 0x2),
    ("fuelMultiplier", ctypes.c_float),
]


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
    ("dummy_PD", ctypes.c_ubyte * (16032 - ctypes.sizeof(cGcPlanetData))),
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


class cGcInventoryElement(ctypes.Structure):
    type: "cGcInventoryType"
    id: common.TkID[0x10]
    amount: int
    maxAmount: int
    damageFactor: float
    fullyInstalled: bool
    index: int

cGcInventoryElement._fields_ = [
    ("type", cGcInventoryType),
    ("padding0x4", ctypes.c_ubyte * 0x4),
    ("id", common.TkID[0x10]),
    ("amount", ctypes.c_int32),
    ("maxAmount", ctypes.c_int32),
    ("damageFactor", ctypes.c_float),
    ("fullyInstalled", ctypes.c_ubyte),
    ("padding0x25", ctypes.c_ubyte * 0x3),
    ("index", ctypes.c_uint64),
]


class cGcInventorySpecialSlotType(ctypes.Structure):
    _meInventorySpecialSlotType: ctypes.c_int32

cGcInventorySpecialSlotType._fields_ = [
    ("_meInventorySpecialSlotType", ctypes.c_int32),
]


class cGcInventoryIndex(ctypes.Structure):
    X: int
    Y: int

cGcInventoryIndex._fields_ = [
    ("X", ctypes.c_int32),
    ("Y", ctypes.c_int32),
]


class cGcInventorySpecialSlot(ctypes.Structure):
    type: "cGcInventorySpecialSlotType"
    index: "cGcInventoryIndex"

cGcInventorySpecialSlot._fields_ = [
    ("type", cGcInventorySpecialSlotType),
    ("index", cGcInventoryIndex),
]


class cGcInventoryBaseStatEntry(ctypes.Structure):
    baseStatID: common.TkID[0x10]
    value: float

cGcInventoryBaseStatEntry._fields_ = [
    ("baseStatID", common.TkID[0x10]),
    ("value", ctypes.c_float),
]


class cGcInventoryLayout(ctypes.Structure):
    slots: int
    seed: common.GcSeed
    level: int

cGcInventoryLayout._fields_ = [
    ("slots", ctypes.c_int32),
    ("padding0x4", ctypes.c_ubyte * 0x4),
    ("seed", common.GcSeed),
    ("level", ctypes.c_int32),
    ("endpadding", ctypes.c_ubyte * 0x8),
]


class cGcInventoryClass(ctypes.Structure):
    _meInventoryClass: ctypes.c_int32

cGcInventoryClass._fields_ = [
    ("_meInventoryClass", ctypes.c_int32),
]


class cGcInventoryStore(ctypes.Structure):
    validSlots: bytes
    width: int
    height: int
    capacity: int
    store: std.vector[cGcInventoryElement]
    storeHistory: std.vector[cGcInventoryElement]
    specialSlots: std.vector[cGcInventorySpecialSlot]
    baseStats: std.vector[cGcInventoryBaseStatEntry]
    layoutDescriptor: "cGcInventoryLayout"
    autoMaxEnabled: bool
    isCool: bool
    _meStackSizeGroup: ctypes.c_int32
    class_: "cGcInventoryClass"
    inventoryName: common.cTkFixedString[0x100]
    techGroupCounts: bytes

cGcInventoryStore._fields_ = [
    ("validSlots", ctypes.c_ubyte * 0x80),
    ("width", ctypes.c_int16),
    ("height", ctypes.c_int16),
    ("capacity", ctypes.c_int16),
    ("padding0x86", ctypes.c_ubyte * 0x2),
    ("store", std.vector[cGcInventoryElement]),
    ("storeHistory", std.vector[cGcInventoryElement]),
    ("specialSlots", std.vector[cGcInventorySpecialSlot]),
    ("baseStats", std.vector[cGcInventoryBaseStatEntry]),
    ("layoutDescriptor", cGcInventoryLayout),
    ("autoMaxEnabled", ctypes.c_ubyte),
    ("isCool", ctypes.c_ubyte),
    ("padding0x10A", ctypes.c_ubyte * 0x2),
    ("_meStackSizeGroup", ctypes.c_int32),
    ("class_", cGcInventoryClass),
    ("inventoryName", common.cTkFixedString[0x100]),
    ("padding0x214", ctypes.c_ubyte * 0x4),
    ("techGroupCounts", ctypes.c_ubyte * 0x40),
]


class IStatWatcher_vtbl(ctypes.Structure):
    StatChanged: bytes
    StatChanged_8: bytes

IStatWatcher_vtbl._fields_ = [
    ("StatChanged", ctypes.c_ubyte * 0x8),
    ("StatChanged_8", ctypes.c_ubyte * 0x8),
]


class IStatWatcher(ctypes.Structure):
    __vftable: _Pointer["IStatWatcher_vtbl"]

IStatWatcher._fields_ = [
    ("__vftable", ctypes.POINTER(IStatWatcher_vtbl)),
]


class sPlayerTitleStatWatcher(IStatWatcher, ctypes.Structure):
    statIdMap: bytes

sPlayerTitleStatWatcher._fields_ = [
    ("statIdMap", ctypes.c_ubyte * 0x40),
]


class cGcExactResource(ctypes.Structure):
    filename: common.cTkFixedString[0x80]
    generationSeed: common.GcSeed

cGcExactResource._fields_ = [
    ("filename", common.cTkFixedString[0x80]),
    ("generationSeed", common.GcSeed),
]


class cGcInventoryStackSizeGroup(ctypes.Structure):
    _meInventoryStackSizeGroup: ctypes.c_int32

cGcInventoryStackSizeGroup._fields_ = [
    ("_meInventoryStackSizeGroup", ctypes.c_int32),
]


class cGcInventoryContainer(ctypes.Structure):
    slots: common.cTkDynamicArray[cGcInventoryElement]
    validSlotIndices: common.cTkDynamicArray[ctypes.c_uint64]
    class_: "cGcInventoryClass"
    stackSizeGroup: "cGcInventoryStackSizeGroup"
    baseStatValues: common.cTkDynamicArray[cGcInventoryBaseStatEntry]
    specialSlots: common.cTkDynamicArray[cGcInventorySpecialSlot]
    width: int
    height: int
    isCool: bool
    name: common.cTkFixedString[0x100]
    version: int

cGcInventoryContainer._fields_ = [
    ("slots", common.cTkDynamicArray[cGcInventoryElement]),
    ("validSlotIndices", common.cTkDynamicArray[ctypes.c_uint64]),
    ("class_", cGcInventoryClass),
    ("stackSizeGroup", cGcInventoryStackSizeGroup),
    ("baseStatValues", common.cTkDynamicArray[cGcInventoryBaseStatEntry]),
    ("specialSlots", common.cTkDynamicArray[cGcInventorySpecialSlot]),
    ("width", ctypes.c_int32),
    ("height", ctypes.c_int32),
    ("isCool", ctypes.c_ubyte),
    ("name", common.cTkFixedString[0x100]),
    ("padding0x151", ctypes.c_ubyte * 0x3),
    ("version", ctypes.c_int32),
]


class cGcMaintenanceContainer(ctypes.Structure):
    inventoryContainer: "cGcInventoryContainer"
    lastUpdateTimestamp: int
    lastCompletedTimestamp: int
    lastBrokenTimestamp: int
    damageTimers: common.cTkDynamicArray[ctypes.c_float]
    amountAccumulators: common.cTkDynamicArray[ctypes.c_float]
    flags: int

cGcMaintenanceContainer._fields_ = [
    ("inventoryContainer", cGcInventoryContainer),
    ("lastUpdateTimestamp", ctypes.c_uint64),
    ("lastCompletedTimestamp", ctypes.c_uint64),
    ("lastBrokenTimestamp", ctypes.c_uint64),
    ("damageTimers", common.cTkDynamicArray[ctypes.c_float]),
    ("amountAccumulators", common.cTkDynamicArray[ctypes.c_float]),
    ("flags", ctypes.c_uint16),
]


class LogBookMessage(ctypes.Structure):
    timeStamp: int
    logMessage: common.cTkFixedString[0x80]

LogBookMessage._fields_ = [
    ("timeStamp", ctypes.c_int32),
    ("logMessage", common.cTkFixedString[0x80]),
]


class cGcRepairTechData(ctypes.Structure):
    maintenanceContainer: "cGcMaintenanceContainer"
    inventoryType: int
    inventorySubIndex: int
    inventoryIndex: cGcInventoryIndex

cGcRepairTechData._fields_ = [
    ("maintenanceContainer", cGcMaintenanceContainer),
    ("inventoryType", ctypes.c_int32),
    ("inventorySubIndex", ctypes.c_int32),
    ("inventoryIndex", cGcInventoryIndex),
]


class cGcPlayerLogBook(ctypes.Structure):
    playerLogs: std.vector[LogBookMessage]

cGcPlayerLogBook._fields_ = [
    ("playerLogs", std.vector[LogBookMessage]),
]


class cGcWordGroupKnowledge(ctypes.Structure):
    group: common.TkID[0x20]
    races: list[bool]

cGcWordGroupKnowledge._fields_ = [
    ("group", common.TkID[0x20]),
    ("races", ctypes.c_ubyte * 0x8),
]


class cGcSavedEntitlement(ctypes.Structure):
    entitlementId: common.cTkFixedString[0x100]

cGcSavedEntitlement._fields_ = [
    ("entitlementId", common.cTkFixedString[0x100]),
]


class cGcPhotoModeSettings(ctypes.Structure):
    fog: float
    cloudAmount: float
    sunDir: common.Vector4f
    foV: float
    _meDepthOfFieldSetting: ctypes.c_int32
    depthOfFieldDistance: float
    depthOfFieldDistanceSpace: float
    halfFocalPlaneDepth: float
    halfFocalPlaneDepthSpace: float
    depthOfFieldPhysConvergence: float
    depthOfFieldPhysAperture: float
    vignette: float
    filter: int
    bloom: float

cGcPhotoModeSettings._fields_ = [
    ("fog", ctypes.c_float),
    ("cloudAmount", ctypes.c_float),
    ("padding0x8", ctypes.c_ubyte * 0x8),
    ("sunDir", common.Vector4f),
    ("foV", ctypes.c_float),
    ("_meDepthOfFieldSetting", ctypes.c_int32),
    ("depthOfFieldDistance", ctypes.c_float),
    ("depthOfFieldDistanceSpace", ctypes.c_float),
    ("halfFocalPlaneDepth", ctypes.c_float),
    ("halfFocalPlaneDepthSpace", ctypes.c_float),
    ("depthOfFieldPhysConvergence", ctypes.c_float),
    ("depthOfFieldPhysAperture", ctypes.c_float),
    ("vignette", ctypes.c_float),
    ("filter", ctypes.c_int32),
    ("bloom", ctypes.c_float),
    ("endpadding", ctypes.c_ubyte * 0x4),
]


class cGcTeleportEndpoint(ctypes.Structure):
    universeAddress: "cGcUniverseAddressData"
    position: common.Vector3f
    facing: common.Vector3f
    _meTeleporterType: ctypes.c_int32
    name: common.cTkFixedString[0x40]
    calcWarpOffset: bool
    isFeatured: bool

cGcTeleportEndpoint._fields_ = [
    ("universeAddress", cGcUniverseAddressData),
    ("padding0x18", ctypes.c_ubyte * 0x8),
    ("position", common.Vector3f),
    ("facing", common.Vector3f),
    ("_meTeleporterType", ctypes.c_int32),
    ("name", common.cTkFixedString[0x40]),
    ("calcWarpOffset", ctypes.c_ubyte),
    ("isFeatured", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0xA),
]


class BaseIndex(ctypes.Structure):
    value: int

BaseIndex._fields_ = [
    ("value", ctypes.c_uint16),
]


class cGcPlayerNPCWorkers(ctypes.Structure):
    class WorkerStationInfo(ctypes.Structure):
        workerHired: bool
        workerIndex: "BaseIndex"
        workerResourceData: "cGcResourceElement"
        nPCInteractionSeed: common.GcSeed

    WorkerStationInfo._fields_ = [
        ("workerHired", ctypes.c_ubyte),
        ("padding0x1", ctypes.c_ubyte * 0x1),
        ("workerIndex", BaseIndex),
        ("padding0x4", ctypes.c_ubyte * 0x4),
        ("workerResourceData", cGcResourceElement),
        ("nPCInteractionSeed", common.GcSeed),
    ]


    workerStations: list[cGcPlayerNPCWorkers.WorkerStationInfo]

cGcPlayerNPCWorkers._fields_ = [
    ("workerStations", cGcPlayerNPCWorkers.WorkerStationInfo * 0x5),
]


class cGcInteractionData(ctypes.Structure):
    galacticAddress: int
    value: int
    position: common.Vector4f

cGcInteractionData._fields_ = [
    ("galacticAddress", ctypes.c_uint64),
    ("value", ctypes.c_uint64),
    ("position", common.Vector4f),
]


class cGcPortalSaveData(ctypes.Structure):
    portalSeed: common.GcSeed
    lastPortalUA: int
    isStoryPortal: bool

cGcPortalSaveData._fields_ = [
    ("portalSeed", common.GcSeed),
    ("lastPortalUA", ctypes.c_uint64),
    ("isStoryPortal", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0x7)
]


class cGcPlayerBanner(ctypes.Structure):
    iconIndex: int
    mainColourIndex: int
    backgroundColourIndex: int
    _meShipClass: ctypes.c_int32
    titleId: common.TkID[0x10]

cGcPlayerBanner._fields_ = [
    ("iconIndex", ctypes.c_uint8),
    ("mainColourIndex", ctypes.c_uint8),
    ("backgroundColourIndex", ctypes.c_uint8),
    ("padding0x3", ctypes.c_ubyte * 0x1),
    ("_meShipClass", ctypes.c_int32),
    ("titleId", common.TkID[0x10]),
]


class cGcSeasonSaveStateOnDeath(ctypes.Structure):
    _meSeasonSaveStateOnDeath: ctypes.c_int32

cGcSeasonSaveStateOnDeath._fields_ = [
    ("_meSeasonSaveStateOnDeath", ctypes.c_int32),
]


class cGcSeasonState(ctypes.Structure):
    class sSeasonalMilestoneProgress(ctypes.Structure):
        stageIndex: int
        milestoneIndex: int
        currentValue: float
        unitProgress: float
        rewardFitsInInventory: bool
        rewardCollected: bool
        revealed: bool
        visible: bool

    sSeasonalMilestoneProgress._fields_ = [
        ("stageIndex", ctypes.c_int32),
        ("milestoneIndex", ctypes.c_int32),
        ("currentValue", ctypes.c_float),
        ("unitProgress", ctypes.c_float),
        ("rewardFitsInInventory", ctypes.c_ubyte),
        ("rewardCollected", ctypes.c_ubyte),
        ("revealed", ctypes.c_ubyte),
        ("visible", ctypes.c_ubyte),
    ]


    class sSeasonalStageProgress(ctypes.Structure):
        milestones: std.vector[cGcSeasonState.sSeasonalMilestoneProgress]
        progress: float


    class sPinnedMilestone(ctypes.Structure):
        stageIndex: int
        milestoneIndex: int

    sPinnedMilestone._fields_ = [
        ("stageIndex", ctypes.c_int32),
        ("milestoneIndex", ctypes.c_int32),
    ]


    class sPendingMilestoneReward(ctypes.Structure):
        stageIndex: int
        milestoneIndex: int

    sPendingMilestoneReward._fields_ = [
        ("stageIndex", ctypes.c_int32),
        ("milestoneIndex", ctypes.c_int32),
    ]


    class sSeasonInitialBuilding(ctypes.Structure):
        position: common.Vector3f
        seed: common.GcSeed
        radius: float

    sSeasonInitialBuilding._fields_ = [
        ("position", common.Vector3f),
        ("seed", common.GcSeed),
        ("radius", ctypes.c_float),
    ]


    class sBuildingPreventionArea(ctypes.Structure):
        position: common.Vector3f
        radius: float

    sBuildingPreventionArea._fields_ = [
        ("position", common.Vector3f),
        ("radius", ctypes.c_float),
    ]


    stageProgress: std.vector[cGcSeasonState.sSeasonalStageProgress]
    pinnedMilestone: "cGcSeasonState.sPinnedMilestone"
    pendingMilestoneReward: "cGcSeasonState.sPendingMilestoneReward"
    rendezvousUAs: std.vector[ctypes.c_uint64]
    initialBuildings: std.vector[cGcSeasonState.sSeasonInitialBuilding]
    buildingPreventionAreas: bytes
    stateOnDeath: "cGcSeasonSaveStateOnDeath"
    replacedTechnologies: std.vector[cGcTechnology]
    replacedProducts: std.vector[cGcProductData]
    replacedSubstances: std.vector[bytes]
    wantToUpdateRewardAvailability: bool
    hasCollectedFinalReward: bool
    finalRewardFitsInInventory: bool

cGcSeasonState.sSeasonalStageProgress._fields_ = [
    ("milestones", std.vector[cGcSeasonState.sSeasonalMilestoneProgress]),
    ("progress", ctypes.c_float),
]

cGcSeasonState._fields_ = [
    ("stageProgress", std.vector[cGcSeasonState.sSeasonalStageProgress]),
    ("pinnedMilestone", cGcSeasonState.sPinnedMilestone),
    ("pendingMilestoneReward", cGcSeasonState.sPendingMilestoneReward),
    ("rendezvousUAs", std.vector[ctypes.c_uint64]),
    ("initialBuildings", std.vector[cGcSeasonState.sSeasonInitialBuilding]),
    ("buildingPreventionAreas", ctypes.c_ubyte * 0x40),
    ("stateOnDeath", cGcSeasonSaveStateOnDeath),
    ("padding0x9C", ctypes.c_ubyte * 0x4),
    ("replacedTechnologies", std.vector[cGcTechnology]),
    ("replacedProducts", std.vector[cGcProductData]),
    ("replacedSubstances", std.vector[ctypes.c_ubyte]),  # cGcRealitySubstanceData
    ("wantToUpdateRewardAvailability", ctypes.c_ubyte),
    ("hasCollectedFinalReward", ctypes.c_ubyte),
    ("finalRewardFitsInInventory", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0x5)
]


class cGcPlayerState(ctypes.Structure):
    class ItemEvent(ctypes.Structure):
        id: common.TkID[0x10]
        time: float

    ItemEvent._fields_ = [
        ("id", common.TkID[0x10]),
        ("time", ctypes.c_float),
        ("endpadding", ctypes.c_ubyte * 0x4),
    ]


    class InventoryChoiceMap(ctypes.Structure):
        store: _Pointer["cGcInventoryStore"]
        choice: bytes

    InventoryChoiceMap._fields_ = [
        ("store", ctypes.POINTER(cGcInventoryStore)),
        ("choice", ctypes.c_ubyte * 0x4),
    ]


    class SavedRaceInteractions(ctypes.Structure):
        forRace: bytes

    SavedRaceInteractions._fields_ = [
        ("forRace", ctypes.c_ubyte * 0x20),
    ]


    nameWithTitle: common.cTkFixedString[0x100]
    titleStatWatcher: "sPlayerTitleStatWatcher"
    changeRevision: int
    gameStartLocation1: "cGcUniverseAddressData"
    gameStartLocation2: "cGcUniverseAddressData"
    location: "cGcUniverseAddressData"
    prevLocation: "cGcUniverseAddressData"
    shield: int
    health: int
    shipHealth: int
    units: int
    nanites: int
    specials: int
    restoreHazardTimers: bytes
    restoreShield: int
    restoreHealth: int
    restoreShipShield: int
    restoreShipHealth: int
    restoreEnergy: int
    weaponResource: "cGcExactResource"
    inventories: bytes
    shelvedInventories: std.vector[cGcInventoryStore]
    vehicleInventories: bytes
    vehicleTechInventories: bytes
    vehicleLocations: bytes
    _mePrimaryVehicle: ctypes.c_int32
    shipInventories: bytes
    shelvedShipInventories: std.vector[cGcInventoryStore]
    shipInventoriesCargo: bytes
    shipInventoriesTechOnly: bytes
    shipResources: bytes
    primaryShip: int
    repairTechBuffer: std.vector[cGcRepairTechData]
    surveyedEventPositions: std.vector[common.Vector3f]
    playerLog: "cGcPlayerLogBook"
    seenBaseBuildingObjects: bytes
    knownTechnologies: std.vector[common.TkID[0x10]]
    knownProducts: std.vector[common.TkID[0x10]]
    knownRefinerRecipes: std.vector[common.TkID[0x20]]
    knownWordGroups: std.vector[cGcWordGroupKnowledge]
    totalPlayTime: int
    timeAlive: int
    timeAccumulator: float
    hazardTimeAlive: int
    hazardTimeAccumulator: float
    lastInventoryStoreTime: float
    lastInventoryFailTime: float
    procTechIndex: int
    savedInteractionIndicies: bytes
    interactionLookupTable: std.vector[common.TkID[0x20]]
    defaultSuitLoadout: std.vector[cGcInventoryElement]
    defaultWeaponLoadout: std.vector[cGcInventoryElement]
    defaultShipLoadout: std.vector[cGcInventoryElement]
    graveInventory: std.vector[cGcInventoryElement]
    graveLocation: "cGcUniverseAddressData"
    graveMatrix: common.cTkMatrix34
    spawnGrave: bool
    spaceGrave: bool
    pendingBootSpawnGrave: bool
    atlasStationLocations: std.vector[cGcUniverseAddressData]
    interactionDialogMap: bytes
    firstAtlasStationDiscovered: bool
    usesThirdPersonCharacterCam: bool
    initialSpawnPosition: common.Vector4f
    initialShipPosition: common.Vector4f
    progressionLevel: int
    activeBattleUA: int
    lastBuiltProduct: "cGcPlayerState.ItemEvent"
    lastBuiltTech: "cGcPlayerState.ItemEvent"
    lastRepairedTech: "cGcPlayerState.ItemEvent"
    slots: int
    level: int
    maxTechValue: int
    maxTechs: int
    fillAllSlots: bool
    warpFromBlackHole: bool
    revealBlackHoles: bool
    warpFromRelicGate: bool
    warpFromFreighterMegaWarp: bool
    useSmallerBlackholeJumps: bool
    isDataNew: bool
    usedEntitlements: std.vector[cGcSavedEntitlement]
    lastSpaceBattleTime: int
    lastSpaceBattleWarps: int
    lastMiniStationTime: int
    lastMiniStationWarps: int
    miniStationLocation: int
    anomalyPositionOverride: common.Vector3f
    photoModeSettings: "cGcPhotoModeSettings"
    teleportEndpoints: std.vector[cGcTeleportEndpoint]
    playerNPCWorkers: "cGcPlayerNPCWorkers"
    holoExplorerInteraction: "cGcInteractionData"
    holoScepticInteraction: "cGcInteractionData"
    holoNooneInteraction: "cGcInteractionData"
    networkPlayerInteraction: "cGcInteractionData"
    startGameShipPosition: common.Vector4f
    shipNeedsTerrainPositioning: bool
    customWeaponName: common.cTkFixedString[0x20]
    customShipNames: bytes
    customVehicleNames: bytes
    lastPortals: std.vector[cGcPortalSaveData]
    lastPortal: "cGcPortalSaveData"
    knownPortalRunes: int
    onOtherSideOfPortal: bool
    otherSideOfPortalReturnBase: "cGcTeleportEndpoint"
    portalMarkerPosition: common.cTkPhysRelVec3
    lastUABeforePortalWarp: int
    activeStoryPortalSeed: int
    previousMission: bytes
    currentMission: bytes
    _meStartingPrimaryWeapon: ctypes.c_int32
    _meStartingSecondaryWeapon: ctypes.c_int32
    vRCameraOffset: float
    thirdPersonShipCam: bool
    thirdPersonVehicleCam: bool
    nextLoadSpawnsWithFreshStart: bool
    initialised: bool
    vehicleAIControlEnabled: bool
    hasAccessToNexus: bool
    nexusUniverseLocation: "cGcUniverseAddressData"
    nexusSavedMatrix: common.cTkMatrix34
    customisationData: bytes
    outfits: bytes
    seenStoriesData: bytes
    jetpackEffect: common.TkID[0x10]
    playerBanner: "cGcPlayerBanner"
    seasonState: "cGcSeasonState"
    redeemedSpecials: bytes
    redeemedSeasonRewards: bytes
    redeemedTwitchRewards: bytes
    redeemedPlatformRewards: bytes
    pendingRewardId: common.TkID[0x10]
    hasPendingRewardFromSeason: bool
    hasPendingRewardFromTwitch: bool
    hasPendingRewardFromPlatform: bool
    _meFinalisePurchaseState: ctypes.c_int32
    settlementStates: bytes
    settlementStateRingBufferIndex: int
    saveName: common.cTkFixedString[0x80]
    saveSummary: common.cTkFixedString[0x80]
    # deathReward: _Pointer["cGcRewardDeath"]
    # characterCustomisationDescriptorGroups: _Pointer["cGcCustomisationDescriptorGroups"]
    # characterCustomisationTextureOptions: _Pointer["cGcCustomisationTextureOptions"]
    # characterCustomisationPresets: _Pointer["cGcCustomisationPresets"]
    # customisationColourPalettes: _Pointer["cGcCustomisationColourPalettes"]
    # customisationBannerData: _Pointer["cGcCustomisationBannerGroup"]
    # customisationThrusterData: _Pointer["cGcCustomisationThrusterEffects"]
    # customisationShipBobbleHeads: _Pointer["cGcCustomisationShipBobbleHeads"]

cGcPlayerState._fields_ = [
    ("nameWithTitle", common.cTkFixedString[0x100]),
    ("titleStatWatcher", sPlayerTitleStatWatcher),
    ("changeRevision", ctypes.c_uint64),
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
    ("restoreHazardTimers", ctypes.c_ubyte * 0x18),
    ("restoreShield", ctypes.c_int32),
    ("restoreHealth", ctypes.c_int32),
    ("restoreShipShield", ctypes.c_int32),
    ("restoreShipHealth", ctypes.c_int32),
    ("restoreEnergy", ctypes.c_int32),
    ("padding0x1F4", ctypes.c_ubyte * 0x4),
    ("weaponResource", cGcExactResource),
    ("inventories", ctypes.c_ubyte * 0x41A0),
    ("shelvedInventories", std.vector[cGcInventoryStore]),
    ("vehicleInventories", ctypes.c_ubyte * 0x1068),
    ("vehicleTechInventories", ctypes.c_ubyte * 0x1068),
    ("vehicleLocations", ctypes.c_ubyte * 0x150),
    ("_mePrimaryVehicle", ctypes.c_int32),
    ("padding0x6664", ctypes.c_ubyte * 0x4),
    ("shipInventories", ctypes.c_ubyte * 0x1C20),
    ("shelvedShipInventories", std.vector[cGcInventoryStore]),
    ("shipInventoriesCargo", ctypes.c_ubyte * 0x1C20),
    ("shipInventoriesTechOnly", ctypes.c_ubyte * 0x1C20),
    ("shipResources", ctypes.c_ubyte * 0x1FE0),
    ("primaryShip", ctypes.c_int32),
    ("padding0xDAC4", ctypes.c_ubyte * 0x4),
    ("repairTechBuffer", std.vector[cGcRepairTechData]),
    ("surveyedEventPositions", std.vector[common.Vector3f]),
    ("playerLog", cGcPlayerLogBook),
    ("seenBaseBuildingObjects", ctypes.c_ubyte * 0x40),
    ("knownTechnologies", std.vector[common.TkID[0x10]]),
    ("knownProducts", std.vector[common.TkID[0x10]]),
    ("knownRefinerRecipes", std.vector[common.TkID[0x20]]),
    ("knownWordGroups", std.vector[cGcWordGroupKnowledge]),
    ("totalPlayTime", ctypes.c_uint64),
    ("timeAlive", ctypes.c_uint64),
    ("timeAccumulator", ctypes.c_float),
    ("padding0xDBC4", ctypes.c_ubyte * 0x4),
    ("hazardTimeAlive", ctypes.c_uint64),
    ("hazardTimeAccumulator", ctypes.c_float),
    ("lastInventoryStoreTime", ctypes.c_float),
    ("lastInventoryFailTime", ctypes.c_float),
    ("procTechIndex", ctypes.c_int32),
    ("savedInteractionIndicies", ctypes.c_ubyte * 0x1478),
    ("interactionLookupTable", std.vector[common.TkID[0x20]]),
    ("defaultSuitLoadout", std.vector[cGcInventoryElement]),
    ("defaultWeaponLoadout", std.vector[cGcInventoryElement]),
    ("defaultShipLoadout", std.vector[cGcInventoryElement]),
    ("graveInventory", std.vector[cGcInventoryElement]),
    ("graveLocation", cGcUniverseAddressData),
    ("padding0xF0E8", ctypes.c_ubyte * 0x8),
    ("graveMatrix", common.cTkMatrix34),
    ("spawnGrave", ctypes.c_ubyte),
    ("spaceGrave", ctypes.c_ubyte),
    ("pendingBootSpawnGrave", ctypes.c_ubyte),
    ("padding0xF133", ctypes.c_ubyte * 0x5),
    ("atlasStationLocations", std.vector[cGcUniverseAddressData]),
    ("interactionDialogMap", ctypes.c_ubyte * 0x28),
    ("firstAtlasStationDiscovered", ctypes.c_ubyte),
    ("usesThirdPersonCharacterCam", ctypes.c_ubyte),
    ("padding0xF17A", ctypes.c_ubyte * 0x6),
    ("initialSpawnPosition", common.Vector4f),
    ("initialShipPosition", common.Vector4f),
    ("progressionLevel", ctypes.c_int32),
    ("padding0xF1A4", ctypes.c_ubyte * 0x4),
    ("activeBattleUA", ctypes.c_uint64),
    ("lastBuiltProduct", cGcPlayerState.ItemEvent),
    ("lastBuiltTech", cGcPlayerState.ItemEvent),
    ("lastRepairedTech", cGcPlayerState.ItemEvent),
    ("slots", ctypes.c_int32),
    ("level", ctypes.c_int32),
    ("maxTechValue", ctypes.c_int32),
    ("maxTechs", ctypes.c_int32),
    ("fillAllSlots", ctypes.c_ubyte),
    ("warpFromBlackHole", ctypes.c_ubyte),
    ("revealBlackHoles", ctypes.c_ubyte),
    ("warpFromRelicGate", ctypes.c_ubyte),
    ("warpFromFreighterMegaWarp", ctypes.c_ubyte),
    ("useSmallerBlackholeJumps", ctypes.c_ubyte),
    ("isDataNew", ctypes.c_ubyte),
    ("padding0xF20F", ctypes.c_ubyte * 0x1),
    ("usedEntitlements", std.vector[cGcSavedEntitlement]),
    ("lastSpaceBattleTime", ctypes.c_uint64),
    ("lastSpaceBattleWarps", ctypes.c_int32),
    ("padding0xF234", ctypes.c_ubyte * 0x4),
    ("lastMiniStationTime", ctypes.c_uint64),
    ("lastMiniStationWarps", ctypes.c_int32),
    ("padding0xF244", ctypes.c_ubyte * 0x4),
    ("miniStationLocation", ctypes.c_uint64),
    ("anomalyPositionOverride", common.Vector3f),
    ("photoModeSettings", cGcPhotoModeSettings),
    ("teleportEndpoints", std.vector[cGcTeleportEndpoint]),
    ("playerNPCWorkers", cGcPlayerNPCWorkers),
    ("padding0x10088", ctypes.c_ubyte * 0x8),
    ("holoExplorerInteraction", cGcInteractionData),
    ("holoScepticInteraction", cGcInteractionData),
    ("holoNooneInteraction", cGcInteractionData),
    ("networkPlayerInteraction", cGcInteractionData),
    ("startGameShipPosition", common.Vector4f),
    ("shipNeedsTerrainPositioning", ctypes.c_ubyte),
    ("customWeaponName", common.cTkFixedString[0x20]),
    ("customShipNames", ctypes.c_ubyte * 0x180),
    ("customVehicleNames", ctypes.c_ubyte * 0xE0),
    ("padding0x103A1", ctypes.c_ubyte * 0x7),
    ("lastPortals", std.vector[cGcPortalSaveData]),
    ("lastPortal", cGcPortalSaveData),
    ("knownPortalRunes", ctypes.c_int32),
    ("onOtherSideOfPortal", ctypes.c_ubyte),
    ("padding0x103E5", ctypes.c_ubyte * 0xB),
    ("otherSideOfPortalReturnBase", cGcTeleportEndpoint),
    ("portalMarkerPosition", common.cTkPhysRelVec3),
    ("lastUABeforePortalWarp", ctypes.c_uint64),
    ("activeStoryPortalSeed", ctypes.c_uint64),
    ("previousMission", ctypes.c_ubyte * 0x20),
    ("currentMission", ctypes.c_ubyte * 0x20),
    ("_meStartingPrimaryWeapon", ctypes.c_int32),
    ("_meStartingSecondaryWeapon", ctypes.c_int32),
    ("vRCameraOffset", ctypes.c_float),
    ("thirdPersonShipCam", ctypes.c_ubyte),
    ("thirdPersonVehicleCam", ctypes.c_ubyte),
    ("nextLoadSpawnsWithFreshStart", ctypes.c_ubyte),
    ("initialised", ctypes.c_ubyte),
    ("vehicleAIControlEnabled", ctypes.c_ubyte),
    ("hasAccessToNexus", ctypes.c_ubyte),
    ("padding0x10502", ctypes.c_ubyte * 0x2),
    ("nexusUniverseLocation", cGcUniverseAddressData),
    ("padding0x1051C", ctypes.c_ubyte * 0x4),
    ("nexusSavedMatrix", common.cTkMatrix34),
    ("customisationData", ctypes.c_ubyte * 0x4A4D0),
    ("outfits", ctypes.c_ubyte * 0x9B10),
    ("seenStoriesData", ctypes.c_ubyte * 0x80),
    ("jetpackEffect", common.TkID[0x10]),
    ("playerBanner", cGcPlayerBanner),
    ("seasonState", cGcSeasonState),
    ("redeemedSpecials", ctypes.c_ubyte * 0x40),
    ("redeemedSeasonRewards", ctypes.c_ubyte * 0x40),
    ("redeemedTwitchRewards", ctypes.c_ubyte * 0x40),
    ("redeemedPlatformRewards", ctypes.c_ubyte * 0x40),
    ("pendingRewardId", common.TkID[0x10]),
    ("hasPendingRewardFromSeason", ctypes.c_ubyte),
    ("hasPendingRewardFromTwitch", ctypes.c_ubyte),
    ("hasPendingRewardFromPlatform", ctypes.c_ubyte),
    ("padding0x647EB", ctypes.c_ubyte * 0x1),
    ("_meFinalisePurchaseState", ctypes.c_int32),
    ("settlementStates", ctypes.c_ubyte * 0x1F400),
    ("settlementStateRingBufferIndex", ctypes.c_int32),
    ("saveName", common.cTkFixedString[0x80]),
    ("saveSummary", common.cTkFixedString[0x80]),
    ("padding0x83CF4", ctypes.c_ubyte * 0x4),
    # ("deathReward", ctypes.POINTER(cGcRewardDeath)),
    # ("characterCustomisationDescriptorGroups", ctypes.POINTER(cGcCustomisationDescriptorGroups)),
    # ("characterCustomisationTextureOptions", ctypes.POINTER(cGcCustomisationTextureOptions)),
    # ("characterCustomisationPresets", ctypes.POINTER(cGcCustomisationPresets)),
    # ("customisationColourPalettes", ctypes.POINTER(cGcCustomisationColourPalettes)),
    # ("customisationBannerData", ctypes.POINTER(cGcCustomisationBannerGroup)),
    # ("customisationThrusterData", ctypes.POINTER(cGcCustomisationThrusterEffects)),
    # ("customisationShipBobbleHeads", ctypes.POINTER(cGcCustomisationShipBobbleHeads)),
]


class cGcRpcCallBase_vtbl(ctypes.Structure):
    cGcRpcCallBase_dtor_0: bytes
    Update: bytes
    ProcessRemoteCall: bytes
    ProcessResponse: bytes

cGcRpcCallBase_vtbl._fields_ = [
    ("cGcRpcCallBase_dtor_0", ctypes.c_ubyte * 0x8),
    ("Update", ctypes.c_ubyte * 0x8),
    ("ProcessRemoteCall", ctypes.c_ubyte * 0x8),
    ("ProcessResponse", ctypes.c_ubyte * 0x8),
]


class cGcRpcCallBase(ctypes.Structure):
    __vftable: _Pointer["cGcRpcCallBase_vtbl"]
    ID: int

cGcRpcCallBase._fields_ = [
    ("__vftable", ctypes.POINTER(cGcRpcCallBase_vtbl)),
    ("ID", ctypes.c_uint32),  # cGcNetworkRpcId
]


class cGcPlayerSpawnStateData(ctypes.Structure):
    playerPositionInSystem: common.Vector4f
    playerTransformAt: common.Vector4f
    playerDeathRespawnPositionInSystem: common.Vector4f
    playerDeathRespawnTransformAt: common.Vector4f
    shipPositionInSystem: common.Vector4f
    shipTransformAt: common.Vector4f
    _meLastKnownPlayerState: ctypes.c_int32
    freighterPositionInSystem: common.Vector4f
    freighterTransformAt: common.Vector4f
    freighterTransformUp: common.Vector4f
    abandonedFreighterPositionInSystem: common.Vector4f
    abandonedFreighterTransformAt: common.Vector4f
    abandonedFreighterTransformUp: common.Vector4f

cGcPlayerSpawnStateData._fields_ = [
    ("playerPositionInSystem", common.Vector4f),
    ("playerTransformAt", common.Vector4f),
    ("playerDeathRespawnPositionInSystem", common.Vector4f),
    ("playerDeathRespawnTransformAt", common.Vector4f),
    ("shipPositionInSystem", common.Vector4f),
    ("shipTransformAt", common.Vector4f),
    ("_meLastKnownPlayerState", ctypes.c_int32),
    ("padding0x64", ctypes.c_ubyte * 0xC),
    ("freighterPositionInSystem", common.Vector4f),
    ("freighterTransformAt", common.Vector4f),
    ("freighterTransformUp", common.Vector4f),
    ("abandonedFreighterPositionInSystem", common.Vector4f),
    ("abandonedFreighterTransformAt", common.Vector4f),
    ("abandonedFreighterTransformUp", common.Vector4f),
]


class cGcCustomisationComponentData(ctypes.Structure):
    _meCustomisationDataType: ctypes.c_int32

cGcCustomisationComponentData._fields_ = [
    ("_meCustomisationDataType", ctypes.c_int32),
]


class cGcPlayerShipOwnership(ctypes.Structure):
    class sGcShipData(ctypes.Structure):
        playerShipSeed: common.GcSeed
        playerShipResHandle: common.cTkSmartResHandle
        playerShipNode: common.TkHandle
        playerShipAttachment: int
        freighterDockIndex: int
        shipCustomisationData: "cGcCustomisationComponentData"

    sGcShipData._fields_ = [
        ("playerShipSeed", common.GcSeed),
        ("playerShipResHandle", common.cTkSmartResHandle),
        ("playerShipNode", common.TkHandle),
        ("playerShipAttachment", ctypes.c_uint64),
        ("freighterDockIndex", ctypes.c_int32),
        ("shipCustomisationData", cGcCustomisationComponentData),
    ]


class cGcScanEffectData(ctypes.Structure):
    id: common.TkID[0x10]
    _meScanEffectType: ctypes.c_int32
    colour: common.Colour
    basecolourIntensity: float
    scanlinesSeparation: float
    fresnelIntensity: float
    glowIntensity: float
    waveOffset: float
    waveActive: bool
    fixedUpAxis: bool
    transparent: bool
    modelFade: bool
    fadeInTime: float
    fadeOutTime: float

cGcScanEffectData._fields_ = [
    ("id", common.TkID[0x10]),
    ("_meScanEffectType", ctypes.c_int32),
    ("padding0x14", ctypes.c_ubyte * 0xC),
    ("colour", common.Colour),
    ("basecolourIntensity", ctypes.c_float),
    ("scanlinesSeparation", ctypes.c_float),
    ("fresnelIntensity", ctypes.c_float),
    ("glowIntensity", ctypes.c_float),
    ("waveOffset", ctypes.c_float),
    ("waveActive", ctypes.c_ubyte),
    ("fixedUpAxis", ctypes.c_ubyte),
    ("transparent", ctypes.c_ubyte),
    ("modelFade", ctypes.c_ubyte),
    ("fadeInTime", ctypes.c_float),
    ("fadeOutTime", ctypes.c_float),
]


class cGcPlayerVehicleOwnership(ctypes.Structure):
    newVehicleSpawnCallbacks: bytes
    groupRootNode: common.TkHandle
    vehicles: bytes
    _meRequestVehicle: ctypes.c_int32
    requestedVehicleMatrix: common.cTkMatrix34
    placementArc: bytes
    _meShowPreview: ctypes.c_int32
    previewScanData: "cGcScanEffectData"
    previewColour: common.Colour
    previewFirstActiveTime: float
    previewLastActiveTime: float
    previewNode: common.TkHandle
    clearPreview: bool
    showRocketPreview: bool
    shouldRefreshMesh: bool
    _mMeshRefreshState: ctypes.c_int32
    refreshSwapRes: common.cTkSmartResHandle

cGcPlayerVehicleOwnership._fields_ = [
    ("newVehicleSpawnCallbacks", ctypes.c_ubyte * 0x40),
    ("groupRootNode", common.TkHandle),
    ("padding0x44", ctypes.c_ubyte * 0xC),
    ("vehicles", ctypes.c_ubyte * 0x310),
    ("_meRequestVehicle", ctypes.c_int32),
    ("padding0x364", ctypes.c_ubyte * 0xC),
    ("requestedVehicleMatrix", common.cTkMatrix34),
    ("placementArc", ctypes.c_ubyte * 304),  # cGcPlacementArc
    ("_meShowPreview", ctypes.c_int32),
    ("padding0x4E4", ctypes.c_ubyte * 0xC),
    ("previewScanData", cGcScanEffectData),
    ("previewColour", common.Colour),
    ("previewFirstActiveTime", ctypes.c_float),
    ("previewLastActiveTime", ctypes.c_float),
    ("previewNode", common.TkHandle),
    ("clearPreview", ctypes.c_ubyte),
    ("showRocketPreview", ctypes.c_ubyte),
    ("shouldRefreshMesh", ctypes.c_ubyte),
    ("padding0x55F", ctypes.c_ubyte * 0x1),
    ("_mMeshRefreshState", ctypes.c_int32),
    ("refreshSwapRes", common.cTkSmartResHandle),
]


class cGcPetEggSpeciesOverrideData(ctypes.Structure):
    creatureID: common.TkID[0x10]
    canChangeGrowth: bool
    canChangeAccessories: bool
    canChangeColour: bool
    canChangeTraits: bool
    minScaleOverride: float
    maxScaleOverride: float

cGcPetEggSpeciesOverrideData._fields_ = [
    ("creatureID", common.TkID[0x10]),
    ("canChangeGrowth", ctypes.c_ubyte),
    ("canChangeAccessories", ctypes.c_ubyte),
    ("canChangeColour", ctypes.c_ubyte),
    ("canChangeTraits", ctypes.c_ubyte),
    ("minScaleOverride", ctypes.c_float),
    ("maxScaleOverride", ctypes.c_float),
]


class cGcPetEggSpeciesOverrideTable(ctypes.Structure):
    speciesOverrides: common.cTkDynamicArray[cGcPetEggSpeciesOverrideData]

cGcPetEggSpeciesOverrideTable._fields_ = [
    ("speciesOverrides", common.cTkDynamicArray[cGcPetEggSpeciesOverrideData]),
]


class cGcPlayerCreatureOwnership(ctypes.Structure):
    creatures: bytes
    eggs: bytes
    accessoryCustomisation: bytes
    unlockedSlots: bytes
    thumbnailsGroup: common.TkHandle
    summonedIndex: int
    groupRootNode: common.TkHandle
    placementMatrix: common.cTkMatrix34
    placementArc: bytes
    previewCreature: int
    previewScanData: "cGcScanEffectData"
    previewColour: common.Colour
    previewFirstActiveTime: float
    previewLastActiveTime: float
    previewNode: common.TkHandle
    clearPreview: bool
    showEmoteArc: bool
    emoteArcID: common.TkID[0x10]
    lastRewardActionTime: float
    _meLastRewardActionType: ctypes.c_int32
    petEggResource: common.cTkSmartResHandle
    petHatchEggResource: common.cTkSmartResHandle
    lightMaterial: common.cTkSmartResHandle
    petEggSpeciesOverrideTable: _Pointer["cGcPetEggSpeciesOverrideTable"]

cGcPlayerCreatureOwnership._fields_ = [
    ("creatures", ctypes.c_ubyte * 0x24D80),
    ("eggs", ctypes.c_ubyte * 0x24D80),
    ("accessoryCustomisation", ctypes.c_ubyte * 0xAE720),
    ("unlockedSlots", ctypes.c_ubyte * 0x12),
    ("padding0xF8232", ctypes.c_ubyte * 0x2),
    ("thumbnailsGroup", common.TkHandle),
    ("summonedIndex", ctypes.c_int32),
    ("groupRootNode", common.TkHandle),
    ("placementMatrix", common.cTkMatrix34),
    ("placementArc", ctypes.c_ubyte * 304),  # cGcPlacementArc
    ("previewCreature", ctypes.c_int32),
    ("padding0xF83B4", ctypes.c_ubyte * 0xC),
    ("previewScanData", cGcScanEffectData),
    ("previewColour", common.Colour),
    ("previewFirstActiveTime", ctypes.c_float),
    ("previewLastActiveTime", ctypes.c_float),
    ("previewNode", common.TkHandle),
    ("clearPreview", ctypes.c_ubyte),
    ("showEmoteArc", ctypes.c_ubyte),
    ("padding0xF842E", ctypes.c_ubyte * 0x2),
    ("emoteArcID", common.TkID[0x10]),
    ("lastRewardActionTime", ctypes.c_float),
    ("_meLastRewardActionType", ctypes.c_int32),
    ("petEggResource", common.cTkSmartResHandle),
    ("petHatchEggResource", common.cTkSmartResHandle),
    ("lightMaterial", common.cTkSmartResHandle),
    ("padding0xF8454", ctypes.c_ubyte * 0x4),
    ("petEggSpeciesOverrideTable", ctypes.POINTER(cGcPetEggSpeciesOverrideTable)),
]


class cGcPlayerMultitoolOwnership(ctypes.Structure):
    class sMultitoolInfo(ctypes.Structure):
        inventory: "cGcInventoryStore"
        resource: common.cTkSmartResHandle
        customName: common.cTkFixedString[0x20]
        _mePrimaryMode: ctypes.c_int32
        _meSecondaryMode: ctypes.c_int32
        isLarge: bool
        useLegacyColours: bool
        seed: common.GcSeed

    sMultitoolInfo._fields_ = [
        ("inventory", cGcInventoryStore),
        ("resource", common.cTkSmartResHandle),
        ("customName", common.cTkFixedString[0x20]),
        ("_mePrimaryMode", ctypes.c_int32),
        ("_meSecondaryMode", ctypes.c_int32),
        ("isLarge", ctypes.c_ubyte),
        ("useLegacyColours", ctypes.c_ubyte),
        ("padding0x286", ctypes.c_ubyte * 0x2),
        ("seed", common.GcSeed),
    ]


    multitools: bytes
    thumbnailRenderers: bytes
    thumbnailsGroup: common.TkHandle
    primaryToolIndex: int
    requestedMultitoolIndex: int
    readyWeapon: bool

cGcPlayerMultitoolOwnership._fields_ = [
    ("multitools", ctypes.c_ubyte * 0xF90),
    ("thumbnailRenderers", ctypes.c_ubyte * 0xEA0),
    ("thumbnailsGroup", common.TkHandle),
    ("primaryToolIndex", ctypes.c_int32),
    ("requestedMultitoolIndex", ctypes.c_int32),
    ("readyWeapon", ctypes.c_ubyte),
]


class cGcShipAISquadronSharedData(ctypes.Structure):
    leaving: bool
    lastFormationBreakTime: float
    numShipsInFormation: int

cGcShipAISquadronSharedData._fields_ = [
    ("leaving", ctypes.c_ubyte),
    ("padding0x1", ctypes.c_ubyte * 0x3),
    ("lastFormationBreakTime", ctypes.c_float),
    ("numShipsInFormation", ctypes.c_int32),
]


class cGcPlayerSquadronOwnership(ctypes.Structure):
    class sDismissRequest(ctypes.Structure):
        requested: bool
        warpOut: bool

    sDismissRequest._fields_ = [
        ("requested", ctypes.c_ubyte),
        ("warpOut", ctypes.c_ubyte),
    ]


    isPrepared: bool
    RNG: "cTkPersonalRNG"
    squadHandle: int
    squadronSharedBehaviourData: "cGcShipAISquadronSharedData"
    _meSquadronSummonState: ctypes.c_int32
    squadronSummonStateTime: float
    pilots: bytes
    unlockedSlots: bytes
    _meSquadronCombatSummonState: ctypes.c_int32
    thumbnailsGroup: common.TkHandle
    dismissRequest: "cGcPlayerSquadronOwnership.sDismissRequest"

cGcPlayerSquadronOwnership._fields_ = [
    ("isPrepared", ctypes.c_ubyte),
    ("padding0x1", ctypes.c_ubyte * 0x3),
    ("RNG", cTkPersonalRNG),
    ("squadHandle", ctypes.c_uint64),
    ("squadronSharedBehaviourData", cGcShipAISquadronSharedData),
    ("_meSquadronSummonState", ctypes.c_int32),
    ("squadronSummonStateTime", ctypes.c_float),
    ("padding0x28", ctypes.c_ubyte * 0x8),
    ("pilots", ctypes.c_ubyte * 0x25C0),
    ("unlockedSlots", ctypes.c_ubyte * 0x4),
    ("_meSquadronCombatSummonState", ctypes.c_int32),
    ("thumbnailsGroup", common.TkHandle),
    ("dismissRequest", cGcPlayerSquadronOwnership.sDismissRequest),
]


class cGcGameKnowledge(ctypes.Structure):
    class Data(ctypes.Structure):
        waypoints: bytes
        eventHandlers: bytes

    Data._fields_ = [
        ("waypoints", ctypes.c_ubyte * 0x1F0),
        ("eventHandlers", ctypes.c_ubyte * 0x40),
    ]


    data: _Pointer["cGcGameKnowledge.Data"]
    cachedHandlers: bytes

cGcGameKnowledge._fields_ = [
    ("data", ctypes.POINTER(cGcGameKnowledge.Data)),
    ("cachedHandlers", ctypes.c_ubyte * 0x40),
]


class cGcGrave(ctypes.Structure):
    discovery: bytes  # cGcAtlasDiscovery
    nodeHandle: common.TkHandle

cGcGrave._fields_ = [
    ("discovery", ctypes.c_ubyte * 752),
    ("nodeHandle", common.TkHandle),
]


class cGcGraveManager(ctypes.Structure):
    class Data(ctypes.Structure):
        requestsInFlight: std.vector[ctypes.c_uint64]
        remoteGraves: std.vector[cGcGrave]
        beaconRes: common.cTkSmartResHandle

    Data._fields_ = [
        ("requestsInFlight", std.vector[ctypes.c_uint64]),
        ("remoteGraves", std.vector[cGcGrave]),
        ("beaconRes", common.cTkSmartResHandle),
    ]

    data: _Pointer["cGcGraveManager.Data"]

cGcGraveManager._fields_ = [
    ("data", ctypes.POINTER(cGcGraveManager.Data)),
]


class cGcMsgBeaconManager(ctypes.Structure):
    class Data(ctypes.Structure):
        requestsInFlight: std.vector[ctypes.c_uint64]
        remoteBeacons: bytes
        remoteAsyncOpsBeacons: bytes
        beaconRes: common.cTkSmartResHandle

    Data._fields_ = [
        ("requestsInFlight", std.vector[ctypes.c_uint64]),
        ("remoteBeacons", ctypes.c_ubyte * 0x18),
        ("remoteAsyncOpsBeacons", ctypes.c_ubyte * 0x18),
        ("beaconRes", common.cTkSmartResHandle),
    ]


    data: _Pointer["cGcMsgBeaconManager.Data"]

cGcMsgBeaconManager._fields_ = [
    ("data", ctypes.POINTER(cGcMsgBeaconManager.Data)),
]


class cGcDiscoverySearch(ctypes.Structure):
    constraints: bytes
    result: bytes
    _meRunState: ctypes.c_int32
    maxResults: int
    _meSortMode: ctypes.c_int32
    includeHidden: bool

cGcDiscoverySearch._fields_ = [
    ("constraints", ctypes.c_ubyte * 0x58),
    ("result", ctypes.c_ubyte * 0x18),
    ("_meRunState", ctypes.c_int32),
    ("maxResults", ctypes.c_uint32),
    ("_meSortMode", ctypes.c_int32),
    ("includeHidden", ctypes.c_ubyte),
]


class cGcPlayerDiscoveryHelper(ctypes.Structure):
    class DiscoveryHelperEvent(ctypes.Structure):
        _meEvent: ctypes.c_int32
        waitTime: float
        duration: float

    DiscoveryHelperEvent._fields_ = [
        ("_meEvent", ctypes.c_int32),
        ("waitTime", ctypes.c_float),
        ("duration", ctypes.c_float),
    ]


    discoveredCreatures: int
    totalDiscoverableCreatures: int
    kiNotifyIfDiscoveredLessThan: int
    events: bytes
    discoverySearch: _Pointer["cGcDiscoverySearch"]
    creatureSeed: common.GcSeed
    pendingDiscoveryNew: bool

cGcPlayerDiscoveryHelper._fields_ = [
    ("discoveredCreatures", ctypes.c_int32),
    ("totalDiscoverableCreatures", ctypes.c_int32),
    ("kiNotifyIfDiscoveredLessThan", ctypes.c_int32),
    ("padding0xC", ctypes.c_ubyte * 0x4),
    ("events", ctypes.c_ubyte * 0x8),
    ("discoverySearch", ctypes.POINTER(cGcDiscoverySearch)),
    ("creatureSeed", common.GcSeed),
    ("pendingDiscoveryNew", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0x7),
]


class cGcUserSeenItemsState(ctypes.Structure):
    seenWikiTopics: bytes
    unlockedWikiTopics: bytes
    seenSubstances: bytes
    seenTechnologies: bytes
    seenProducts: bytes
    unlockedTitles: bytes
    unlockedSpecials: bytes
    unlockedSeasonRewards: bytes
    unlockedTwitchRewards: bytes
    unlockedPlatformRewards: bytes
    dataLoadedCallbacks: bytes
    outdated: bool
    loaded: bool

cGcUserSeenItemsState._fields_ = [
    ("seenWikiTopics", ctypes.c_ubyte * 0x40),
    ("unlockedWikiTopics", ctypes.c_ubyte * 0x40),
    ("seenSubstances", ctypes.c_ubyte * 0x40),
    ("seenTechnologies", ctypes.c_ubyte * 0x40),
    ("seenProducts", ctypes.c_ubyte * 0x40),
    ("unlockedTitles", ctypes.c_ubyte * 0x40),
    ("unlockedSpecials", ctypes.c_ubyte * 0x40),
    ("unlockedSeasonRewards", ctypes.c_ubyte * 0x40),
    ("unlockedTwitchRewards", ctypes.c_ubyte * 0x40),
    ("unlockedPlatformRewards", ctypes.c_ubyte * 0x40),
    ("dataLoadedCallbacks", ctypes.c_ubyte * 0x18),
    ("outdated", ctypes.c_ubyte),
    ("loaded", ctypes.c_ubyte),
]


class cGcDifficultyPresetType(ctypes.Structure):
    _meDifficultyPresetType: ctypes.c_int32

cGcDifficultyPresetType._fields_ = [
    ("_meDifficultyPresetType", ctypes.c_int32),
]


class cGcDifficultyStateData(ctypes.Structure):
    preset: "cGcDifficultyPresetType"
    easiestUsedPreset: "cGcDifficultyPresetType"
    hardestUsedPreset: "cGcDifficultyPresetType"
    settings: bytes  # cGcDifficultySettingsData

cGcDifficultyStateData._fields_ = [
    ("preset", cGcDifficultyPresetType),
    ("easiestUsedPreset", cGcDifficultyPresetType),
    ("hardestUsedPreset", cGcDifficultyPresetType),
    ("settings", ctypes.c_ubyte * 88),  # cGcDifficultySettingsData
]


class cGcDifficultySettings(ctypes.Structure):
    difficultyStateData: "cGcDifficultyStateData"
    difficultySettingsDirty: bool

cGcDifficultySettings._fields_ = [
    ("difficultyStateData", cGcDifficultyStateData),
    ("difficultySettingsDirty", ctypes.c_ubyte),
]


class cGcEntitlementRewardData(ctypes.Structure):
    entitlementId: common.TkID[0x10]
    rewardId: common.TkID[0x10]
    name: common.TkID[0x20]
    error: common.TkID[0x20]

cGcEntitlementRewardData._fields_ = [
    ("entitlementId", common.TkID[0x10]),
    ("rewardId", common.TkID[0x10]),
    ("name", common.TkID[0x20]),
    ("error", common.TkID[0x20]),
]


class cGcEntitlementRewardsTable(ctypes.Structure):
    table: common.cTkDynamicArray[cGcEntitlementRewardData]

cGcEntitlementRewardsTable._fields_ = [
    ("table", common.cTkDynamicArray[cGcEntitlementRewardData]),
]


class cGcEntitlementManager(ctypes.Structure):
    entitlementRewardsTable: _Pointer["cGcEntitlementRewardsTable"]

cGcEntitlementManager._fields_ = [
    ("entitlementRewardsTable", ctypes.POINTER(cGcEntitlementRewardsTable)),
]


class cGcPlanetSectionData(ctypes.Structure):
    discovererUID: int
    discovererPlatform: list[int]
    discoveredState: bool

cGcPlanetSectionData._fields_ = [
    ("discovererUID", ctypes.c_uint64),
    ("discovererPlatform", ctypes.c_ubyte * 0x2),
    ("discoveredState", ctypes.c_ubyte),
]


class cGcPlanetaryMappingData(ctypes.Structure):
    UA: int
    sectionsData: common.cTkDynamicArray[cGcPlanetSectionData]

cGcPlanetaryMappingData._fields_ = [
    ("UA", ctypes.c_uint64),
    ("sectionsData", common.cTkDynamicArray[cGcPlanetSectionData]),
]


class MappingDataInternal(ctypes.Structure):
    mappingData: "cGcPlanetaryMappingData"
    sectionPerSide: int
    polesPerSection: int
    minSectionIndex: int
    maxSectionIndex: int
    discoveredState: common.cTkDynamicArray[ctypes.c_uint16]

MappingDataInternal._fields_ = [
    ("mappingData", cGcPlanetaryMappingData),
    ("sectionPerSide", ctypes.c_uint16),
    ("polesPerSection", ctypes.c_uint16),
    ("minSectionIndex", ctypes.c_int32),
    ("maxSectionIndex", ctypes.c_int32),
    ("padding0x24", ctypes.c_ubyte * 0x4),
    ("discoveredState", common.cTkDynamicArray[ctypes.c_uint16]),
]


class cGcPlanetMappingManager(ctypes.Structure):
    mappingInternal: std.vector[MappingDataInternal]

cGcPlanetMappingManager._fields_ = [
    ("mappingInternal", std.vector[MappingDataInternal]),
]


class cGcDiscoveryOwner(ctypes.Structure):
    localID: common.cTkFixedString[0x40]
    onlineID: common.cTkFixedString[0x40]
    username: common.cTkFixedString[0x40]
    platform: common.cTkFixedString[0x40]
    timestamp: int

cGcDiscoveryOwner._fields_ = [
    ("localID", common.cTkFixedString[0x40]),
    ("onlineID", common.cTkFixedString[0x40]),
    ("username", common.cTkFixedString[0x40]),
    ("platform", common.cTkFixedString[0x40]),
    ("timestamp", ctypes.c_int32),
]


class cGcSettlementJudgementType(ctypes.Structure):
    _meSettlementJudgementType: ctypes.c_int32

cGcSettlementJudgementType._fields_ = [
    ("_meSettlementJudgementType", ctypes.c_int32),
]


class cGcSettlementState(ctypes.Structure):
    uniqueId: common.cTkFixedString[0x40]
    universeAddress: int
    position: common.Vector3f
    seedValue: int
    buildingStates: bytes
    lastBuildingUpgradesTimestamps: bytes
    name: common.cTkFixedString[0x40]
    owner: "cGcDiscoveryOwner"
    pendingJudgementType: "cGcSettlementJudgementType"
    pendingCustomJudgementID: common.TkID[0x10]
    stats: bytes
    perks: common.cTkDynamicArray[common.TkID[0x10]]
    lastJudgementTime: int
    lastUpkeepDebtCheckTime: int
    lastDebtChangeTime: int
    lastAlertChangeTime: int
    dbResourceId: common.cTkFixedString[0x40]
    dbTimestamp: int
    dbVersion: int
    productionState: bytes
    isReported: bool
    nextBuildingUpgradeIndex: int
    nextBuildingUpgradeClass: "cGcBuildingClassification"
    nextBuildingUpgradeSeedValue: int

cGcSettlementState._fields_ = [
    ("uniqueId", common.cTkFixedString[0x40]),
    ("universeAddress", ctypes.c_uint64),
    ("padding0x48", ctypes.c_ubyte * 0x8),
    ("position", common.Vector3f),
    ("seedValue", ctypes.c_uint64),
    ("buildingStates", ctypes.c_ubyte * 0xC0),
    ("lastBuildingUpgradesTimestamps", ctypes.c_ubyte * 0x180),
    ("name", common.cTkFixedString[0x40]),
    ("owner", cGcDiscoveryOwner),
    ("pendingJudgementType", cGcSettlementJudgementType),
    ("pendingCustomJudgementID", common.TkID[0x10]),
    ("stats", ctypes.c_ubyte * 0x1C),
    ("padding0x41C", ctypes.c_ubyte * 0x4),
    ("perks", common.cTkDynamicArray[common.TkID[0x10]]),
    ("lastJudgementTime", ctypes.c_uint64),
    ("lastUpkeepDebtCheckTime", ctypes.c_uint64),
    ("lastDebtChangeTime", ctypes.c_uint64),
    ("lastAlertChangeTime", ctypes.c_uint64),
    ("dbResourceId", common.cTkFixedString[0x40]),
    ("dbTimestamp", ctypes.c_uint64),
    ("dbVersion", ctypes.c_int32),
    ("padding0x49C", ctypes.c_ubyte * 0x4),
    ("productionState", ctypes.c_ubyte * 0x40),
    ("isReported", ctypes.c_ubyte),
    ("padding0x4E1", ctypes.c_ubyte * 0x3),
    ("nextBuildingUpgradeIndex", ctypes.c_int32),
    ("nextBuildingUpgradeClass", cGcBuildingClassification),
    ("padding0x4EC", ctypes.c_ubyte * 0x4),
    ("nextBuildingUpgradeSeedValue", ctypes.c_uint64),
    ("endpadding", ctypes.c_ubyte * 0x8),
]


class cGcSettlementStateManager(ctypes.Structure):
    ownedSettlementBuildingClasses: bytes
    ownedSettlementBuildingSeeds: bytes
    ownedSettlementState: _Pointer["cGcSettlementState"]
    settlementToReport: _Pointer["cGcSettlementState"]
    settlementToAbandon: "cGcSettlementState"
    cachedPendingCustomJudgementID: common.TkID[0x10]
    nextBuildingUpgradeTimestamp: int
    hasBuildingClassesAndSeeds: bool
    ownedSettlementPendingUpload: bool
    ownedSettlementUploadFailed: bool
    abandonSettlementUploadFailed: bool
    reportSettlementFailed: bool
    storeSettlementTeleportEndpointFailed: bool
    onBuildingStateChangedPending: bool
    claimingFirstSettlement: bool
    completAllClumpsChecked: bool

cGcSettlementStateManager._fields_ = [
    ("ownedSettlementBuildingClasses", ctypes.c_ubyte * 0xC0),
    ("ownedSettlementBuildingSeeds", ctypes.c_ubyte * 0x300),
    ("ownedSettlementState", ctypes.POINTER(cGcSettlementState)),
    ("settlementToReport", ctypes.POINTER(cGcSettlementState)),
    ("settlementToAbandon", cGcSettlementState),
    ("cachedPendingCustomJudgementID", common.TkID[0x10]),
    ("nextBuildingUpgradeTimestamp", ctypes.c_uint64),
    ("hasBuildingClassesAndSeeds", ctypes.c_ubyte),
    ("ownedSettlementPendingUpload", ctypes.c_ubyte),
    ("ownedSettlementUploadFailed", ctypes.c_ubyte),
    ("abandonSettlementUploadFailed", ctypes.c_ubyte),
    ("reportSettlementFailed", ctypes.c_ubyte),
    ("storeSettlementTeleportEndpointFailed", ctypes.c_ubyte),
    ("onBuildingStateChangedPending", ctypes.c_ubyte),
    ("claimingFirstSettlement", ctypes.c_ubyte),
    ("completAllClumpsChecked", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0xF),
]


class cGcNetworkBufferHash_vtbl(ctypes.Structure):
    cGcNetworkBufferHash_dtor_0: bytes
    GetHashValue: bytes
    GetHashTimestamp: bytes
    GenerateHashValue: bytes
    OnHashOffsetChanged: bytes

cGcNetworkBufferHash_vtbl._fields_ = [
    ("cGcNetworkBufferHash_dtor_0", ctypes.c_ubyte * 0x8),
    ("GetHashValue", ctypes.c_ubyte * 0x8),
    ("GetHashTimestamp", ctypes.c_ubyte * 0x8),
    ("GenerateHashValue", ctypes.c_ubyte * 0x8),
    ("OnHashOffsetChanged", ctypes.c_ubyte * 0x8),
]


class sHashValue(ctypes.Structure):
    hashValue: int
    timeStamp: int

sHashValue._fields_ = [
    ("hashValue", ctypes.c_uint16),
    ("timeStamp", ctypes.c_int16),
]


class cGcNetworkBufferHash(ctypes.Structure):
    __vftable: _Pointer["cGcNetworkBufferHash_vtbl"]
    kiChunkSize: int
    chunkHashOffset: int
    chunkHashValues: std.vector[sHashValue]
    timestamp: int
    initialised: bool

cGcNetworkBufferHash._fields_ = [
    ("__vftable", ctypes.POINTER(cGcNetworkBufferHash_vtbl)),
    ("kiChunkSize", ctypes.c_int32),
    ("chunkHashOffset", ctypes.c_int32),
    ("chunkHashValues", std.vector[sHashValue]),
    ("timestamp", ctypes.c_uint64),
    ("initialised", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0x7),
]


class cGcNetworkSynchronisedBuffer(cGcNetworkBufferHash, ctypes.Structure):
    pass

cGcNetworkSynchronisedBuffer._fields_ = []


class cGcPersistentBBObjectData(ctypes.Structure):
    timestamp: int
    objectID: common.TkID[0x10]
    galacticAddress: int
    regionSeed: int
    userData: int
    position: common.Vector3f
    up: common.Vector3f
    at: common.Vector3f

cGcPersistentBBObjectData._fields_ = [
    ("timestamp", ctypes.c_uint64),
    ("objectID", common.TkID[0x10]),
    ("galacticAddress", ctypes.c_uint64),
    ("regionSeed", ctypes.c_uint64),
    ("userData", ctypes.c_uint64),
    ("position", common.Vector3f),
    ("up", common.Vector3f),
    ("at", common.Vector3f),
]


class cGcBaseBuildingPersistentBuffer(cGcNetworkSynchronisedBuffer, ctypes.Structure):
    class BaseBuildingPersistentData_vtbl(ctypes.Structure):
        pass

    BaseBuildingPersistentData_vtbl._fields_ = []

    class BaseBuildingPersistentData(ctypes.Structure):
        __vftable: bytes
        data: cGcPersistentBBObjectData
        inc: int

    BaseBuildingPersistentData._fields_ = [
        ("__vftable", ctypes.c_ubyte * 0x8),
        ("data", cGcPersistentBBObjectData),
        ("inc", ctypes.c_uint16),
        ("endpadding", ctypes.c_ubyte * 0xE),
    ]


    baseBuildingObjects: std.vector[cGcBaseBuildingPersistentBuffer.BaseBuildingPersistentData]
    currentPlanetObjects: bytes
    currentAddress: int
    debugPositions: bool
    networkOwnerId: bytes
    bufferIndex: int

cGcBaseBuildingPersistentBuffer._fields_ = [
    ("baseBuildingObjects", std.vector[cGcBaseBuildingPersistentBuffer.BaseBuildingPersistentData]),
    ("currentPlanetObjects", ctypes.c_ubyte * 0x40),
    ("currentAddress", ctypes.c_uint64),
    ("debugPositions", ctypes.c_ubyte),
    ("networkOwnerId", ctypes.c_ubyte * 0x40),
    ("padding0xD9", ctypes.c_ubyte * 0x3),
    ("bufferIndex", ctypes.c_uint32),
]


class cGcBaseBuildingGlobalBuffer(ctypes.Structure):
    class BaseBuildingPersistentData_vtbl(ctypes.Structure):
        pass

    BaseBuildingPersistentData_vtbl._fields_ = []


    persistentBuffers: list[cGcBaseBuildingPersistentBuffer]

cGcBaseBuildingGlobalBuffer._fields_ = [
    ("persistentBuffers", cGcBaseBuildingPersistentBuffer * 0x20),
]


class cGcBaseBuildingBaseLayout(ctypes.Structure):
    baseUA: int
    basePosition: common.Vector3f
    baseUp: common.Vector3f
    baseObjectSpheres: bytes
    baseObjectsTree: bytes
    baseRadiusSqr: float
    treeNeedsRebuild: bool
    treeRebuildTimer: float

cGcBaseBuildingBaseLayout._fields_ = [
    ("baseUA", ctypes.c_uint64),
    ("padding0x8", ctypes.c_ubyte * 0x8),
    ("basePosition", common.Vector3f),
    ("baseUp", common.Vector3f),
    ("baseObjectSpheres", ctypes.c_ubyte * 0x80),
    ("baseObjectsTree", ctypes.c_ubyte * 0xA8),
    ("baseRadiusSqr", ctypes.c_float),
    ("treeNeedsRebuild", ctypes.c_ubyte),
    ("padding0x15D", ctypes.c_ubyte * 0x3),
    ("treeRebuildTimer", ctypes.c_float),
    ("endpadding", ctypes.c_ubyte * 0xC),
]


class cGcBaseLinkMap(ctypes.Structure):
    class sLinkSocket(ctypes.Structure):
        linkIndex: int
        dependentIndex: str

    sLinkSocket._fields_ = [
        ("linkIndex", ctypes.c_uint16),
        ("dependentIndex", ctypes.c_char),
    ]


    class sObjectLinkData(ctypes.Structure):
        links: std.vector[cGcBaseLinkMap.sLinkSocket]
        dependentLinks: std.vector[std.vector[ctypes.c_uint16]]
        bufferIndex: int
        dependantLinksStart: int
        setNext: int


    linkObjects: std.vector[cGcBaseLinkMap.sObjectLinkData]
    linkObjectInstanceLookup: std.vector[ctypes.c_uint16]


cGcBaseLinkMap.sObjectLinkData._fields_ = [
    ("links", std.vector[cGcBaseLinkMap.sLinkSocket]),
    ("dependentLinks", std.vector[std.vector[ctypes.c_uint16]]),
    ("bufferIndex", ctypes.c_uint16),
    ("dependantLinksStart", ctypes.c_uint16),
    ("setNext", ctypes.c_uint16),
]

cGcBaseLinkMap._fields_ = [
    ("linkObjects", std.vector[cGcBaseLinkMap.sObjectLinkData]),
    ("linkObjectInstanceLookup", std.vector[ctypes.c_uint16]),
]


class cGcGameMode(ctypes.Structure):
    _mePresetGameMode: ctypes.c_int32

cGcGameMode._fields_ = [
    ("_mePresetGameMode", ctypes.c_int32),
]


class cGcPersistentBaseDifficultyData(ctypes.Structure):
    difficultyPreset: "cGcDifficultyPresetType"
    _mexPersistentBaseDifficultyFlags: ctypes.c_int32

cGcPersistentBaseDifficultyData._fields_ = [
    ("difficultyPreset", cGcDifficultyPresetType),
    ("_mexPersistentBaseDifficultyFlags", ctypes.c_int32),
]


class cGcPersistentBaseEntry(ctypes.Structure):
    timestamp: int
    objectID: common.TkID[0x10]
    userData: int
    position: common.Vector3f
    up: common.Vector3f
    at: common.Vector3f
    message: common.cTkFixedString[0x40]

cGcPersistentBaseEntry._fields_ = [
    ("timestamp", ctypes.c_uint64),
    ("objectID", common.TkID[0x10]),
    ("userData", ctypes.c_uint64),
    ("position", common.Vector3f),
    ("up", common.Vector3f),
    ("at", common.Vector3f),
    ("message", common.cTkFixedString[0x40]),
]


class cGcBaseBuildingPartStyle(ctypes.Structure):
    _meStyle: ctypes.c_int32

cGcBaseBuildingPartStyle._fields_ = [
    ("_meStyle", ctypes.c_int32),
]


class cGcBaseBuildingObjectDecorationTypes(ctypes.Structure):
    _meBaseBuildingDecorationType: ctypes.c_int32

cGcBaseBuildingObjectDecorationTypes._fields_ = [
    ("_meBaseBuildingDecorationType", ctypes.c_int32),
]


class cGcBaseBuildingEntryGroup(ctypes.Structure):
    group: common.TkID[0x10]
    subGroupName: common.TkID[0x10]
    subGroup: int

cGcBaseBuildingEntryGroup._fields_ = [
    ("group", common.TkID[0x10]),
    ("subGroupName", common.TkID[0x10]),
    ("subGroup", ctypes.c_int32),
]


class cGcLinkNetworkTypes(ctypes.Structure):
    _meLinkNetworkType: ctypes.c_int32

cGcLinkNetworkTypes._fields_ = [
    ("_meLinkNetworkType", ctypes.c_int32),
]


class cGcBaseLinkGridConnectionData(ctypes.Structure):
    network: "cGcLinkNetworkTypes"
    networkSubGroup: int
    networkMask: int
    connectionDistance: float
    useMinDistance: bool
    linkSocketPositions: common.cTkDynamicArray[common.Vector3f]
    linkSocketSubGroups: common.cTkDynamicArray[ctypes.c_int32]

cGcBaseLinkGridConnectionData._fields_ = [
    ("network", cGcLinkNetworkTypes),
    ("networkSubGroup", ctypes.c_int32),
    ("networkMask", ctypes.c_int32),
    ("connectionDistance", ctypes.c_float),
    ("useMinDistance", ctypes.c_ubyte),
    ("padding0x11", ctypes.c_ubyte * 0x7),
    ("linkSocketPositions", common.cTkDynamicArray[common.Vector3f]),
    ("linkSocketSubGroups", common.cTkDynamicArray[ctypes.c_int32]),
]


class cGcBaseLinkGridConnectionDependency(ctypes.Structure):
    connection: "cGcBaseLinkGridConnectionData"
    dependentRate: int
    _meDependentEffect: ctypes.c_int32
    disableWhenOffline: bool
    transfersConnections: bool

cGcBaseLinkGridConnectionDependency._fields_ = [
    ("connection", cGcBaseLinkGridConnectionData),
    ("dependentRate", ctypes.c_int32),
    ("_meDependentEffect", ctypes.c_int32),
    ("disableWhenOffline", ctypes.c_ubyte),
    ("transfersConnections", ctypes.c_ubyte),
]


class cGcBaseLinkGridData(ctypes.Structure):
    connection: "cGcBaseLinkGridConnectionData"
    rate: int
    storage: int
    _meDependsOnEnvironment: ctypes.c_int32
    _meDependsOnHotspots: ctypes.c_int32
    dependentConnections: common.cTkDynamicArray[cGcBaseLinkGridConnectionDependency]

cGcBaseLinkGridData._fields_ = [
    ("connection", cGcBaseLinkGridConnectionData),
    ("rate", ctypes.c_int32),
    ("storage", ctypes.c_int32),
    ("_meDependsOnEnvironment", ctypes.c_int32),
    ("_meDependsOnHotspots", ctypes.c_int32),
    ("dependentConnections", common.cTkDynamicArray[cGcBaseLinkGridConnectionDependency]),
]


class cGcBaseBuildingEntry(ctypes.Structure):
    ID: common.TkID[0x10]
    isTemporary: bool
    isFromModFolder: bool
    style: "cGcBaseBuildingPartStyle"
    placementScene: "cTkModelResource"
    decorationType: "cGcBaseBuildingObjectDecorationTypes"
    isPlaceable: bool
    isDecoration: bool
    biome: "cGcBiomeType"
    buildableOnPlanetBase: bool
    buildableOnSpaceBase: bool
    buildableOnFreighter: bool
    buildableOnPlanet: bool
    buildableOnPlanetWithProduct: bool
    buildableUnderwater: bool
    buildableAboveWater: bool
    planetLimit: int
    regionLimit: int
    planetBaseLimit: int
    freighterBaseLimit: int
    checkPlaceholderCollision: bool
    checkPlayerCollision: bool
    canRotate3D: bool
    canScale: bool
    groups: common.cTkDynamicArray[cGcBaseBuildingEntryGroup]
    storageContainerIndex: int
    colourPaletteGroupId: common.TkID[0x20]
    defaultColourPaletteId: common.TkID[0x20]
    materialGroupId: common.TkID[0x20]
    defaultMaterialId: common.TkID[0x20]
    canChangeColour: bool
    canChangeMaterial: bool
    canPickUp: bool
    showInBuildMenu: bool
    compositePartObjectIDs: common.cTkDynamicArray[common.TkID[0x10]]
    familyIDs: common.cTkDynamicArray[common.TkID[0x10]]
    buildEffectAccelerator: float
    removesAttachedDecoration: bool
    removesWhenUnsnapped: bool
    editsTerrain: bool
    _meBaseTerrainEditShape: ctypes.c_int32
    minimumDeleteDistance: float
    isSealed: bool
    closeMenuAfterBuild: bool
    linkGridData: "cGcBaseLinkGridData"
    ghostsCountOverride: int
    showGhosts: bool
    snappingDistanceOverride: float
    regionSpawnLOD: int
    nPCInteractionScene: "cTkModelResource"

cGcBaseBuildingEntry._fields_ = [
    ("ID", common.TkID[0x10]),
    ("isTemporary", ctypes.c_ubyte),
    ("isFromModFolder", ctypes.c_ubyte),
    ("padding0x12", ctypes.c_ubyte * 0x2),
    ("style", cGcBaseBuildingPartStyle),
    ("placementScene", cTkModelResource),
    ("decorationType", cGcBaseBuildingObjectDecorationTypes),
    ("isPlaceable", ctypes.c_ubyte),
    ("isDecoration", ctypes.c_ubyte),
    ("padding0xA2", ctypes.c_ubyte * 0x2),
    ("biome", cGcBiomeType),
    ("buildableOnPlanetBase", ctypes.c_ubyte),
    ("buildableOnSpaceBase", ctypes.c_ubyte),
    ("buildableOnFreighter", ctypes.c_ubyte),
    ("buildableOnPlanet", ctypes.c_ubyte),
    ("buildableOnPlanetWithProduct", ctypes.c_ubyte),
    ("buildableUnderwater", ctypes.c_ubyte),
    ("buildableAboveWater", ctypes.c_ubyte),
    ("padding0xAF", ctypes.c_ubyte * 0x1),
    ("planetLimit", ctypes.c_int32),
    ("regionLimit", ctypes.c_int32),
    ("planetBaseLimit", ctypes.c_int32),
    ("freighterBaseLimit", ctypes.c_int32),
    ("checkPlaceholderCollision", ctypes.c_ubyte),
    ("checkPlayerCollision", ctypes.c_ubyte),
    ("canRotate3D", ctypes.c_ubyte),
    ("canScale", ctypes.c_ubyte),
    ("padding0xC4", ctypes.c_ubyte * 0x4),
    ("groups", common.cTkDynamicArray[cGcBaseBuildingEntryGroup]),
    ("storageContainerIndex", ctypes.c_int32),
    ("padding0xDC", ctypes.c_ubyte * 0x4),
    ("colourPaletteGroupId", common.TkID[0x20]),
    ("defaultColourPaletteId", common.TkID[0x20]),
    ("materialGroupId", common.TkID[0x20]),
    ("defaultMaterialId", common.TkID[0x20]),
    ("canChangeColour", ctypes.c_ubyte),
    ("canChangeMaterial", ctypes.c_ubyte),
    ("canPickUp", ctypes.c_ubyte),
    ("showInBuildMenu", ctypes.c_ubyte),
    ("padding0x164", ctypes.c_ubyte * 0x4),
    ("compositePartObjectIDs", common.cTkDynamicArray[common.TkID[0x10]]),
    ("familyIDs", common.cTkDynamicArray[common.TkID[0x10]]),
    ("buildEffectAccelerator", ctypes.c_float),
    ("removesAttachedDecoration", ctypes.c_ubyte),
    ("removesWhenUnsnapped", ctypes.c_ubyte),
    ("editsTerrain", ctypes.c_ubyte),
    ("padding0x18F", ctypes.c_ubyte * 0x1),
    ("_meBaseTerrainEditShape", ctypes.c_int32),
    ("minimumDeleteDistance", ctypes.c_float),
    ("isSealed", ctypes.c_ubyte),
    ("closeMenuAfterBuild", ctypes.c_ubyte),
    ("padding0x19A", ctypes.c_ubyte * 0x6),
    ("linkGridData", cGcBaseLinkGridData),
    ("ghostsCountOverride", ctypes.c_int32),
    ("showGhosts", ctypes.c_ubyte),
    ("padding0x1FD", ctypes.c_ubyte * 0x3),
    ("snappingDistanceOverride", ctypes.c_float),
    ("regionSpawnLOD", ctypes.c_int32),
    ("nPCInteractionScene", cTkModelResource),
    ("endpadding", ctypes.c_ubyte * 0x4),
]


class cGcPlayerBasePersistentBuffer(cGcNetworkSynchronisedBuffer, ctypes.Structure):
    class PlayerBasePersistentData_vtbl(ctypes.Structure):
        pass

    PlayerBasePersistentData_vtbl._fields_ = []

    class PlayerBasePersistentData(ctypes.Structure):
        __vftable: bytes
        data: cGcPersistentBaseEntry
        inc: int
        regionId: int
        linkIndex: int
        gridIndex: int
        buildingEntry: ctypes._Pointer[cGcBaseBuildingEntry]


    PlayerBasePersistentData._fields_ = [
        ("__vftable", ctypes.c_ubyte * 0x8),
        ("data", cGcPersistentBaseEntry),
        ("inc", ctypes.c_uint16),
        ("padding", ctypes.c_ubyte * 0xE),
        ("regionId", ctypes.c_uint64),
        ("linkIndex", ctypes.c_uint16),
        ("gridIndex", ctypes.c_uint16),
        ("buildingEntry", ctypes.POINTER(cGcBaseBuildingEntry)),
        ("endpadding", ctypes.c_ubyte * 0x8),
    ]

    class sStats(ctypes.Structure):
        hasTeleporter: bool
        hasMainframe: bool
        hasParagonGenerator: bool
        storageContainers: int

    sStats._fields_ = [
        ("hasTeleporter", ctypes.c_ubyte),
        ("hasMainframe", ctypes.c_ubyte),
        ("hasParagonGenerator", ctypes.c_ubyte),
        ("padding0x3", ctypes.c_ubyte * 0x1),
        ("storageContainers", ctypes.c_uint16),
    ]


    baseBuildingObjects: std.vector[cGcPlayerBasePersistentBuffer.PlayerBasePersistentData]
    currentAddress: int
    lastUpdateTimestamp: int
    baseMatrix: common.cTkMatrix34
    baseUA: int
    baseUserData: int
    RID: common.cTkFixedString[0x40]
    owner: "cGcDiscoveryOwner"
    name: common.cTkFixedString[0x40]
    baseVersion: int
    originalBaseVersion: int
    _meBaseType: ctypes.c_int32
    networkOwnerId: bytes
    lastEditedById: bytes
    lastEditedByUsername: common.cTkFixedString[0x40]
    layoutHandle: _Pointer["cGcBaseBuildingBaseLayout"]
    validObjectsCount: int
    expectedObjectsCount: int
    lowestInvalidIndex: int
    screenshotPosition: common.Vector3f
    screenshotAt: common.Vector3f
    linkMap: "cGcBaseLinkMap"
    linkGrids: std.vector[bytes]  # cGcLinkGrid
    regenerateLinkGrids: bool
    isReported: bool
    isFeatured: bool
    isHidden: bool
    _meAutoPowerSetting: ctypes.c_int32
    stats: "cGcPlayerBasePersistentBuffer.sStats"
    statsDirty: bool
    nGuiOffset: int
    debugPositions: bool
    gameMode: "cGcGameMode"
    difficulty: "cGcPersistentBaseDifficultyData"

cGcPlayerBasePersistentBuffer._fields_ = [
    ("baseBuildingObjects", std.vector[cGcPlayerBasePersistentBuffer.PlayerBasePersistentData]),
    ("currentAddress", ctypes.c_uint64),
    ("lastUpdateTimestamp", ctypes.c_uint64),
    ("baseMatrix", common.cTkMatrix34),
    ("baseUA", ctypes.c_uint64),
    ("baseUserData", ctypes.c_uint64),
    ("RID", common.cTkFixedString[0x40]),
    ("owner", cGcDiscoveryOwner),
    ("name", common.cTkFixedString[0x40]),
    ("baseVersion", ctypes.c_int32),
    ("originalBaseVersion", ctypes.c_int32),
    ("_meBaseType", ctypes.c_int32),
    ("networkOwnerId", ctypes.c_ubyte * 0x40),
    ("lastEditedById", ctypes.c_ubyte * 0x40),
    ("lastEditedByUsername", common.cTkFixedString[0x40]),
    ("layoutHandle", ctypes.POINTER(cGcBaseBuildingBaseLayout)),
    ("validObjectsCount", ctypes.c_uint32),
    ("expectedObjectsCount", ctypes.c_uint32),
    ("lowestInvalidIndex", ctypes.c_uint32),
    ("padding0x324", ctypes.c_ubyte * 0xC),
    ("screenshotPosition", common.Vector3f),
    ("screenshotAt", common.Vector3f),
    ("linkMap", cGcBaseLinkMap),
    ("linkGrids", std.vector[ctypes.c_ubyte * 0x80]),  # cGcLinkGrid
    ("regenerateLinkGrids", ctypes.c_ubyte),
    ("isReported", ctypes.c_ubyte),
    ("isFeatured", ctypes.c_ubyte),
    ("isHidden", ctypes.c_ubyte),
    ("_meAutoPowerSetting", ctypes.c_int32),
    ("stats", cGcPlayerBasePersistentBuffer.sStats),
    ("statsDirty", ctypes.c_ubyte),
    ("padding0x3A7", ctypes.c_ubyte * 0x1),
    ("nGuiOffset", ctypes.c_int32),
    ("debugPositions", ctypes.c_ubyte),
    ("padding0x3AD", ctypes.c_ubyte * 0x3),
    ("gameMode", cGcGameMode),
    ("difficulty", cGcPersistentBaseDifficultyData),
    ("endpadding", ctypes.c_ubyte * 0x4),
]


class cGcPersistentInteractionBuffer(cGcNetworkSynchronisedBuffer, ctypes.Structure):
    lastBufferIndex: int
    currentAddress: int
    _meType: ctypes.c_int32
    bufferData: common.cTkDynamicArray[cGcInteractionData]
    currentPos: int
    savedInteractionsDB: bytes
    tree: bytes
    nGuiOffset: int
    timeSinceLastSavedInteraction: float
    furthestPointDistance: float
    furthestPoint: common.Vector3f
    mutex: int
    persistenceActive: bool
    treeHasData: bool
    treeNeedsRebuild: bool

cGcPersistentInteractionBuffer._fields_ = [
    ("lastBufferIndex", ctypes.c_int32),
    ("padding0x3C", ctypes.c_ubyte * 0x4),
    ("currentAddress", ctypes.c_uint64),
    ("_meType", ctypes.c_int32),
    ("padding0x4C", ctypes.c_ubyte * 0x4),
    ("bufferData", common.cTkDynamicArray[cGcInteractionData]),
    ("currentPos", ctypes.c_int32),
    ("padding0x64", ctypes.c_ubyte * 0xC),
    ("savedInteractionsDB", ctypes.c_ubyte * 0x80),
    ("tree", ctypes.c_ubyte * 0xA8),
    ("nGuiOffset", ctypes.c_int32),
    ("timeSinceLastSavedInteraction", ctypes.c_float),
    ("furthestPointDistance", ctypes.c_float),
    ("padding0x1A4", ctypes.c_ubyte * 0xC),
    ("furthestPoint", common.Vector3f),
    ("mutex", ctypes.c_void_p),
    ("persistenceActive", ctypes.c_ubyte),
    ("treeHasData", ctypes.c_ubyte),
    ("treeNeedsRebuild", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0x7),
]


class sSharedMutex(ctypes.Structure):
    mutex: int
    mutexCreated: bool

sSharedMutex._fields_ = [
    ("mutex", ctypes.c_void_p),
    ("mutexCreated", ctypes.c_ubyte),
]


class cGcTerrainEditBlockBuffer(cGcNetworkSynchronisedBuffer, ctypes.Structure):
    sharedMutex: _Pointer["sSharedMutex"]
    galacticAddress: int
    editsBoundingBox: common.cTkAABB
    edits: bytes
    networkOwnerId: bytes
    isBaseProtected: bool
    lastPlayerRequestTimestamp: bytes

cGcTerrainEditBlockBuffer._fields_ = [
    ("sharedMutex", ctypes.POINTER(sSharedMutex)),
    ("galacticAddress", ctypes.c_uint64),
    ("padding0x48", ctypes.c_ubyte * 0x8),
    ("editsBoundingBox", common.cTkAABB),
    ("edits", ctypes.c_ubyte * 0x28),
    ("networkOwnerId", ctypes.c_ubyte * 0x40),
    ("isBaseProtected", ctypes.c_ubyte),
    ("padding0xD9", ctypes.c_ubyte * 0x1),
    ("lastPlayerRequestTimestamp", ctypes.c_int16 * 31),
    ("endpadding", ctypes.c_ubyte * 0x8),
]


class cGcTerrainEditsPersistentBuffer(ctypes.Structure):
    class sPendingEdit(ctypes.Structure):
        position: common.Vector3f
        data: int
        UA: int
        extraData: str
        isUndo: bool
        setBaseProtected: bool
        jobId: bool

    sPendingEdit._fields_ = [
        ("position", common.Vector3f),
        ("data", ctypes.c_int8),
        ("padding0x11", ctypes.c_ubyte * 0x7),
        ("UA", ctypes.c_uint64),
        ("extraData", ctypes.c_char),
        ("isUndo", ctypes.c_ubyte),
        ("setBaseProtected", ctypes.c_ubyte),
        ("jobId", ctypes.c_ubyte),
        ("endpadding", ctypes.c_ubyte * 0xC),
    ]


    class sPendingBlockJob(ctypes.Structure):
        UA: int
        anchor: common.Vector3f
        limits: common.Vector3f
        ownerId: bytes
        hashOffset: int
        edits: bytes

    sPendingBlockJob._fields_ = [
        ("UA", ctypes.c_uint64),
        ("padding0x8", ctypes.c_ubyte * 0x8),
        ("anchor", common.Vector3f),
        ("limits", common.Vector3f),
        ("ownerId", ctypes.c_ubyte * 0x40),
        ("hashOffset", ctypes.c_uint16),
        ("padding0x72", ctypes.c_ubyte * 0x6),
        ("edits", ctypes.c_ubyte * 0x28),
    ]


    blockBuffers: list[cGcTerrainEditBlockBuffer]
    bufferAges: list[int]
    currentGalacticAddress: int
    nonEmptyBuffersCount: int
    initialised: bool
    cachedProtectedEditsCount: int
    cachedProtectedBlocksCount: int
    pendingEdits: list[cGcTerrainEditsPersistentBuffer.sPendingEdit]
    jobPendingEditIndex: ctypes.c_int32
    jobProcessedEditIndex: int
    editJobRunning: ctypes.c_int32
    currentJobId: bool
    jobMutex: int
    pendingBlockJobs: bytes
    blockJobPendingIndex: int
    blockJobProcessedIndex: int

cGcTerrainEditsPersistentBuffer._fields_ = [
    ("blockBuffers", cGcTerrainEditBlockBuffer * 0x100),
    ("bufferAges", ctypes.c_int32 * 0x100),
    ("currentGalacticAddress", ctypes.c_uint64),
    ("nonEmptyBuffersCount", ctypes.c_int32),
    ("initialised", ctypes.c_ubyte),
    ("padding0x1240D", ctypes.c_ubyte * 0x3),
    ("cachedProtectedEditsCount", ctypes.c_int32),
    ("cachedProtectedBlocksCount", ctypes.c_int32),
    ("padding0x12418", ctypes.c_ubyte * 0x8),
    ("pendingEdits", cGcTerrainEditsPersistentBuffer.sPendingEdit * 50000),
    ("jobPendingEditIndex", ctypes.c_int32),
    ("jobProcessedEditIndex", ctypes.c_int32),
    ("editJobRunning", ctypes.c_int32),
    ("currentJobId", ctypes.c_ubyte),
    ("padding0x25C32D", ctypes.c_ubyte * 0x3),
    ("jobMutex", ctypes.c_void_p),
    ("padding0x25C338", ctypes.c_ubyte * 0x8),
    ("pendingBlockJobs", cGcTerrainEditsPersistentBuffer.sPendingBlockJob * 0x100),
    ("blockJobPendingIndex", ctypes.c_int32),
    ("blockJobProcessedIndex", ctypes.c_int32),
    ("endpadding", ctypes.c_ubyte * 0xC),
]


class cGcTradingSupplyData(ctypes.Structure):
    galacticAddress: int
    supply: float
    demand: float
    product: common.TkID[0x10]
    timestamp: int

cGcTradingSupplyData._fields_ = [
    ("galacticAddress", ctypes.c_uint64),
    ("supply", ctypes.c_float),
    ("demand", ctypes.c_float),
    ("product", common.TkID[0x10]),
    ("timestamp", ctypes.c_uint64),
]


class cGcTradingSupplyBuffer(ctypes.Structure):
    class TradingUA(ctypes.Structure):
        data: int

    TradingUA._fields_ = [
        ("data", ctypes.c_uint64),
    ]


    debugCurrentPage: int
    currentIndex: int
    tradingData: std.vector[cGcTradingSupplyData]

cGcTradingSupplyBuffer._fields_ = [
    ("debugCurrentPage", ctypes.c_int32),
    ("currentIndex", ctypes.c_int32),
    ("tradingData", std.vector[cGcTradingSupplyData]),
]


class cGcMaintenanceBuffer(cGcPersistentInteractionBuffer, ctypes.Structure):
    variableData: std.vector[cGcMaintenanceContainer]
    syncMessageMaxSize: int

cGcMaintenanceBuffer._fields_ = [
    ("variableData", std.vector[cGcMaintenanceContainer]),
    ("syncMessageMaxSize", ctypes.c_int32),
    ("endpadding", ctypes.c_ubyte * 0x4),
]


class cGcGalacticVoxelCoordinate(ctypes.Structure):
    X: int
    Z: int
    Y: int
    valid: bool

cGcGalacticVoxelCoordinate._fields_ = [
    ("X", ctypes.c_int16),
    ("Z", ctypes.c_int16),
    ("Y", ctypes.c_int16),
    ("valid", ctypes.c_ubyte),
]


class sVisitedSystem(ctypes.Structure):
    voxel: "cGcGalacticVoxelCoordinate"
    systemIndex: int
    planetsVisited: int

sVisitedSystem._fields_ = [
    ("voxel", cGcGalacticVoxelCoordinate),
    ("systemIndex", ctypes.c_int16),
    ("planetsVisited", ctypes.c_uint16),
]


class cGcVisitedSystemsBuffer(ctypes.Structure):
    visitedSystems: list[sVisitedSystem]
    currentPosition: int
    visitedSystemsCount: int

cGcVisitedSystemsBuffer._fields_ = [
    ("visitedSystems", sVisitedSystem * 0x200),
    ("currentPosition", ctypes.c_int32),
    ("visitedSystemsCount", ctypes.c_int32),
]


class cGcPersistentInteractionsManager(ctypes.Structure):
    baseBuildingBuffer: "cGcBaseBuildingGlobalBuffer"
    persistentBaseBuffers: std.vector[cGcPlayerBasePersistentBuffer]
    distressSignalBuffer: "cGcPersistentInteractionBuffer"
    crateBuffer: "cGcPersistentInteractionBuffer"
    destructableBuffer: "cGcPersistentInteractionBuffer"
    costBuffer: "cGcPersistentInteractionBuffer"
    buildingBuffer: "cGcPersistentInteractionBuffer"
    creatureBuffer: "cGcPersistentInteractionBuffer"
    personalBuffer: "cGcPersistentInteractionBuffer"
    fireteamSyncBuffer: "cGcPersistentInteractionBuffer"
    terrainEditBuffer: "cGcTerrainEditsPersistentBuffer"
    tradingSupplyBuffer: "cGcTradingSupplyBuffer"
    maintenanceBuffer: "cGcMaintenanceBuffer"
    personalMaintenanceBuffer: "cGcMaintenanceBuffer"
    visitedSystemsBuffer: "cGcVisitedSystemsBuffer"

cGcPersistentInteractionsManager._fields_ = [
    ("baseBuildingBuffer", cGcBaseBuildingGlobalBuffer),
    ("persistentBaseBuffers", std.vector[cGcPlayerBasePersistentBuffer]),
    ("padding0x1C18", ctypes.c_ubyte * 0x8),
    ("distressSignalBuffer", cGcPersistentInteractionBuffer),
    ("crateBuffer", cGcPersistentInteractionBuffer),
    ("destructableBuffer", cGcPersistentInteractionBuffer),
    ("costBuffer", cGcPersistentInteractionBuffer),
    ("buildingBuffer", cGcPersistentInteractionBuffer),
    ("creatureBuffer", cGcPersistentInteractionBuffer),
    ("personalBuffer", cGcPersistentInteractionBuffer),
    ("fireteamSyncBuffer", cGcPersistentInteractionBuffer),
    ("terrainEditBuffer", cGcTerrainEditsPersistentBuffer),
    ("tradingSupplyBuffer", cGcTradingSupplyBuffer),
    ("maintenanceBuffer", cGcMaintenanceBuffer),
    ("personalMaintenanceBuffer", cGcMaintenanceBuffer),
    ("visitedSystemsBuffer", cGcVisitedSystemsBuffer),
]


class cGcInventoryStoreBalance(ctypes.Structure):
    playerPersonalInventoryTechWidth: int
    playerPersonalInventoryTechHeight: int
    playerPersonalInventoryCargoWidth: int
    playerPersonalInventoryCargoHeight: int
    deconstructRefundPercentage: float

cGcInventoryStoreBalance._fields_ = [
    ("playerPersonalInventoryTechWidth", ctypes.c_int32),
    ("playerPersonalInventoryTechHeight", ctypes.c_int32),
    ("playerPersonalInventoryCargoWidth", ctypes.c_int32),
    ("playerPersonalInventoryCargoHeight", ctypes.c_int32),
    ("deconstructRefundPercentage", ctypes.c_float),
]


class cGcRichPresence(IStatWatcher, ctypes.Structure):
    onPlanet: bool
    stormActive: bool
    playerOutside: bool

cGcRichPresence._fields_ = [
    ("onPlanet", ctypes.c_ubyte),
    ("stormActive", ctypes.c_ubyte),
    ("playerOutside", ctypes.c_ubyte),
    ("endpadding", ctypes.c_ubyte * 0x7)
]


class cGcGameState(ctypes.Structure):
    class SaveThreadData(ctypes.Structure):
        gameState: _Pointer["cGcGameState"]
        _meSaveReason: ctypes.c_int32
        showMessage: bool
        fullSave: bool
        # playerStateDataToSave: "cGcPlayerStateData"
        # saveMaskFlagsToRemove: int


    RRIT: _Pointer["cGcRpcCallBase"]
    RRCE: _Pointer["cGcRpcCallBase"]
    RRBB: _Pointer["cGcRpcCallBase"]
    gameStateGroupNode: common.TkHandle
    playerState: "cGcPlayerState"
    savedSpawnState: "cGcPlayerSpawnStateData"
    playerShipOwnership: "cGcPlayerShipOwnership"
    playerVehicleOwnership: "cGcPlayerVehicleOwnership"
    playerCreatureOwnership: "cGcPlayerCreatureOwnership"
    playerMultitoolOwnership: "cGcPlayerMultitoolOwnership"
    playerFreighterOwnership: bytes
    playerFleetManager: bytes
    playerSquadronOwnership: "cGcPlayerSquadronOwnership"
    gameKnowledge: "cGcGameKnowledge"
    discoveryManager: bytes  # cGcDiscoveryManager
    wonderManager: bytes  # cGcWonderManager
    graveManager: "cGcGraveManager"
    msgBeaconManager: "cGcMsgBeaconManager"
    playerDiscoveryHelper: "cGcPlayerDiscoveryHelper"
    statsManager: bytes  # cGcStatsManager
    telemetryManager: bytes  # cGcTelemetryManager
    userSettings: bytes  # cGcUserSettings
    userSeenItemsState: "cGcUserSeenItemsState"
    difficultySettings: "cGcDifficultySettings"
    mPMissionTracker: bytes  # cGcMPMissionTracker
    entitlementManager: "cGcEntitlementManager"
    planetMappingManager: "cGcPlanetMappingManager"
    settlementStateManager: "cGcSettlementStateManager"
    saveStateDisplayTime: float
    _meSaveStateLastResult: ctypes.c_int32
    lastSaveOperationTimestamp: int
    restoreRequested: bool
    _meRestoreType: ctypes.c_int32
    savedInteractionsManager: "cGcPersistentInteractionsManager"
    pendingProgressWrite: bool
    delayedMicroSave: bool
    pendingDifficultySave: bool
    restartAllInactiveSeasonalMissions: bool
    _mePatchVersion: ctypes.c_int32
    patchAffectsLoading: bool
    warpTunnelRes: common.cTkSmartResHandle
    teleportTunnelRes: common.cTkSmartResHandle
    blackHoleTunnelRes: common.cTkSmartResHandle
    portalTunnelRes: common.cTkSmartResHandle
    placeMarkerRes: common.cTkSmartResHandle
    inventoryStoreBalance: "cGcInventoryStoreBalance"
    playerRichPresence: "cGcRichPresence"
    singleMultiPositionInSync: bool
    saveCompletedThisFrame: bool
    startedSaveTime: float
    saveThreadData: _Pointer["cGcGameState.SaveThreadData"]
    saveThreadId: int
    saveRequestNewEvent: int
    saveThreadExitedEvent: int
    saveThreadRequestExit: bool
    pendingAsyncSaveRequest: bool
    _mePendingAsyncSaveRequestReason: ctypes.c_int32
    pendingAsyncSaveRequestShowMessage: bool
    upgradeMessageFilterTimer: float
    networkClientLoad: bool
    lastDeathTriggeredSlotSelect: bool
    waitingForSeasonalGameMode: bool
    # cloudSaveManager: "cGcCloudSaveManager"


cGcGameState.SaveThreadData._fields_ = [
    ("gameState", ctypes.POINTER(cGcGameState)),
    ("_meSaveReason", ctypes.c_int32),
    ("showMessage", ctypes.c_ubyte),
    ("fullSave", ctypes.c_ubyte),
    ("padding0xE", ctypes.c_ubyte * 0x2),
    # ("playerStateDataToSave", cGcPlayerStateData),
    # ("saveMaskFlagsToRemove", ctypes.c_uint32),
]


cGcGameState._fields_ = [
    ("RRIT", ctypes.POINTER(cGcRpcCallBase)),
    ("RRCE", ctypes.POINTER(cGcRpcCallBase)),
    ("RRBB", ctypes.POINTER(cGcRpcCallBase)),
    ("gameStateGroupNode", common.TkHandle),
    ("padding0x1C", ctypes.c_ubyte * 0x4),
    ("playerState", cGcPlayerState),
    ("padding_PS", ctypes.c_ubyte * (539968 - ctypes.sizeof(cGcPlayerState))),
    ("savedSpawnState", cGcPlayerSpawnStateData),
    ("playerShipOwnership", cGcPlayerShipOwnership),
    ("playerVehicleOwnership", cGcPlayerVehicleOwnership),
    ("playerCreatureOwnership", cGcPlayerCreatureOwnership),
    ("playerMultitoolOwnership", cGcPlayerMultitoolOwnership),
    ("playerFreighterOwnership", ctypes.c_ubyte * 0x3940),
    ("playerFleetManager", ctypes.c_ubyte * 0x10F00),
    ("playerSquadronOwnership", cGcPlayerSquadronOwnership),
    ("gameKnowledge", cGcGameKnowledge),
    ("discoveryManager", ctypes.c_ubyte * 96),  # cGcDiscoveryManager
    ("padding0x1977D8", ctypes.c_ubyte * 0x8),
    ("wonderManager", ctypes.c_ubyte * 217824),  # cGcWonderManager
    ("graveManager", cGcGraveManager),
    ("msgBeaconManager", cGcMsgBeaconManager),
    ("playerDiscoveryHelper", cGcPlayerDiscoveryHelper),
    ("statsManager", ctypes.c_ubyte * 368),  # cGcStatsManager
    ("telemetryManager", ctypes.c_ubyte * 400),  # cGcTelemetryManager
    ("padding0x1CCE08", ctypes.c_ubyte * 0x8),
    ("userSettings", ctypes.c_ubyte * 15424),  # cGcUserSettings
    ("userSeenItemsState", cGcUserSeenItemsState),
    ("difficultySettings", cGcDifficultySettings),
    ("mPMissionTracker", ctypes.c_ubyte * 360),  # cGcMPMissionTracker
    ("entitlementManager", cGcEntitlementManager),
    ("planetMappingManager", cGcPlanetMappingManager),
    ("settlementStateManager", cGcSettlementStateManager),
    ("saveStateDisplayTime", ctypes.c_float),
    ("_meSaveStateLastResult", ctypes.c_int32),
    ("lastSaveOperationTimestamp", ctypes.c_uint64),
    ("restoreRequested", ctypes.c_ubyte),
    ("padding0x1D17F1", ctypes.c_ubyte * 0x3),
    ("_meRestoreType", ctypes.c_int32),
    ("padding0x1D17F8", ctypes.c_ubyte * 0x8),
    ("savedInteractionsManager", cGcPersistentInteractionsManager),  # + 0x1906688
    ("pendingProgressWrite", ctypes.c_ubyte),
    ("delayedMicroSave", ctypes.c_ubyte),
    ("pendingDifficultySave", ctypes.c_ubyte),
    ("restartAllInactiveSeasonalMissions", ctypes.c_ubyte),
    ("_mePatchVersion", ctypes.c_int32),
    ("patchAffectsLoading", ctypes.c_ubyte),
    ("padding0x43C209", ctypes.c_ubyte * 0x3),
    ("warpTunnelRes", common.cTkSmartResHandle),
    ("teleportTunnelRes", common.cTkSmartResHandle),
    ("blackHoleTunnelRes", common.cTkSmartResHandle),
    ("portalTunnelRes", common.cTkSmartResHandle),
    ("placeMarkerRes", common.cTkSmartResHandle),
    ("inventoryStoreBalance", cGcInventoryStoreBalance),
    ("padding0x43C234", ctypes.c_ubyte * 0x4),
    ("playerRichPresence", cGcRichPresence),
    ("singleMultiPositionInSync", ctypes.c_ubyte),
    ("saveCompletedThisFrame", ctypes.c_ubyte),
    ("padding0x43C24A", ctypes.c_ubyte * 0x2),
    ("startedSaveTime", ctypes.c_float),
    ("saveThreadData", ctypes.POINTER(cGcGameState.SaveThreadData)),
    ("saveThreadId", ctypes.c_uint32),
    ("padding0x43C25C", ctypes.c_ubyte * 0x4),
    ("saveRequestNewEvent", ctypes.c_void_p),
    ("saveThreadExitedEvent", ctypes.c_void_p),
    ("saveThreadRequestExit", ctypes.c_ubyte),
    ("pendingAsyncSaveRequest", ctypes.c_ubyte),
    ("padding0x43C272", ctypes.c_ubyte * 0x2),
    ("_mePendingAsyncSaveRequestReason", ctypes.c_int32),
    ("pendingAsyncSaveRequestShowMessage", ctypes.c_ubyte),
    ("padding0x43C279", ctypes.c_ubyte * 0x3),
    ("upgradeMessageFilterTimer", ctypes.c_float),
    ("networkClientLoad", ctypes.c_ubyte),
    ("lastDeathTriggeredSlotSelect", ctypes.c_ubyte),
    ("waitingForSeasonalGameMode", ctypes.c_ubyte),
    ("padding0x43C283", ctypes.c_ubyte * 0x5),
    # ("cloudSaveManager", cGcCloudSaveManager),
]


class cGcApplication(cTkFSM, ctypes.Structure):
    """The Main Application structure"""
    class Data(ctypes.Structure):
        """Much of the associated application data"""
        FirstBootContext: cGcFirstBootContext
        TkMcQmcLFSRStore: bytes
        RealityManager: cGcRealityManager
        GameState: cGcGameState
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
    ("GameState", cGcGameState),
    ("_paddingGS", ctypes.c_ubyte * (0x43c560 - ctypes.sizeof(cGcGameState))),
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