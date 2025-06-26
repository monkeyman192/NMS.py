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
    Text: Annotated[
        basic.cTkDynamicArray[ctypes.c_char],
        Field(basic.cTkDynamicArray[ctypes.c_char], 0x88),
    ]


class cGcScanEventData(Structure):
    pass


@partial_struct
class GcSolarSystemData(Structure):
    PlanetOrbits: Annotated[list[int], Field(ctypes.c_int32 * 8, 0x21D0)]


@partial_struct
class cGcInteractionComponentData(Structure):
    mInteractionType: Annotated[c_enum32[enums.GcInteractionType], 0x31C]


@partial_struct
class cGcPlanetGenerationInputData(Structure):
    CommonSubstance: Annotated[basic.cTkFixedString[0x10], 0x00]
    RareSubstance: Annotated[basic.cTkFixedString[0x10], 0x10]
    Seed: Annotated[basic.GcSeed, 0x20]
    Biome: Annotated[c_enum32[enums.GcBiomeType], 0x30]
