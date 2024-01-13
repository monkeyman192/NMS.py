# A collection of functions to allow directly calling NMS engine functions since
# these are all static methods.
from nmspy.calling import call_function as _call_function


def ShiftAllTransformsForNode(node: int, shift: int) -> None:
    return _call_function("Engine::ShiftAllTransformsForNode", node, shift)
