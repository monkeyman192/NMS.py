import logging

import ctypes
import types
from typing import Any, Union, TypeVar, Generic, Type, Annotated

from nmspy.data.cpptypes import std

# from nmspy.hashing import fnv_1a

CTYPES = Union[ctypes._SimpleCData, ctypes.Structure, ctypes._Pointer]

T = TypeVar("T", bound=CTYPES)
T1 = TypeVar("T1", bound=CTYPES)
T2 = TypeVar("T2", bound=CTYPES)
N = TypeVar("N", bound=int)


class Colour(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float)
    ]


class Vector2f(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]


class Vector3f(ctypes.Structure):
    x: float
    y: float
    z: float

    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("_padding", ctypes.c_byte * 0x4),
    ]

    def __iadd__(self, other: "Vector3f"):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __add__(self, other: "Vector3f"):
        return Vector3f(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3f"):
        return Vector3f(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: Union[float, int]):
        if isinstance(other, Vector3f):
            raise NotImplementedError("To multiply two vectors, use a @ b to compute the dot product")
        return Vector3f(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, other: Union[float, int]):
        return self * other

    def __matmul__(self, other: "Vector3f") -> float:
        """ Dot product """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __neg__(self):
        return Vector3f(-self.x, -self.y, -self.z)

    def __repr__(self):
        return f"Vector3f({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        return f"<{self.x, self.y, self.z}>"

    def __json__(self) -> dict:
        return {"x": self.x, "y": self.y, "z": self.z}


class cTkPhysRelVec3(ctypes.Structure):
    local: Vector3f
    offset: Vector3f
    _fields_ = [
        ("local", Vector3f),
        ("offset", Vector3f),
    ]

# class VmaAllocation_T__BlockAllocation(ctypes.Structure):
#     pass


# class VmaAllocation_T__DedicatedAllocation(ctypes.Structure):
#     pass


# class VmaAllocation_T(ctypes.Structure):
#     class _sub(ctypes.Union):
#         _fields_ = [
#             ("m_BlockAllocation", VmaAllocation_T__BlockAllocation),
#             ("m_DedicatedAllocation", VmaAllocation_T__DedicatedAllocation),
#         ]
#     _anonymous_ = ("_sub",)
#     _fields_ = [
#         ("m_Alignment", ctypes.c_uint64),
#         ("m_Size", ctypes.c_uint64),
#         ("m_pUserData", ctypes.c_void_p),
#         ("m_LastUseFrameIndex", ctypes.c_uint32),
#         ("m_Type", ctypes.c_uint8),
#         ("m_SuballocationType", ctypes.c_uint8),
#         ("m_MapCount", ctypes.c_uint8),
#         ("m_Flags", ctypes.c_uint8),
#         ("_sub", _sub),
#         ("m_CreationFrameIndex", ctypes.c_uint32),
#         ("m_BufferImageUsage", ctypes.c_uint32),
#     ]


class cTkMatrix44(ctypes.Union):
    _fields_ = [
        ("c", (ctypes.c_float * 4) * 4),
        ("x", (ctypes.c_float * 16)),
    ]


class TkShaderConstHandle(ctypes.Structure):
    class _sub(ctypes.Union):
        class _sub_sub(ctypes.Structure):
            _fields_ = [
                ("vertexSlot", ctypes.c_char),
                ("fragmentSlot", ctypes.c_char),
            ]
        _anonymous_ = ("_sub_sub",)
        _fields_ = [
            ("_sub_sub", _sub_sub),
            ("valid", ctypes.c_uint32),
        ]
    _anonymous_ = ("_sub",)
    _fields_ = [
        ("_sub", _sub),
        ("offset", ctypes.c_uint16),
        ("isCustomPerMaterial", ctypes.c_ubyte),
        ("uniformBufferMask", ctypes.c_uint8),
    ]


class cTkMatrix34(ctypes.Structure):
    right: Vector3f
    up: Vector3f
    at: Vector3f
    pos: Vector3f

    _fields_ = [
        ("right", Vector3f),
        ("up", Vector3f),
        ("at", Vector3f),
        ("pos", Vector3f),
    ]

    @property
    def matrix(self):
        return (
            (self.right.x, self.right.y, self.right.z, 0),
            (self.up.x, self.up.y, self.up.z, 0),
            (self.at.x, self.at.y, self.at.z, 0),
            (self.pos.x, self.pos.y, self.pos.z, 1),
        )

    def __str__(self) -> str:
        return f"<right: {str(self.right)}, up: {str(self.up)}, at: {str(self.at)}, pos: {str(self.pos)}>"


class Vector4f(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("w", ctypes.c_float),
    ]


class Vector4i(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int32),
        ("y", ctypes.c_int32),
        ("z", ctypes.c_int32),
        ("w", ctypes.c_int32),
    ]


