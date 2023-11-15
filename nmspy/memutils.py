import ctypes
import array
import logging
import time
from typing import Type, TypeVar, Optional, Iterable, Union

from nmspy.common import BASE_ADDRESS, SIZE_OF_IMAGE


mem_logger = logging.getLogger("MemUtils")


MEM_ACCESS_R = 0x100   # Read only.
MEM_ACCESS_RW = 0x200  # Read and Write access.

BLOB_SIZE = 0x1_000_000  # 16Mb


ctypes.pythonapi.PyMemoryView_FromMemory.argtypes = (
    ctypes.c_char_p,
    ctypes.c_ssize_t,
    ctypes.c_int,
)
ctypes.pythonapi.PyMemoryView_FromMemory.restype = ctypes.py_object


# TODO: Move
class NMSStruct(ctypes.Structure):
    _offset: int


# TypeVar for the map_struct so that we can correctly get the returned type to
# be the same as the input type.
Struct = TypeVar("Struct", bound=ctypes.Structure)


def chunks(lst: Iterable, n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def match(patt: bytes, input: bytes):
    """ Check whether or not the pattern matches the provided bytes. """
    for i, char in enumerate(patt):
        if not (char == b'.' or char == input[i]):
            return False
    return True


def pprint_mem(offset: int, size: int, stride: Optional[int] = None) -> str:
    # TODO: Make this print a much nicer output... It sucks right now...
    if not offset:
        # If we are passed in an offset of 0, don't even try.
        return ""
    _data = (ctypes.c_char * size).from_address(offset)
    if stride:
        result = " ".join([f"{x:02X}".upper() for x in range(stride)]) + "\n"
        for chunk in chunks(_data, stride):
            result += " ".join([f"{k:02X}".upper() for k in chunk]) + "\n"
        return result
    else:
        return " ".join([k.hex().upper() for k in _data])


def get_addressof(obj) -> int:
    try:
        # If it's a pointer, this is the branc that is used.
        return ctypes.cast(obj, ctypes.c_void_p).value
    except:
        # TODO: Get correct error type.
        # Otherwise fallback to the usual method.
        return ctypes.addressof(obj)


def _get_memview(offset: int, type_: Type[ctypes.Structure]) -> memoryview:
    """ Return a memoryview which covers the region of memory specified by the
    struct provided.

    Parameters
    ----------
    offset:
        The memory address to start reading the struct from.
    type_:
        The type of the ctypes.Structure to be loaded at this location.
    """
    return ctypes.pythonapi.PyMemoryView_FromMemory(
        ctypes.cast(offset, ctypes.c_char_p),
        ctypes.sizeof(type_),
        MEM_ACCESS_RW,
    )


def _get_memview_with_size(offset: int, size: int) -> Optional[memoryview]:
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
    return ctypes.pythonapi.PyMemoryView_FromMemory(
        ctypes.cast(offset, ctypes.c_char_p),
        size,
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
    instance = type_.from_buffer(_get_memview(offset, type_))
    instance._offset = offset
    return instance


def pattern_to_bytes(patt: str) -> array.array:
    arr = array.array("H")
    for char in patt.split(" "):
        try:
            num = int(char, 0x10)
        except ValueError:
            num = -1
        if num > 0xFF:
            raise ValueError
        elif num == -1:
            num = 0x100
        arr.append(num)
    return arr


def find_bytes(
    pattern: str,
    start: Optional[int] = None,
    end: Optional[int] = None,
    alignment: int = 0x4,
    find_all: bool = False,
) -> Union[int, list[int], None]:
    if start is None:
        start = BASE_ADDRESS
    if end is None:
        end = start + SIZE_OF_IMAGE
    # Search memory as follows:
    # Read the requested bytes in (up to) 0x10 byte blobs.
    # For the first blob then loop over all the memory addresses reading from
    # start to finish.
    # If, at any given memory address we find the start memory to match, then
    # we continue to loop over the rest of the memory to see if it also matches.
    # If not, then return back to the first part of the data and continue
    # searching through memory.
    start_time = time.time()
    offsets = []
    _addr = start
    patt = pattern_to_bytes(pattern)
    # Loop over the whole region.
    while _addr < end:
        # Determine how much data we should read, and then read it into a
        # memoryview.
        _size = min(end - _addr, BLOB_SIZE)
        mv = _get_memview_with_size(_addr, _size)
        for i in range(_size // alignment):
            for j, char in enumerate(patt):
                # 0x100 is used as the "wildcard" since every byte will be from
                # 0 -> 0xFF, but we will store each in 2 bytes.
                if char == 0x100:
                    continue
                try:
                    if not mv[alignment * i + j] == char:
                        break
                except IndexError:
                    mem_logger.info(f"i: {i}, alignment: {alignment}, len: {len(mv)}, {alignment * i + j}")
                    raise
            else:
                # In this case we matched. Check to see if we want all or just
                # one.
                if find_all:
                    offsets.append(_addr + alignment * i)
                else:
                    mem_logger.info(f"Time to find pattern: {time.time() - start_time:.3f}s")
                    return _addr + alignment * i
        # Move forward by the alignment amount.
        _addr += BLOB_SIZE
    if find_all:
        return offsets
    else:
        return None
