import ctypes
from typing import Type, TypeVar, Optional


MEM_ACCESS_R = 0x100   # Read only.
MEM_ACCESS_RW = 0x200  # Read and Write access.


ctypes.pythonapi.PyMemoryView_FromMemory.argtypes = (
    ctypes.c_char_p,
    ctypes.c_ssize_t,
    ctypes.c_int,
)
ctypes.pythonapi.PyMemoryView_FromMemory.restype = ctypes.py_object


# TypeVar for the map_struct so that we can correctly get the returned type to
# be the same as the input type.
Struct = TypeVar("Struct", bound=ctypes.Structure)


def pprint_mem(offset: int, size: int) -> str:
    _data = (ctypes.c_char * size).from_address(offset)
    return " ".join([k.hex().upper() for k in _data])


def get_memview(offset: int, type_: Type[ctypes.Structure]) -> Optional[memoryview]:
    """ Return a memoryview which covers the region of memory specified by the
    struct provided.

    Parameters
    ----------
    offset:
        The memory address to start reading the struct from.
    type_:
        The type of the ctypes.Structure to be loaded at this location.
    """
    if not offset:
        return None
    addr = ctypes.cast(offset, ctypes.c_char_p)
    return ctypes.pythonapi.PyMemoryView_FromMemory(
        addr,
        ctypes.sizeof(type_),
        MEM_ACCESS_RW,
    )


def map_struct(offset: int, type_: Type[Struct]) -> Struct:
    """ Return an instance of the `type_` struct provided which shares memory
    with the provided offset.
    Note that the amount of memory to read is automatically determined by the
    size of the struct provided.

    Parameters
    ----------
    offset:
        The memory address to start reading the struct from.
    type_:
        The type of the ctypes.Structure to be loaded at this location.

    Returns
    -------
    An instance of the input type.
    """
    if not offset:
        raise ValueError("Offset is 0. This would result in a segfault or similar")
    return type_.from_buffer(get_memview(offset, type_))
