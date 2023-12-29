import ctypes
import types
from typing import Any, TYPE_CHECKING, TypeVar, Generic, Union, Type


if TYPE_CHECKING:
    from ctypes import _Pointer

CTYPES = Union[ctypes._SimpleCData, ctypes.Structure, ctypes._Pointer]

T = TypeVar("T", bound=CTYPES)
N = TypeVar("N", bound=int)
T1 = TypeVar("T1", bound=CTYPES)
T2 = TypeVar("T2", bound=CTYPES)

# Good source of info for these:
# # https://devblogs.microsoft.com/search?query=inside+stl&blog=%2Foldnewthing%2F



class _array(ctypes.Structure, Generic[T, N]):
    _elements: list[T]
    def __class_getitem__(cls: Type["_array"], key: tuple[Type[T], int]):
        _type, _size = key
        _cls: Type[_array[T, N]] = types.new_class(
            f"std::aray<{_type}, {_size}>", (cls,)
        )
        _cls._fields_ = [  # type: ignore
            ("_elements", _type * _size),
        ]
        return _cls

    def __len__(self) -> int:
        return len(self._elements)

    def __getitem__(self, i: int) -> T:
        return self._elements[i]

    def __setitem__(self, i: int, val: T):
        self._elements[i] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

class _vb_val(ctypes.Structure, Generic[T]):
    #   std::vector<unsigned int,StackAllocator<unsigned int,1,-1> > _Myvec;
    # unsigned __int64 _Mysize;
    pass


class _vector(ctypes.Structure, Generic[T]):
    _template_type: T
    if TYPE_CHECKING:
        _first: _Pointer[Any]
        _last: _Pointer[Any]
        _end: _Pointer[Any]

    def __class_getitem__(cls: Type["_vector"], type_: Type[T]):
        _cls: Type[_vector[T]] = types.new_class(
            f"std::vector<{type_}>", (cls,)
        )
        _cls._template_type = type_
        _cls._fields_ = [  # type: ignore
            ("_first", ctypes.POINTER(type_)),
            ("_last", ctypes.POINTER(type_)),
            ("_end", ctypes.POINTER(type_)),
        ]
        return _cls

    def __len__(self) -> int:
        return (
            ctypes.addressof(self._last.contents) -
            ctypes.addressof(self._first.contents)
        ) // 0x8  # Assuming 64 bit architecture

    def __getitem__(self, i: int) -> T:
        return self._first[i]

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def clear(self):
        """
        Empty the vector. This will remove all references to the elements.
        USE THIS WISELY as is may cause issues.
        """
        nullptr = ctypes.POINTER(self._template_type)
        self._first = nullptr()
        self._last = nullptr()
        self._end = nullptr()

class _pair(ctypes.Structure, Generic[T1, T2]):
    first: T1
    second: T2

    def __class_getitem__(cls: Type["_pair"], key: tuple[Type[T1], Type[T2]]):
        first, second = key
        _cls: Type[_pair[T1, T2]] = types.new_class(
            f"std::pair<{first}, {second}>", (cls,)
        )
        _cls._fields_ = [  # type: ignore
            ("first", first),
            ("second", second),
        ]
        return _cls

# 0x40 long
class _unordered_map(ctypes.Structure, Generic[T1, T2]):

    """
    std::_Hash<
        std::_Umap_traits<
            TkID<128>,
            TkID<256>,
            std::_Uhash_compare<TkID<128>,
            TkIDUnorderedMap::Hash128,
            std::equal_to<TkID<128> >
        >,
        TkSTLAllocatorShim<
            std::pair<TkID<128> const ,TkID<256> >
            ,8,
            -1>
        ,
        0>
    >
    +0x00 std::_Umap_traits<TkID<128>,TkID<256>,std::_Uhash_compare<TkID<128>,TkIDUnorderedMap::Hash128,std::equal_to<TkID<128> > >,TkSTLAllocatorShim<std::pair<TkID<128> const ,TkID<256> >,8,-1>,0> _Traitsobj;
    +0x08 std::list<
            std::pair<
                TkID<128> const ,
                TkID<256>
            >,
            TkSTLAllocatorShim<
                std::pair<
                    TkID<128> const ,
                    TkID<256>
                >,
                8,
                -1
            >
          > _List;
    +0x18 std::_Hash_vec<TkSTLAllocatorShim<std::_List_unchecked_iterator<std::_List_val<std::_List_simple_types<std::pair<TkID<128> const ,TkID<256> > > > >,8,-1> > _Vec;
    +0x30 unsigned __int64 _Mask;
    +0x38 unsigned __int64 _Maxidx;
    """

    pass


class _list_node(ctypes.Structure, Generic[T]):
    """
    +0x00 std::_List_node<std::pair<TkID<128> const ,TkID<256> >,void *> *_Next;
    +0x08 std::_List_node<std::pair<TkID<128> const ,TkID<256> >,void *> *_Prev;
    +0x10 std::pair<TkID<128> const ,TkID<128> > _Myval;
    """
    if TYPE_CHECKING:
        _next: _Pointer["_list_node"]
        _myval: _pair

_list_node._fields_ = [
        ("_next", ctypes.POINTER(_list_node)),  # TEMP
        ("_prev", ctypes.POINTER(_list_node)),  # TEMP
        ("_myval", _pair)
    ]


# 0x10 long
class _list(ctypes.Structure, Generic[T]):
    """
        +0x00 std::_List_node<std::pair<TkID<128> const ,TkID<256> >,void *> *_Myhead;
        +0x08 unsigned __int64 _Mysize;
    """
    pass


class std:
    array = _array
    vector = _vector
    pair = _pair
    list = _list

# class STD:
#     class ARRAY():
#         def __new__(cls, type_: Type[T], size: int) -> std.array:
#             _cls = types.new_class(
#                 f"std::aray<{type_}, {size}>", (std.array,)
#             )
#             _cls._fields_ = [
#                 ("_elements", type_ * size),
#             ]
#             return _cls



if __name__ == "__main__":
    data = bytearray(b"\x01\x02\x00\x00\x07\x00\x00\x00")
    pear = std.pair[ctypes.c_uint32, ctypes.c_int32]
    k = pear.from_buffer(data)
    print(k.first)
    print(k.second)
    harry = std.array[ctypes.c_ubyte, 6]
    d = harry.from_buffer(data)
    for i in d:
        print(i)
    print('setting')
    d[3] = 9
    for i in d:
        print(i)

    # print("AAAAAAAAA")
    # arry = STD.ARRAY(ctypes.c_ubyte, 6)
    # pp = arry.from_buffer(data)
    # for i in pp:
    #     print(i)
