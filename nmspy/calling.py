import nmspy.common as nms
from nmspy.data.func_call_sigs import FUNC_CALL_SIGS
from nmspy.data import FUNC_OFFSETS


def call_function(name: str, *args, **kwargs):
    sig = FUNC_CALL_SIGS[name]
    cfunc = sig(nms.BASE_ADDRESS + FUNC_OFFSETS[name])
    cfunc(*args, **kwargs)
