# Have the NMS* class definitions here since there is a circular dependency
# otherwise.

from collections import namedtuple
from ctypes import CFUNCTYPE
from _ctypes import CFuncPtr
from typing import Callable, Any, Optional
import inspect
from types import MethodType

import cyminhook


FUNCDEF = namedtuple("FUNCDEF", ["restype", "argtypes"])


class NMSHook(cyminhook.MinHook):
    original: Callable[..., Any]
    target: int
    detour: Callable[..., Any]
    signature: CFuncPtr
    _name: str
    _should_enable: bool
    _invalid: bool
    _pattern: Optional[str]
    mod: Any

    def __init__(self,
        *,
        detour: Optional[Callable[..., Any]] = None,
        signature: Optional[CFuncPtr] = None,
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
        if not hasattr(self, "_should_enable"):
            self._should_enable = True
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
        if self._should_enable:
            super().enable()
            self.state = "enabled"

    def disable(self):
        super().disable()
        self.state = "disabled"