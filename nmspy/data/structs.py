from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from ctypes import _Pointer

import ctypes
import ctypes.wintypes

from nmspy.data import common
from nmspy.memutils import map_struct


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
    def members(self) -> Generator[cTkMetaDataMember]:
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
    ]


class cGcApplication(ctypes.Structure):
    """The Main Application structure"""
    class Data(ctypes.Structure):
        """Much of the associated application data"""
        _fields_ = [
            ("firstBootContext", cGcFirstBootContext)
        ]

    _fields_ = [
        ("baseclass_0", cTkFSM),
        ("data", ctypes.POINTER(Data)),
    ]

    baseclass_0: cTkFSM
    data: _Pointer[Data]


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