class cTkHalfVector4(ctypes.Structure):
    x: int
    y: int
    z: int
    w: int

cTkHalfVector4._fields_ = [
    ("x", ctypes.c_uint16),
    ("y", ctypes.c_uint16),
    ("z", ctypes.c_uint16),
    ("w", ctypes.c_uint16),
]


class GcSeed(ctypes.Structure):
    Seed: int
    UseSeedValue: bool
    _fields_ = [
        ("Seed", ctypes.c_longlong),
        ("UseSeedValue", ctypes.c_ubyte),
        ("padding0x9", ctypes.c_ubyte * 0x7)
    ]


class Quaternion(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("w", ctypes.c_float),
    ]


class TkHandle(ctypes.Union):
    class TkHandleSub(ctypes.Structure):
        _fields_ = [
            ("lookup", ctypes.c_uint32, 18),
            ("incrementor", ctypes.c_uint32, 14),
        ]
    _anonymous_ = ("_sub",)
    _fields_ = [
        ("_sub", TkHandleSub),
        ("lookupInt", ctypes.c_uint32)
    ]
    lookupInt: int

class cTkSmartResHandle(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_int32)
    ]
    value: int


class cTkBBox2d(ctypes.Structure):
    min: Vector2f
    max: Vector2f
    _fields_ = [
        ("min", Vector2f),
        ("max", Vector2f),
    ]


class cTkAABB2D(ctypes.Structure):
    min: Vector2f
    max: Vector2f
    _fields_ = [
        ("min", Vector2f),
        ("max", Vector2f),
    ]


class cTkAABB(ctypes.Structure):
    min: Vector3f
    max: Vector3f
    _fields_ = [
        ("min", Vector3f),
        ("max", Vector3f),
    ]


class cTkDynamicArray(ctypes.Structure, Generic[T]):
    _template_type: T
    _fields_ = [
        ("array", ctypes.c_ulonglong),
        ("size", ctypes.c_uint32),
        ("allocatedFromData", ctypes.c_ubyte),
        ("_magicPad", ctypes.c_char * 0x3)
    ]

    Array: int
    Size: int
    allocatedFromData: bool

    @property
    def value(self) -> Any:
        from nmspy.memutils import map_struct

        if self.array == 0 or self.size == 0:
            # Empty lists are store with an empty pointer in mem.
            return []
        return map_struct(self.array, self._template_type * self.size)

    def __iter__(self):
        # TODO: Improve to generate as we go.
        for obj in self.value:
            yield obj

    def __getitem__(self, i: int) -> T:
        return self.value[i]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.size})"

    def __class_getitem__(cls: type["cTkDynamicArray"], key: Union[tuple[T], Any]):
        _cls: type["cTkDynamicArray"] = types.new_class(f"cTkDynamicArray<{key}>", (cls,))
        _cls._template_type = key
        return _cls

    def __len__(self) -> int:
        return self.size


class cTkDynamicString(ctypes.Structure):
    _fields_ = [
        ("array", ctypes.c_char_p),
        ("size", ctypes.c_uint32),
        ("allocatedFromData", ctypes.c_ubyte),
        ("_magicPad", ctypes.c_char * 0x3)
    ]

    array: bytes
    size: int
    allocatedFromData: bool

    @property
    def value(self) -> bytes:
        return self.array

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.size})"

    def __str__(self) -> str:
        return self.value.decode()

    def __len__(self) -> int:
        return self.size


class TkSmoothCD(ctypes.Structure, Generic[T]):
    _template_type: T
    velocity: T
    value: T

    def __class_getitem__(cls: type["TkSmoothCD"], key: T):
        _cls: type["TkSmoothCD"] = types.new_class(f"TkSmoothCD<{key}>", (cls,))
        _cls._template_type = key
        _cls._fields_ = [
            ("velocity", key),
            ("value", key)
        ]
        return _cls


