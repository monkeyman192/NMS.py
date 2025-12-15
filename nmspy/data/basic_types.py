import ctypes
from logging import getLogger
from typing import Union, TypeVar, Generic, Generator, Any, Type
import types

from pymhf.extensions.cpptypes import std
from pymhf.core.memutils import map_struct, get_addressof


logger = getLogger()


CTYPES = Union[ctypes._SimpleCData, ctypes.Structure, ctypes._Pointer]

T = TypeVar("T", bound=CTYPES)
T1 = TypeVar("T1", bound=CTYPES)
T2 = TypeVar("T2", bound=CTYPES)
N = TypeVar("N", bound=int)


FNV_offset_basis = 0xCBF29CE484222325
FNV_prime = 0x100000001B3


def fnv_1a(input: str, length: int):
    _input = input.ljust(length, "\x00")
    _hash = FNV_offset_basis
    for char in _input:
        _hash = (ord(char) ^ _hash) & 0xFFFFFFFFFFFFFFFF
        _hash = (_hash * FNV_prime) & 0xFFFFFFFFFFFFFFFF
    return _hash


# TODO: Rewrite a bit?
class cTkBitArray(ctypes.Structure, Generic[T, N]):
    _size: int
    _template_type: T
    _type_size: int
    array: list[T]

    def __class_getitem__(cls: Type["cTkBitArray"], key: tuple[Type[T], int]):
        _type, _size = key
        _cls: type[cTkBitArray] = types.new_class(
            f"cTkBitArray<{_type}, {_size}>", (cls,)
        )
        _cls._size = _size
        _cls._template_type = _type
        _cls._type_size = 8 * ctypes.sizeof(_type)
        _cls._fields_ = [("array", _type * (_size // _cls._type_size))]
        return _cls

    def __getitem__(self, key: int) -> bool:
        """Determine if the particular value is in the bitarray."""
        # Get the chunk the value lies in.
        if key >= self._size:
            raise ValueError("key is too large for this datatype")
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

    def __eq__(self, other: "cTkBitArray"):
        return self.ones() == other.ones()

    def __str__(self):
        """A string representation.
        This will be an "unwrapped" version of how it's actually represented in
        memory so that the bits can be read from right to left instead of in
        strides like how they are in memory.
        """
        res = ""
        for val in self.array:
            res = bin(int(val))[2:].zfill(self._type_size) + " " + res
        return res


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

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

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
            raise NotImplementedError(
                "To multiply two vectors, use a @ b to compute the dot product"
            )
        return Vector3f(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, other: Union[float, int]):
        return self * other

    def __matmul__(self, other: "Vector3f") -> float:
        """Dot product"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __neg__(self):
        return Vector3f(-self.x, -self.y, -self.z)

    def __repr__(self):
        return f"Vector3f({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        return f"<{self.x, self.y, self.z}>"

    def __json__(self) -> dict:
        return {"x": self.x, "y": self.y, "z": self.z}

    def normalise(self) -> "Vector3f":
        """Return a normalised version of the vector."""
        return ((self.x**2 + self.y**2 + self.z**2) ** (-0.5)) * Vector3f(
            self.x, self.y, self.z
        )

    def __len__(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** (0.5)


cTkVector3 = Vector3f


class Vector4f(ctypes.Structure):
    x: float
    y: float
    z: float
    w: float

    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("w", ctypes.c_float),
    ]


class Vector4i(ctypes.Structure):
    x: int
    y: int
    z: int
    w: int

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

    _fields_ = [
        ("x", ctypes.c_uint16),
        ("y", ctypes.c_uint16),
        ("z", ctypes.c_uint16),
        ("w", ctypes.c_uint16),
    ]


class cTkPhysRelVec3(ctypes.Structure):
    local: Vector3f
    offset: Vector3f
    _fields_ = [
        ("local", Vector3f),
        ("offset", Vector3f),
    ]

    def __str__(self):
        return f"<{self.__qualname__}; local: {str(self.local)}, offset: {str(self.offset)}"


class GcResource(ctypes.Structure):
    ResourceID: int
    _fields_ = [("ResourceID", ctypes.c_int32)]


class GcNodeID(ctypes.Structure):
    NodeID: int
    _fields_ = [("NodeID", ctypes.c_int32)]


class GcSeed(ctypes.Structure):
    Seed: int
    UseSeedValue: bool
    _fields_ = [
        ("Seed", ctypes.c_longlong),
        ("UseSeedValue", ctypes.c_ubyte),
        ("padding0x9", ctypes.c_ubyte * 0x7),
    ]


class Colour(ctypes.Structure):
    r: float
    g: float
    b: float
    a: float

    _fields_ = [
        ("r", ctypes.c_float),
        ("g", ctypes.c_float),
        ("b", ctypes.c_float),
        ("a", ctypes.c_float),
    ]


class Colour32(ctypes.Structure):
    r: int
    g: int
    b: int
    a: int

    _fields_ = [
        ("r", ctypes.c_byte),
        ("g", ctypes.c_byte),
        ("b", ctypes.c_byte),
        ("a", ctypes.c_byte),
    ]


class TkID(ctypes.Structure):
    """TkID<128> -> TkID[0x10], TkID<256> -> TkID[0x20]"""

    _align_ = 0x10  # One day this will work...
    _size: int  # This should only ever be 0x10 or 0x20...
    value: bytes

    def __class_getitem__(cls: type["TkID"], key: int):
        _cls: type["TkID"] = types.new_class(f"TkID<0x{key:X}>", (cls,))
        _cls._size = key
        _cls._fields_ = [("value", ctypes.c_char * _cls._size)]
        return _cls

    def __str__(self) -> str:
        return self.value.decode()

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return fnv_1a(str(self), self._size)


class cTkFixedWString(ctypes.Structure):
    """Equivalent of cTkFixedString<N,wchar_t>"""

    _size: int
    value: bytes

    def set(self, val: str):
        """Set the value of the string."""
        new_len = len(val)
        self.value = val[: self._size].encode() + (self._size - new_len) * b"\x00"

    def __class_getitem__(cls: type["cTkFixedWString"], key: int):
        _cls: type["cTkFixedWString"] = types.new_class(
            f"cTkFixedWString<0x{key:X}>", (cls,)
        )
        _cls._size = key
        _cls._fields_ = [("value", ctypes.c_wchar * key)]
        return _cls

    def __str__(self) -> str:
        return self.value.decode()

    def __eq__(self, other: str) -> bool:
        return str(self) == other

    def __repr__(self) -> str:
        return str(self)


class cTkFixedString(ctypes.Structure):
    """Equivalent of cTkFixedString<N,char_t>"""

    _size: int
    value: bytes

    def set(self, val: str):
        """Set the value of the string."""
        new_len = len(val)
        self.value = val[: self._size].encode() + (self._size - new_len) * b"\x00"

    def __class_getitem__(cls: type["cTkFixedString"], key: int):
        _cls: type["cTkFixedString"] = types.new_class(
            f"cTkFixedString<0x{key:X}>", (cls,)
        )
        _cls._size = key
        _cls._fields_ = [("value", ctypes.c_char * key)]
        return _cls

    def __str__(self) -> str:
        return self.value.decode()

    def __eq__(self, other: str) -> bool:
        return str(self) == other

    def __repr__(self) -> str:
        return str(self)


class TkHandle(ctypes.Union):
    class TkHandleSub(ctypes.Structure):
        _fields_ = [
            ("lookup", ctypes.c_uint32, 18),
            ("incrementor", ctypes.c_uint32, 14),
        ]

    _anonymous_ = ("_sub",)
    _fields_ = [("_sub", TkHandleSub), ("lookupInt", ctypes.c_uint32)]
    lookupInt: int

    def __json__(self) -> dict:
        return {"lookupInt": self.lookupInt}


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


class cTkAABB(ctypes.Structure):
    min: Vector3f
    max: Vector3f
    _fields_ = [
        ("min", Vector3f),
        ("max", Vector3f),
    ]


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


class cTkDynamicArray(ctypes.Structure, Generic[T]):
    _template_type: Type[T]
    _fields_ = [
        ("Array", ctypes.c_uint64),
        ("Size", ctypes.c_uint32),
        ("AllocatedFromData", ctypes.c_ubyte),
        ("_magicPad", ctypes.c_char * 0x3),
    ]

    Array: int
    Size: int
    allocatedFromData: bool

    @property
    def value(self) -> ctypes.Array[T]:
        if self.Array == 0 or self.Size == 0:
            # Empty lists are stored with an empty pointer in mem.
            return (self._template_type * 0)()
        return map_struct(self.Array, self._template_type * self.Size)

    def set(self, data: ctypes.Array[T]):
        self.Array = get_addressof(data)
        self.Size = len(data) + 1

    def __iter__(self) -> Generator[T, None, None]:
        # TODO: Improve to generate as we go.
        for obj in self.value:
            yield obj

    def __getitem__(self, i: int) -> T:
        return self.value[i]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.Size})"

    def __class_getitem__(cls: type["cTkDynamicArray"], key: Union[tuple[T], Any]):
        _cls: type["cTkDynamicArray"] = types.new_class(
            f"cTkDynamicArray<{key}>", (cls,)
        )
        _cls._template_type = key
        return _cls

    def __len__(self) -> int:
        return self.Size


class cTkClassPointer(ctypes.Structure):
    class cTkClassPointerData(ctypes.Union):
        _fields_ = [("class_", ctypes.c_void_p), ("offset", ctypes.c_longlong)]

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
        _cls: type[cTkListNode] = types.new_class(
            f"cTkListNode<{_type1}, {_type2}>", (cls,)
        )
        _cls._template_type1 = _type1
        _cls._template_type2 = _type2
        _cls._fields_ = [
            ("_value", std.pair[_type1, _type2]),
            ("hash", ctypes.c_uint64),
            ("_next", ctypes.c_uint64),
            ("_prev", ctypes.c_uint64),
            ("used", ctypes.c_ubyte),
        ]
        return _cls

    @property
    def value(self):
        return (self._value.first, self._value.second)

    @property
    def next(self):
        if self._next:
            return map_struct(
                self._next, cTkListNode[self._template_type1, self._template_type2]
            )

    @property
    def prev(self):
        if self._prev:
            return map_struct(
                self._prev, cTkListNode[self._template_type1, self._template_type2]
            )


class cTkLinearHashTable(ctypes.Structure, Generic[T1, T2]):
    capacity: int
    size: int
    tableSize: int

    def __class_getitem__(
        cls: Type["cTkLinearHashTable"], key: tuple[Type[T1], Type[T2]]
    ):
        _type1, _type2 = key
        _cls: type[cTkLinearHashTable] = types.new_class(
            f"cTkLinearHashTable<{_type1}, {_type2}>", (cls,)
        )
        _cls._fields_ = [
            ("nodes", ctypes.POINTER(cTkListNode[_type1, _type2])),
            (
                "bucketTable",
                ctypes.POINTER(ctypes.POINTER(cTkListNode[_type1, _type2])),
            ),
            ("firstFreeNode", ctypes.POINTER(cTkListNode[_type1, _type2])),
            ("capacity", ctypes.c_int32),
            ("size", ctypes.c_int32),
            ("tableSize", ctypes.c_int32),
        ]
        return _cls


class halfVector4(ctypes.Structure):
    pass


class HashedString(ctypes.Structure):
    pass


class NMSTemplate(ctypes.Structure):
    pass


class LinkableNMSTemplate(ctypes.Structure):
    pass


class VariableSizeString(cTkDynamicArray[ctypes.c_char]):
    @property
    def value(self) -> str:
        return super().value.value.decode()

    def __str__(self):
        return self.value


class VariableSizeWString(cTkDynamicArray[ctypes.c_wchar]):
    @property
    def value(self) -> str:
        return super().value.value.decode()

    def __str__(self):
        return self.value


# Aliases
cTkSeed = GcSeed
# String type aliases
TkID0x10 = TkID[0x10]
TkID0x20 = TkID[0x20]
cTkFixedString0x20 = cTkFixedString[0x20]
cTkFixedString0x40 = cTkFixedString[0x40]
cTkFixedString0x80 = cTkFixedString[0x80]
cTkFixedString0x100 = cTkFixedString[0x100]
cTkFixedString0x200 = cTkFixedString[0x200]
cTkFixedString0x400 = cTkFixedString[0x400]
cTkFixedString0x800 = cTkFixedString[0x800]
cTkFixedWString0x20 = cTkFixedWString[0x20]
cTkFixedWString0x40 = cTkFixedWString[0x40]
cTkFixedWString0x80 = cTkFixedWString[0x80]
cTkFixedWString0x100 = cTkFixedWString[0x100]
cTkFixedWString0x200 = cTkFixedWString[0x200]
cTkFixedWString0x400 = cTkFixedWString[0x400]
cTkFixedWString0x800 = cTkFixedWString[0x800]
# Vector type aliases
cTkBigPos = cTkPhysRelVec3
