from collections.abc import Callable
from ctypes import CFUNCTYPE
from functools import wraps
import inspect
import logging
from typing import Any, Optional, Type
import traceback

import cyminhook

import nmspy.common as nms
from nmspy.data.func_offsets import FUNC_OFFSETS
from nmspy.data.func_call_sigs import FUNC_CALL_SIGS
from nmspy.errors import UnknownFunctionError

hook_logger = logging.getLogger("HookManager")


def before(func):
    func._before = True
    return func


def after(func):
    """ Mark the decorated function as one which will only be run after the
    original function has been run.
    This function may have the keyword argument `__result`. If it does, then
    this value will be the result of the call of the original function
    """
    func._after = True
    func_sig = inspect.signature(func)
    if "result" in func_sig.parameters.keys():
        func._has_return_arg = True
    else:
        func._has_return_arg = False
    return func


def hook_function(
    function_name: Optional[str] = None,
    *,
    offset: Optional[int] = None,
    pattern: Optional[str] = None
):
    """ Specify parameters for the function to hook.

    Parameters
    ----------
    function_name:
        The name of the function to hook. This will be looked up against the
        known functions for the game and hooked if found.
    offset:
        The offset relative to the base address of the exe where the function
        starts.
    pattern:
        A byte pattern in the form `"AB CD ?? EF ..."`
        This will be the same pattern as used by IDA and cheat engine.
    """
    def _hook_function(klass):
        if function_name in FUNC_OFFSETS:
            target = nms.BASE_ADDRESS + FUNC_OFFSETS[function_name]
        else:
            raise UnknownFunctionError(f"{function_name} has no known address")
        if function_name in FUNC_CALL_SIGS:
            signature = FUNC_CALL_SIGS[function_name]
        else:
            raise UnknownFunctionError(f"{function_name} has no known call signature")
        klass.target = target
        klass.signature = signature
        klass._name = function_name
        return klass
    return _hook_function


def conditionally_enabled_hook(conditional: bool):
    """ Conditionally enable a hook.
    This conditional is check at function definition time and will determine if
    the hook should actually be enabled when told to enable.

    Parameters
    ----------
    conditional:
        A statement which must resolve to True or False
        Eg. `some_variable == 42`
    """
    def _conditional_hook(klass):
        klass._should_enable = conditional
        return klass
    return _conditional_hook


def conditional_hook(conditional: str):
    """ Conditionally call the detour function when the provided conditional
    evaluates to true.
    This can be used to conditionally turn on or off the detouring automatically
    based on some condition.

    Parameters
    ----------
    conditional:
        String containing a statement which, when evaluated to be True, will
        cause the detour to be run.
    """
    def _conditional_hook(klass):
        orig_detour = klass.detour
        @wraps(klass.detour)
        def conditional_detour(self: NMSHook, *args, **kwargs):
            # Run the original function if the conditional evaluates to True.
            if eval(conditional) is True:
                ret = orig_detour(self, *args, **kwargs)
            else:
                ret = self.original(*args, **kwargs)
            return ret
        # Assign the decorated method to the `detour` attribute.
        klass.detour = conditional_detour
        return klass
    return _conditional_hook


def one_shot(klass):
    """ A decorator to make a hook a one-shot hook. """
    orig_detour = klass.detour
    @wraps(klass.detour)
    def oneshot_detour(self: NMSHook, *args, **kwargs):
        # Run the original function
        ret = orig_detour(self, *args, **kwargs)
        # Then disable the hook.
        self.disable()
        return ret
    # Assign the decorated method to the `detour` attribute.
    klass.detour = oneshot_detour
    return klass


class NMSHook(cyminhook.MinHook):
    original: Callable[..., Any]

    def __init__(self,
        *,
        signature: Optional[CFUNCTYPE] = None,
        target: Optional[int] = None
    ):
        # Normally defined classes will not be "compound compatible".
        # This means that they will be the only function to hook a given game
        # function.
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
        super().enable()
        self.state = "enabled"

    def disable(self):
        super().disable()
        self.state = "disabled"


