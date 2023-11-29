from ctypes import CFUNCTYPE
from logging import getLogger
from typing import Optional

import nmspy._internal as _internal
from nmspy.data.function_call_sigs import FUNC_CALL_SIGS
from nmspy.data import FUNC_OFFSETS
from nmspy._types import FUNCDEF


calling_logger = getLogger("CallingManager")


def call_function(name: str, *args, overload: Optional[str] = None):
    _sig = FUNC_CALL_SIGS[name]
    offset = FUNC_OFFSETS[name]
    if isinstance(_sig, FUNCDEF):
        sig = CFUNCTYPE(_sig.restype, *_sig.argtypes)
    else:
        # Look up the overload:
        if (osig := _sig.get(overload)) is not None:  # type: ignore
            sig = CFUNCTYPE(osig.restype, *osig.argtypes)
        else:
            # Need to fallback on something. Raise a warning that no
            # overload was defined and that it will fallback to the
            # first entry in the dict.
            first = list(_sig.items())[0]
            calling_logger.warning(
                f"No function arguments overload was provided for {name}. "
            )
            calling_logger.warning(
                f"Falling back to the first overload ({first[0]})")
            sig = CFUNCTYPE(first[1].restype, *first[1].argtypes)
    if isinstance(offset, dict):
        # Handle overloads
        if (_offset := offset.get(overload)) is not None:  # type: ignore
            offset = _offset
        else:
            _offset = list(offset.items())[0]
            calling_logger.warning(
                f"No function arguments overload was provided for {name}. "
            )
            calling_logger.warning(
                f"Falling back to the first overload ({_offset[0]})")
            offset = _offset[1]

    cfunc = sig(_internal.BASE_ADDRESS + offset)
    return cfunc(*args)
