from ctypes import CFUNCTYPE

import nmspy._internal as _internal
from nmspy.data.function_call_sigs import FUNC_CALL_SIGS
from nmspy.data import FUNC_OFFSETS
from nmspy._types import FUNCDEF


def call_function(name: str, *args, **kwargs):
    _sig = FUNC_CALL_SIGS[name]
    if isinstance(_sig, FUNCDEF):
        sig = CFUNCTYPE(_sig.restype, *_sig.argtypes)
    else:
        # TODO: Handle overloads
        raise NotImplementedError("Calling overloads not implemented yet... Sorry!")
    cfunc = sig(_internal.BASE_ADDRESS + FUNC_OFFSETS[name])
    return cfunc(*args, **kwargs)
