# This will be an auto-generated file by MBINCompiler for the current exe version.

import ctypes
from typing import Annotated

from pymhf.core.hooking import Structure
from pymhf.utils.partial_struct import partial_struct, Field, c_enum32

import nmspy.data.basic_types as basic
import nmspy.data.enums as enums


@partial_struct
class cGcSolarSystemData(Structure):
    PlanetPositions: Annotated[list[basic.Vector3f], Field(basic.Vector3f * 8, 0x1DE0)]
    PlanetOrbits: Annotated[list[int], Field(ctypes.c_int32 * 8, 0x21D0)]
    Planets: Annotated[int, Field(ctypes.c_int32, 0x2264)]


@partial_struct
class cGcNGuiTextData(Structure):
    Text: Annotated[basic.cTkDynamicArray[ctypes.c_char], 0x88]


class cGcScanEventData(Structure):
    pass


@partial_struct
class cGcInteractionComponentData(Structure):
    InteractionType: Annotated[c_enum32[enums.cGcInteractionType], 0x32C]


@partial_struct
class cGcPlanetGenerationInputData(Structure):
    CommonSubstance: Annotated[basic.cTkFixedString[0x10], 0x00]
    RareSubstance: Annotated[basic.cTkFixedString[0x10], 0x10]
    Seed: Annotated[basic.GcSeed, 0x20]
    Biome: Annotated[c_enum32[enums.cGcBiomeType], 0x30]


@partial_struct
class cGcPlanetData(Structure):
    Name: Annotated[basic.cTkFixedString[0x80], 0x395E]


class cGcCreatureRoleData(Structure):
    pass


class cGcCreatureSpawnData(Structure):
    pass


class cGcGalaxyVoxelAttributesData(Structure):
    pass


@partial_struct
class GcPlanetTradingData(Structure):
    TradingClass: Annotated[c_enum32[enums.cGcTradingClass], 0x0]
    WealthClass: Annotated[c_enum32[enums.cGcWealthClass], 0x4]


@partial_struct
class cGcGalaxyStarAttributesData(Structure):
    PlanetSeeds: Annotated[list[basic.GcSeed], Field(basic.GcSeed * 0x10, 0x000)]
    PlanetParentIndices: Annotated[list[int], Field(ctypes.c_int32 * 0x10, 0x100)]
    PlanetSizes: Annotated[
        list[enums.cGcPlanetSize], Field(c_enum32[enums.cGcPlanetSize] * 0x10, 0x140)
    ]
    TradingData: Annotated[GcPlanetTradingData, 0x180]
    Anomaly: Annotated[c_enum32[enums.cGcGalaxyStarAnomaly], 0x188]
    ConflictData: Annotated[c_enum32[enums.cGcPlayerConflictData], 0x18C]
    NumberOfPlanets: Annotated[ctypes.c_int32, 0x190]
    NumberOfPrimePlanets: Annotated[ctypes.c_int32, 0x194]
    Race: Annotated[c_enum32[enums.cGcAlienRace], 0x198]
    Type: Annotated[c_enum32[enums.cGcGalaxyStarTypes], 0x19C]
    AbandonedSystem: Annotated[ctypes.c_bool, 0x1A0]
    IsGasGiantSystem: Annotated[ctypes.c_bool, 0x1A1]
    IsGiantSystem: Annotated[ctypes.c_bool, 0x1A2]
    IsPirateSystem: Annotated[ctypes.c_bool, 0x1A3]
    IsSystemSafe: Annotated[ctypes.c_bool, 0x1A4]
