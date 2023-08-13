from ctypes import Structure, c_longlong
from ctypes.wintypes import FLOAT, BOOLEAN


class Colour(Structure):
    _pack_ = 0x10
    _fields_ = [
        ("r", FLOAT),
        ("g", FLOAT),
        ("b", FLOAT),
        ("a", FLOAT)
    ]


class Vector2f(Structure):
    _pack = 0x8
    _fields_ = [
        ("x", FLOAT),
        ("y", FLOAT),
    ]


class Vector3f(Structure):
    _pack = 0x10
    _fields_ = [
        ("x", FLOAT),
        ("y", FLOAT),
        ("z", FLOAT),
    ]


class Vector4f(Structure):
    _pack = 0x10
    _fields_ = [
        ("x", FLOAT),
        ("y", FLOAT),
        ("z", FLOAT),
        ("w", FLOAT),
    ]


class GcSeed(Structure):
    _fields_ = [
        ("Seed", c_longlong),
        ("UseSeedValue", BOOLEAN),
    ]