class cTkNGuiElementID(ctypes.Structure):
    counter: int
    base: int
    frameRenderTracker: int
    perFrameUseCount: int


class cTkFrameData(ctypes.Structure, Generic[T]):
    _template_type: T
    set: bool
    value: T

    def __class_getitem__(cls: type["cTkUiDataMap"], key: T):
        _cls: type["cTkUiDataMap"] = types.new_class(f"cTkUiDataMap<{key}>", (cls,))
        _cls._template_type = key
        _cls._fields_ = [
            ("velocity", std.vector[cls._template_type]),
            ("elementIndices", std.vector[cTkNGuiElementID])
        ]
        return _cls

# cTkStackVector<bool,1,-1>
# StackContainer<
#    std::vector<bool,StackAllocator<bool,1,-1> >
#    ,1,-1>


class cTkStackVector(ctypes.Structure, Generic[T]):
    _template_type: T
    set: bool
    value: T

    def __class_getitem__(cls: type["cTkStackVector"], key: T):
        _cls: type["cTkStackVector"] = types.new_class(f"cTkStackVector<{key}>", (cls,))
        _cls._template_type = key
        _cls._fields_ = [
            ("velocity", std.vector[cls._template_type]),
            ("elementIndices", std.vector[cTkNGuiElementID])
        ]
        return _cls


class cTkUiDataMap(ctypes.Structure, Generic[T]):
    _template_type: T
    uiData: std.vector
    elementIndices: std.vector[cTkNGuiElementID]

    def __class_getitem__(cls: type["cTkUiDataMap"], key: Type[T]):
        _cls: type["cTkUiDataMap"] = types.new_class(f"cTkUiDataMap<{key}>", (cls,))
        _cls._template_type = key
        _cls._fields_ = [
            ("velocity", std.vector[cls._template_type]),
            ("elementIndices", std.vector[cTkNGuiElementID])
        ]
        return _cls


class TkID(ctypes.Structure):
    _align_ = 0x10  # One day this will work...
    _size: int  # This should only ever be 0x10 or 0x20...
    value: bytes

    def __class_getitem__(cls: type["TkID"], key: int):
        _cls: type["TkID"] = types.new_class(f"TkID<0x{key:X}>", (cls,))
        _cls._size = key
        _cls._fields_ = [
            ("value", ctypes.c_char * _cls._size)
        ]
        return _cls

    def __str__(self) -> str:
        return self.value.decode()

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return fnv_1a(str(self), self._size)


class cTkFixedString(ctypes.Structure):
    _size: int
    value: bytes

    def set(self, val: str):
        self.value = val[:self._size].encode()

    def __class_getitem__(cls: type["cTkFixedString"], key: int):
        _cls: type["cTkFixedString"] = types.new_class(f"cTkFixedString<0x{key:X}>", (cls,))
        _cls._size = key
        _cls._fields_ = [
            ("value", ctypes.c_char * key)
        ]
        return _cls

    def __str__(self) -> str:
        return self.value.decode()

    def __repr__(self) -> str:
        return str(self)


class cTkClassPool(ctypes.Structure, Generic[T, N]):
    _size: int
    _template_type: T
    pool: list[T]
    uniqueIds: list[int]
    roster: list[int]
    rosterPartition: int
    uniqueIDGenerator: int

    def __class_getitem__(cls: Type["cTkClassPool"], key: tuple[Type[T], int]):
        _type, _size = key
        _cls: Type[cTkClassPool[T, N]] = types.new_class(
            f"cTkClassPool<{_type}, {_size}>", (cls,)
        )
        _cls._fields_ = [  # type: ignore
            ("pool", _type * _size),
            ("uniqueIds", ctypes.c_int32 * _size),
            ("roster", ctypes.c_int32 * _size),
            ("rosterPartition", ctypes.c_int32),
            ("uniqueIDGenerator", ctypes.c_int32),
        ]
        return _cls


