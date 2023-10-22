# A collection of types which are "simple"
# They have no dependencies on other types but are still compound types with
# multiple fields.

import ctypes

class TkAudioID(ctypes.Structure):
    _fields_ = [
        ("mpacName", ctypes.c_char_p),
        ("muID", ctypes.c_uint32),
        ("mbValid", ctypes.c_ubyte),
    ]
    mpacName: bytes
    muID: int
    mbValid: bool
