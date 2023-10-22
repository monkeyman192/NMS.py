from ctypes import Structure, c_longlong
from ctypes.wintypes import FLOAT, BOOLEAN, INT


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


class Vector4i(Structure):
    _pack = 0x10
    _fields_ = [
        ("x", INT),
        ("y", INT),
        ("z", INT),
        ("w", INT),
    ]


class GcSeed(Structure):
    _fields_ = [
        ("Seed", c_longlong),
        ("UseSeedValue", BOOLEAN),
    ]


class Quaternion(Structure):
    _pack = 0x10
    _fields_ = [
        ("x", FLOAT),
        ("y", FLOAT),
        ("z", FLOAT),
        ("w", FLOAT),
    ]