class CompoundHook(NMSHook):
    def __init__(
        self,
        *,
        signature: Optional[CFUNCTYPE] = None,
        target: Optional[int] = None
    ):
        super().__init__(target=target, signature=signature)
        self.before_funcs = []
        self.after_funcs = []
        self.after_funcs_with_result = []

    def add_before(self, func):
        self.before_funcs.append(func)

    def add_after(self, func):
        if func._has_return_arg:
            self.after_funcs_with_result.append(func)
        else:
            self.after_funcs.append(func)

    def detour(self, *args, **kwargs):
        for func in self.before_funcs:
            func(*args, **kwargs)
        return_value = self.original(*args, **kwargs)
        for func in self.after_funcs:
            return_value = func(*args, **kwargs) or return_value
        for func in self.after_funcs_with_result:
            return_value = func(*args, result=return_value, **kwargs) or return_value
        return return_value


class HookManager():
    def __init__(self):
        self.hooks: dict[str, NMSHook] = {}
        self.compound_hooks: dict[str, CompoundHook] = {}
        # Keep a mapping of any hooks that try to be registered but fail.
        # These hooks will not be instances of classes, but the class type.
        self.failed_hooks: dict[str, Type[NMSHook]] = {}

    def add_hook(self, detour: Callable[..., Any], *, function_name: str, one_shot: bool):
        # In-line creation of hooks.
        if function_name in FUNC_OFFSETS:
            target = nms.BASE_ADDRESS + FUNC_OFFSETS[function_name]
        else:
            raise UnknownFunctionError(f"{function_name} has no known address")
        if function_name in FUNC_CALL_SIGS:
            signature = FUNC_CALL_SIGS[function_name]
        else:
            raise UnknownFunctionError(f"{function_name} has no known call signature")
        # TODO: sort out adding `self` to the func so it's bound to the class instance.
        hook = NMSHook(signature=signature, target=target, detour=detour)
        hook._name = function_name

    def _add_cls_to_compound_hook(self, cls, compound_cls):
        if before_hook := getattr(cls, "_before_hook", None):
            compound_cls.add_before(before_hook)
        if after_hook := getattr(cls, "_after_hook", None):
            compound_cls.add_after(after_hook)

    def register(
        self,
        hook: Type[NMSHook],
        func_name: Optional[str] = None,
        enable: bool = True
    ):
        # Try and instance the hook object. This may fail so we want to raise
        # a more helpful message than cyminhook raises if this happens.
        func_name = getattr(hook, "_name", func_name)
        try:
            _hook: NMSHook = hook()
        except cyminhook._cyminhook.Error as e:
            hook_logger.error(e)
            hook_logger.error(e.status.name[3:].replace("_", " "))
            # Log some info about the target region.
            hook_logger.error(f"The target function was expected at 0x{hook.target}")
            self.failed_hooks[func_name] = hook
            return
        # Check to see if the provided class implement the compound hook
        # functionality. If so, handle it.
        if _hook._is_compound_compatible:
            if func_name not in self.compound_hooks:
                compound_class = CompoundHook(
                    target=_hook.target,
                    signature=_hook.signature
                )
                self._add_cls_to_compound_hook(_hook, compound_class)
                self.compound_hooks[func_name] = compound_class
                hook_logger.info(f"Added hook {hook.__name__} as a compound hook")
                _hook = compound_class
            else:
                self._add_cls_to_compound_hook(_hook, self.compound_hooks[func_name])
                hook_logger.info(f"Added hook {hook.__name__} to an existing compound hook")
                _hook = self.compound_hooks[func_name]
        else:
            hook_logger.info(f"Registered hook {hook.__name__} for function {func_name}")
            self.hooks[func_name] = _hook
        if enable:
            try:
                _hook.enable()
            except:
                hook_logger.info(traceback.format_exc())

    def enable(self, func_name: str):
        if hook := self.hooks.get(func_name):
            hook.enable()
        elif hook := self.compound_hooks.get(func_name):
            hook.enable()
        hook_logger.info(f"Enabled hook for function {func_name}")

    def disable(self, func_name: str):
        if hook := self.hooks.get(func_name):
            hook.disable()
        elif hook := self.compound_hooks.get(func_name):
            hook.disable()
        hook_logger.info(f"Disabled hook for function {func_name}")

    @property
    def states(self):
        # Return the states of all the registered hooks
        for func_name, hook in self.hooks.items():
            yield f"{func_name}: {hook.state}"
