import ctypes
from typing import Any, Union

from nmspy.memutils import map_struct


class Colour(ctypes.Structure):
    _pack_ = 0x10
    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float)
    ]


class Vector2f(ctypes.Structure):
    _pack = 0x8
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]


class Vector3f(ctypes.Structure):
    _pack = 0x10
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
    ]


class Vector4f(ctypes.Structure):
    _pack = 0x10
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("w", ctypes.c_float),
    ]


class Vector4i(ctypes.Structure):
    _pack = 0x10
    _fields_ = [
        ("x", ctypes.c_int32),
        ("y", ctypes.c_int32),
        ("z", ctypes.c_int32),
        ("w", ctypes.c_int32),
    ]


class GcSeed(ctypes.Structure):
    _fields_ = [
        ("Seed", ctypes.c_longlong),
        ("UseSeedValue", ctypes.c_ubyte),
    ]


class Quaternion(ctypes.Structure):
    _pack = 0x10
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("w", ctypes.c_float),
    ]


class cTkDynamicArray(ctypes.Structure):
    _template_type = ctypes.c_char
    _fields_ = [
        ("mArray", ctypes.c_ulonglong),
        ("miSize", ctypes.c_uint32),
        ("mbAllocatedFromData", ctypes.c_ubyte),
        ("_macMagicPad", ctypes.c_char * 0x3)
    ]

    mArray: int
    miSize: int
    mbAllocatedFromData: bool

    @property
    def value(self) -> Any:
        if self.mArray == 0 or self.miSize == 0:
            # Empty lists are store with an empty pointer in mem.
            return []
        return map_struct(self.mArray, self._template_type * self.miSize)

    def __str__(self):
        str_val = [x.value for x in self.value]
        return f"cTkDynamicArray(value: {str_val}, size: 0x{self.miSize:X})"

    def __class_getitem__(cls: type["cTkDynamicArray"], key: Union[tuple[Any], Any]):
        cls._template_type = key
        return cls


class cTkDynamicString(ctypes.Structure):
    _fields_ = [
        ("mArray", ctypes.c_char_p),
        ("miSize", ctypes.c_uint32),
        ("mbAllocatedFromData", ctypes.c_ubyte),
        ("_macMagicPad", ctypes.c_char * 0x3)
    ]

    mArray: bytes
    miSize: int
    mbAllocatedFromData: bool

    @property
    def value(self) -> bytes:
        return self.mArray

    def __str__(self):
        val = self.value.decode()
        return f"cTkDynamicString(value: {val}, size: 0x{self.miSize:X})"
