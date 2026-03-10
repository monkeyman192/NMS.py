from ctypes import c_uint64, c_void_p
from typing import Annotated

from pymhf.core.hooking import Structure
from pymhf.utils.partial_struct import Field, partial_struct


@partial_struct
class VkBuffer_T(Structure):
    size: Annotated[int, Field(c_uint64, 0x0)]
    bytes_: Annotated[c_void_p, 0x8]
