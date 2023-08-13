import ctypes
import ctypes.wintypes

from nmspy.data import common


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


class cTkMetaDataClass(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("nameHash", ctypes.c_ulonglong),
        ("templateHash", ctypes.c_ulonglong),
        ("members", ctypes.c_ulonglong),
        ("numMembers", ctypes.c_int32),
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


class cGcApplication(ctypes.Structure):
    _fields_ = [
        ("baseclass_0", cTkFSM),
        ("Data", ctypes.c_longlong),
    ]


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
