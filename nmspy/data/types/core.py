# A collection of core internal types which, whilst you could consider common,
# They are specific to NMS, rather than beings "common" types such as colours.

import ctypes

class cTkSmartResHandle(ctypes.Structure):
    _fields_ = [
        ("InternalHandle", ctypes.c_int32),
    ]
    InternalHandle: int


class TkHandle(ctypes.Structure):
    _fields_ = [
        ("InternalHandle", ctypes.c_int32),
    ]
    InternalHandle: int