class cTkBitArray(ctypes.Structure, Generic[T, N]):
    _size: int
    _template_type: T
    _type_size: int
    array: list[T]

    def __class_getitem__(cls: Type["cTkBitArray"], key: tuple[Type[T], int]):
        _type, _size = key
        _cls: type[cTkBitArray] = types.new_class(f"cTkBitArray<{_type}, {_size}>", (cls,))
        _cls._size = _size
        _cls._template_type = _type
        _cls._type_size = 8 * ctypes.sizeof(_type)
        _cls._fields_ = [
            ("array", _type * (_size // _cls._type_size))
        ]
        return _cls

    def __getitem__(self, key: int) -> bool:
        """ Determine if the particular value is in the bitarray."""
        # Get the chunk the value lies in.
        if key >= self._size:
            raise ValueError(f"key is too large for this datatype")
        idx = key // self._type_size
        subval = key & (self._type_size - 1)
        return (int(self.array[idx]) & (1 << subval)) != 0

    def __setitem__(self, key: int, value: bool):
        idx = idx = key // self._type_size
        subval = key & (self._type_size - 1)
        cval = int(self.array[idx])
        if value:
            # Set the bit
            cval = cval | (1 << subval)
        else:
            # Remove the bit
            cval = cval & (~(1 << subval))
        self.array[idx] = cval

    def ones(self) -> list[int]:
        return [i for i in range(self._size) if self[i]]

    def __str__(self):
        """ A string representation.
        This will be an "unwrapped" version of how it's actually represented in
        memory so that the bits can be read from right to left instead of in
        strides like how they are in memory.
        """
        res = ""
        for val in self.array:
            res = bin(int(val))[2:].zfill(self._type_size) + " " + res
        return res


class cTkClassPointer(ctypes.Structure):
    class cTkClassPointerData(ctypes.Union):
        _fields_ = [
            ("class_", ctypes.c_void_p),
            ("offset", ctypes.c_longlong)
        ]
    _fields_ = [
        ("classData", cTkClassPointerData),
        ("className", cTkFixedString[0x63]),
        ("classFixed", ctypes.c_ubyte),
        ("classNameHash", ctypes.c_uint64),
    ]
    classData: cTkClassPointerData
    className: cTkFixedString[0x63]
    classFixed: bool
    classNameHash: int


class cTkListNode(ctypes.Structure, Generic[T1, T2]):
    _template_type1: T1
    _template_type2: T2
    # This is techcnically cTkLinearHashTable<...>::cTkListNode, but this is
    # easier...
    # value: std.pair[T1, T2]
    hash: int
    _next: int
    _prev: int
    used: bool

    def __class_getitem__(cls: Type["cTkListNode"], key: tuple[Type[T1], Type[T2]]):
        _type1, _type2 = key
        _cls: type[cTkListNode] = types.new_class(f"cTkListNode<{_type1}, {_type2}>", (cls,))
        _cls._template_type1 = _type1
        _cls._template_type2 = _type2
        _cls._fields_ = [
            ("value", std.pair[_type1, _type2]),
            ("hash", ctypes.c_uint64),
            ("_next", ctypes.c_uint64),
            ("_prev", ctypes.c_uint64),
            ("used", ctypes.c_ubyte),
        ]
        return _cls

    @property
    def next(self):
        from nmspy.memutils import map_struct
        return map_struct(self._next, cTkListNode[self._template_type1, self._template_type2])

    @property
    def prev(self):
        from nmspy.memutils import map_struct
        return map_struct(self._prev, cTkListNode[self._template_type1, self._template_type2])


class cTkLinearHashTable(ctypes.Structure, Generic[T1, T2]):
    capacity: int
    size: int
    tableSize: int

    def __class_getitem__(cls: Type["cTkLinearHashTable"], key: tuple[Type[T1], Type[T2]]):
        _type1, _type2 = key
        _cls: type[cTkLinearHashTable] = types.new_class(f"cTkLinearHashTable<{_type1}, {_type2}>", (cls,))
        _cls._fields_ = [
            ("nodes", ctypes.POINTER(cTkListNode[_type1, _type2])),
            ("bucketTable", ctypes.POINTER(ctypes.POINTER(cTkListNode[_type1, _type2]))),
            ("firstFreeNode", ctypes.POINTER(cTkListNode[_type1, _type2])),
            ("capacity", ctypes.c_int32),
            ("size", ctypes.c_int32),
            ("tableSize", ctypes.c_int32),
        ]
        return _cls


if __name__ == "__main__":
    data = bytearray(b"\xFF\x10")
    m = cTkBitArray[ctypes.c_uint8, 16].from_buffer(data)
    print(m[3])
    print(str(m))
    m[3] = False
    print(str(m))
    m[8] = True
    print(str(m))
    print(m.ones())
