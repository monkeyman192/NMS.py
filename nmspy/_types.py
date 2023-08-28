# Have the NMS* class definitions here since there is a circular dependency
# otherwise.

from ctypes import CFUNCTYPE
from typing import Callable, Any, Optional
import inspect
from types import MethodType

import cyminhook


def _hook_predicate(value: Any) -> bool:
    """ Filter function to only return classes which subclass NMSHook"""
    try:
        return issubclass(value, NMSHook)
    except TypeError:
        return False


class NMSMod():
    def __init__(self):
        # Find all the hooks defined for the mod.
        self.hooks: list[NMSHook] = [
            x[1] for x in inspect.getmembers(self, _hook_predicate)
        ]
        # For each hook, associate the mod with it so that it can reference it.
        for hook in self.hooks:
            hook.mod = self


class NMSHook(cyminhook.MinHook):
    original: Callable[..., Any]
    target: int
    detour: Callable[..., Any]
    signature: CFUNCTYPE
    _name: str
    _should_enable: bool
    mod: NMSMod

    def __init__(self,
        *,
        detour: Optional[Callable[..., Any]] = None,
        signature: Optional[CFUNCTYPE] = None,
        target: Optional[int] = None
    ):
        # Normally defined classes will not be "compound compatible".
        # This means that they will be the only function to hook a given game
        # function.
        if detour is not None:
            # If detour is provided, then bind it to the detour method of
            # ourself.
            setattr(self, "detour", MethodType(detour, self))
        self._is_compound_compatible = False
        for _, obj in inspect.getmembers(self):
            if hasattr(obj, "_before"):
                self._before_hook = obj
                self._is_compound_compatible = True
            elif hasattr(obj, "_after"):
                self._after_hook = obj
                self._is_compound_compatible = True
        # Only initialize the cyminhook subclass if we are not a compound-compatible hook.
        # If it's a compound hook then initializing it will cause and error to
        # occur. We will initialize the hook properly when we create the actual
        # compound hook.
        if not self._is_compound_compatible:
            super().__init__(signature=signature, target=target)
        self.state = "initialized"

    def close(self):
        super().close()
        self.state = "closed"

    def enable(self):
        if getattr(self, "_should_enable", True):
            super().enable()
            self.state = "enabled"

    def disable(self):
        super().disable()
        self.state = "disabled"