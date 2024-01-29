# A collection of functions to allow directly calling NMS engine functions since
# these are all static methods.
# Note: The arguments may not always be the same as the vanilla functions. This
# is to make them easier to call.
import ctypes
from typing import Optional

from nmspy.calling import call_function as _call_function
from nmspy.data.common import TkHandle, Vector3f, cTkMatrix34


def GetNodeAbsoluteTransMatrix(
    node: TkHandle,
    mat: Optional[cTkMatrix34] = None,
) -> cTkMatrix34:
    if mat is None:
        mat = cTkMatrix34()
    _call_function(
        "Engine::GetNodeAbsoluteTransMatrix",
        node.lookupInt,
        ctypes.addressof(mat)
    )
    return mat


def GetNodeTransMats(
    node: TkHandle,
    rel_mat: Optional[cTkMatrix34] = None,
    abs_mat: Optional[cTkMatrix34] = None,
) -> tuple[cTkMatrix34, cTkMatrix34]:
    if rel_mat is None:
        rel_mat = cTkMatrix34()
    if abs_mat is None:
        abs_mat = cTkMatrix34()
    _call_function(
        "Engine::GetNodeTransMats",
        node.lookupInt,
        ctypes.addressof(rel_mat),
        ctypes.addressof(abs_mat),
        overload="TkHandle, cTkMatrix34 *, cTkMatrix34 *"
    )
    return (rel_mat, abs_mat)


def RequestRemoveNode(node: TkHandle) -> None:
    _call_function("Engine::RequestRemoveNode", node.lookupInt)


def SetNodeActivation(node: TkHandle, active: bool):
    _call_function("Engine::SetNodeActivation", node.lookupInt, active)


def SetNodeActivationRecursive(node: TkHandle, active: bool):
    _call_function("Engine::SetNodeActivationRecursive", node.lookupInt, active)


def SetNodeTransMat(node: TkHandle, mat: cTkMatrix34):
    _call_function(
        "Engine::SetNodeTransMat",
        node.lookupInt,
        ctypes.addressof(mat),
    )


def ShiftAllTransformsForNode(node: TkHandle, shift: Vector3f) -> None:
    return _call_function(
        "Engine::ShiftAllTransformsForNode",
        node.lookupInt,
        ctypes.addressof(shift)
    )
