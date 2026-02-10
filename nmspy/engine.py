# This contains a collection of in-game engine related functions, modified to be easier to call directly.

import ctypes

import nmspy.data.basic_types as basic
from nmspy.data.types import Engine


def GetNodeAbsoluteTransMatrix(node: basic.TkHandle) -> basic.cTkMatrix34:
    """Get the aboslute transform matrix of a node."""
    matrix = basic.cTkMatrix34(
        basic.Vector3f(0, 0, 0),
        basic.Vector3f(0, 0, 0),
        basic.Vector3f(0, 0, 0),
        basic.Vector3f(0, 0, 0),
    )
    Engine.GetNodeAbsoluteTransMatrix(node, ctypes.byref(matrix))
    return matrix


def ShiftAllTransformsForNode(node: basic.TkHandle, shift: basic.Vector3f):
    """Shift all transforms for the provided node handle."""
    Engine.ShiftAllTransformsForNode(node, ctypes.byref(shift))
