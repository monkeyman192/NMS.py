import ast
from collections.abc import Callable
from ctypes import CFUNCTYPE
from enum import Enum
from functools import wraps, update_wrapper, partial
import inspect
import logging
from typing import Any, Optional, Type, Union, Generic
import traceback

import cyminhook

import nmspy.common as nms
from nmspy.data import FUNC_OFFSETS
from nmspy.data.func_call_sigs import FUNC_CALL_SIGS
from nmspy.errors import UnknownFunctionError
from nmspy.memutils import find_bytes
from nmspy._types import NMSHook
from nmspy.caching import function_cache, pattern_cache

hook_logger = logging.getLogger("HookManager")


# Currently unused, but can maybe figure out how to utilise it.
# It currently doesn't work I think because we subclass from the cyminhook class
# which is cdef'd, and I guess ast falls over trying to get the actual source...
# Can possible use annotations and inspect the return type (return `None`
# explictly eg.) to give some hints. Maybe just raise warnings etc.
def _detour_is_valid(f):
    for node in ast.walk(ast.parse(inspect.getsource(f))):
        if isinstance(node, ast.Return):
            return True
    return False


class DetourTime(Enum):
    NONE = 0
    BEFORE = 1
    AFTER = 2


ORIGINAL_MAPPING = dict()


class _NMSHook(cyminhook.MinHook):
    original: Callable[..., Any]
    target: int
    detour: Callable[..., Any]
    signature: CFUNCTYPE
    _name: str
    _should_enable: bool
    _invalid: bool = False
    _pattern: Optional[str]
    _is_one_shot: bool = False

    def __init__(
        self,
        detour: Callable[..., Any],
        *,
        name: Optional[str] = None,
        offset: Optional[int] = None,
        pattern: Optional[str] = None,
        detour_time: DetourTime = DetourTime.NONE,
    ):
        self._mod = None
        self._should_enable = True
        self._original_detour = detour
        self.detour_time = detour_time
        if not offset and not pattern:
            if name in FUNC_OFFSETS:
                self.target = nms.BASE_ADDRESS + FUNC_OFFSETS[name]
            else:
                hook_logger.error(f"{name} has no known address")
                self._invalid = True
        else:
            if pattern:
                self._pattern = pattern
        if name in FUNC_CALL_SIGS:
            self.signature = FUNC_CALL_SIGS[name]
        else:
            hook_logger.error(f"{name} has no known call signature")
            self._invalid = True
        self._name = name

    def bind(self, cls = None) -> bool:
        """ Actually initialise the base class. Returns whether the hook is bound. """
        # Associate the mod now whether or not we get one. This way if the
        # function is actually disabled, we may enable it later with no issues.
        self._mod = cls
        if not self._should_enable:
            return False

        if cls is not None:
            self._detour_func = partial(self._original_detour, cls)
        else:
            self._detour_func = self._original_detour

        # Check the detour time and create an approriately "wrapped" function
        # which will run instead of the original function.
        if self.detour_time == DetourTime.BEFORE:
            self.detour = self._before_detour
        elif self.detour_time == DetourTime.AFTER:
            # For an "after" hook, we need to determine if "__result" is in the
            # function arguments.
            func_sig = inspect.signature(self._original_detour)
            if "__result" in func_sig.parameters.keys():
                self.detour = self._after_detour_with_return
            else:
                self.detour = self._after_detour
        else:
            self.detour = self._normal_detour

        # Check to see if it's a one shot and wrap this detour one more to be
        # one-shot.
        if self._is_one_shot:
            self._non_oneshot_detour = self.detour
            self.detour = self._oneshot_detour

        super().__init__(signature=self.signature, target=self.target)
        ORIGINAL_MAPPING[self._name] = self.original
        self.state = "initialized"
        if not hasattr(self, "_should_enable"):
            self._should_enable = True
        return True

    def __call__(self, *args, **kwargs):
        return self.detour(*args, **kwargs)

    def __get__(self, instance, owner=None):
        # Pass the instance through to the __call__ function so that we can use
        # this decorator on a method of a class.
        return partial(self.__call__, instance)

    def _oneshot_detour(self, *args):
        ret = self._non_oneshot_detour(*args)
        self.disable()
        hook_logger.info(f"Disabling a one-shot hook ({self._name})")
        return ret

    def _normal_detour(self, *args):
        # Run a detour as provided by the user.
        return self._detour_func(*args)

    def _before_detour(self, *args):
        # A detour to be run instead of the normal one when we are registered as
        # a "before" hook.
        ret = self._detour_func(*args)
        # If we get a return value that is not None, then pass it through.
        if ret is not None:
            return self.original(*ret)
        else:
            return self.original(*args)

    def _after_detour(self, *args):
        # Detour which will be run instead of the normal one.
        # The original function will be run before.
        ret = self.original(*args)
        self._detour_func(*args)
        return ret

    def _after_detour_with_return(self, *args):
        # Detour which will be run instead of the normal one.
        # The original function will be run before.
        # The return value of the original function will be passed in.
        ret = self.original(*args)
        new_ret = self._detour_func(*args, __result=ret)
        if new_ret is not None:
            return new_ret
        return ret

    def close(self):
        super().close()
        self.state = "closed"

    def enable(self):
        super().enable()
        self.state = "enabled"
        self._should_enable = True

    def disable(self):
        super().disable()
        self.state = "disabled"


class HookFactory:
    _name: Optional[str] = None
    _templates: Optional[tuple[str]] = None
    def __init__(self, func):
        self.func = func
        self._after = False
        self._before = False
        update_wrapper(self, func)

    def __new__(cls, detour, detour_time: DetourTime = DetourTime.NONE) -> _NMSHook:
        return _NMSHook(detour, name=cls._name, detour_time=detour_time)

    def __class_getitem__(cls: type["HookFactory"], key: Union[tuple[Any], Any]):
        if cls._templates is not None and cls._name is not None:
            if isinstance(key, tuple):
                fmt_key = dict(zip(cls._templates, [x.__name__ for x in key]))
            else:
                fmt_key = {cls._templates[0]: key.__name__}
            hook_logger.info(cls._name.format(**fmt_key))
            cls._name = cls._name.format(**fmt_key)
        return cls

    @classmethod
    def original(cls, *args):
        """ Call the orgiginal function with the given arguments. """
        return ORIGINAL_MAPPING[cls._name](*args)

    @classmethod
    def before(cls, func: Callable[..., Any]) -> _NMSHook:
        """
        Run the decorated function before the original function is run.
        This function in general should not call the original function, and does
        not need to return anything.
        If you wish to modify the values being passed into the original
        function, return a tuple which has values in the same order as the
        original function.
        """
        return _NMSHook(func, name=cls._name, detour_time=DetourTime.BEFORE)

    @classmethod
    def after(cls, func: Callable[..., Any]) -> _NMSHook:
        """ Run the decorated function after the original function is run. """
        return _NMSHook(func, name=cls._name, detour_time=DetourTime.AFTER)


def disable(klass: _NMSHook):
    """ Disable the current hook. This must be the outermost decorator is applied. """
    klass._should_enable = False
    return klass


def before(func):
    """ Mark the hook to be only run before the original function.
    Currently these cannot mutate the arguments passed into the original
    function, but this will likely change in the future.
    """
    func._before = True
    return func


def after(func):
    """ Mark the hook to be only run after the original function.
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


def main_loop(func):
    # TODO: Make work...
    func._update_loop = True
    return func


def hook_function(
    function_name: str,
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
        NOTE: Currently doesn't work.
    pattern:
        A byte pattern in the form `"AB CD ?? EF ..."`
        This will be the same pattern as used by IDA and cheat engine.
        NOTE: Currently doesn't work.
    """
    def _hook_function(klass: NMSHook):
        klass._pattern = None
        klass.target = 0
        if not offset and not pattern:
            if function_name in FUNC_OFFSETS:
                klass.target = nms.BASE_ADDRESS + FUNC_OFFSETS[function_name]
            else:
                raise UnknownFunctionError(f"{function_name} has no known address")
        else:
            if pattern:
                klass._pattern = pattern
        if function_name in FUNC_CALL_SIGS:
            signature = FUNC_CALL_SIGS[function_name]
        else:
            raise UnknownFunctionError(f"{function_name} has no known call signature")
        klass.signature = signature
        klass._name = function_name
        return klass
    return _hook_function


def conditionally_enabled_hook(conditional: bool):
    """ Conditionally enable a hook.
    This conditional is checked at function definition time and will determine
    if the hook should actually be enabled when told to enable.

    Parameters
    ----------
    conditional:
        A statement which must resolve to True or False
        Eg. `some_variable == 42`
    """
    def _conditional_hook(klass: NMSHook):
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
    def _conditional_hook(klass: NMSHook):
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


def one_shot(klass: _NMSHook):
    klass._is_one_shot = True
    return klass


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
        """ Detour function consisting of multiple sub-functions. """
        # First, run each of the 'before' detours.
        for func in self.before_funcs:
            func(*args, **kwargs)
        # Then, run the original function.
        return_value = self.original(*args, **kwargs)
        # Then run each of the 'after' detours.
        for func in self.after_funcs:
            return_value = func(*args, **kwargs) or return_value
        # Finally, run reach of the 'after' functions which takes the return
        # value.
        # We run these last so that they may have the most recent return value
        # possible.
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

    def add_hook(
        self,
        detour: Callable[..., Any],
        signature: CFUNCTYPE,
        target: int,
        func_name: str,
        enable: bool = True
    ):
        # In-line creation of hooks.
        hook = NMSHook(signature=signature, target=target, detour=detour)
        hook._name = func_name
        self.hooks[func_name] = hook
        if enable:
            try:
                hook.enable()
            except:
                hook_logger.info(traceback.format_exc())

    def _add_cls_to_compound_hook(
        self,
        cls: NMSHook,
        compound_cls: CompoundHook
    ):
        if before_hook := getattr(cls, "_before_hook", None):
            compound_cls.add_before(before_hook)
        if after_hook := getattr(cls, "_after_hook", None):
            compound_cls.add_after(after_hook)

    # Deprecated
    # def register(
    #     self,
    #     hook: Type[NMSHook],
    #     func_name: Optional[str] = None,
    #     enable: bool = True
    # ):
    #     # Try and instance the hook object. This may fail so we want to raise
    #     # a more helpful message than cyminhook raises if this happens.
    #     func_name = getattr(hook, "_name", func_name)
    #     hook_name = hook.__name__

    #     # Do some initial checks to see if the hook has a pattern defined for
    #     # it.
    #     # We need to do pattern scanning now since we can't do it when the
    #     # decorator runs.

    #     if hook._pattern is not None:
    #         # If we get a pattern, look up by name to see if we have already got
    #         # it cached, otherwise look it up by pattern.
    #         # If that also fails, then it means we don't have it cached and we
    #         # need to search memory for it.
    #         target = function_cache.get(hook._name)
    #         if not target:
    #             target = pattern_cache.get(hook._pattern)
    #         if target is None:
    #             hook_logger.info(f"Finding {func_name} by pattern")
    #             abs_offset = find_bytes(hook._pattern, alignment=0x10)
    #             if abs_offset:
    #                 target = abs_offset - nms.BASE_ADDRESS
    #                 hook_logger.info(f"Pattern found at +0x{target:X}. Saving to cache")
    #                 function_cache.set(func_name, target)
    #                 pattern_cache.set(hook._pattern, target)
    #                 hook.target = nms.BASE_ADDRESS + target
    #             else:
    #                 # Signature not found. We can't register this hook.
    #                 self.failed_hooks[func_name] = hook
    #                 hook_logger.info(f"Unable to register {func_name}. "
    #                                  f"Cannot find pattern: {hook._pattern}")
    #                 return
    #         else:
    #             hook_logger.info(f"Found {func_name} in offset cache")
    #             hook.target = nms.BASE_ADDRESS + target

    #     try:
    #         _hook: NMSHook = hook()
    #     except cyminhook._cyminhook.Error as e:
    #         hook_logger.error(e)
    #         hook_logger.error(e.status.name[3:].replace("_", " "))
    #         # Log some info about the target region.
    #         hook_logger.error(f"The target function was expected at 0x{hook.target}")
    #         self.failed_hooks[func_name] = hook
    #         return
    #     # Check to see if the provided class implement the compound hook
    #     # functionality. If so, handle it.
    #     if _hook._is_compound_compatible:
    #         if func_name not in self.compound_hooks:
    #             compound_class = CompoundHook(
    #                 target=_hook.target,
    #                 signature=_hook.signature
    #             )
    #             self._add_cls_to_compound_hook(_hook, compound_class)
    #             self.compound_hooks[func_name] = compound_class
    #             hook_logger.info(f"Added hook '{hook_name}' as a compound hook")
    #             _hook = compound_class
    #         else:
    #             self._add_cls_to_compound_hook(_hook, self.compound_hooks[func_name])
    #             hook_logger.info(f"Added hook '{hook_name}' to an existing compound hook")
    #             _hook = self.compound_hooks[func_name]
    #     else:
    #         hook_logger.info(f"Registered hook '{hook_name}' for function '{func_name}'")
    #         self.hooks[func_name] = _hook
    #     if enable:
    #         try:
    #             _hook.enable()
    #         except:
    #             hook_logger.info(traceback.format_exc())

    def resolve_dependencies(self):
        """ Resolve dependencies of hooks.
        This will get all the functions which are to be hooked and construct
        compound hooks as required."""
        # TODO: Make work.
        pass

    def register_function(self, hook: _NMSHook, enable: bool = True, mod = None):
        """ Register the provided function as a callback. """
        if hook._invalid:
            # If the hook is invalid for any reason, then just return (for now...)
            return
        bound_ok = hook.bind(mod)
        if bound_ok:
            hook_logger.info(
                f"Registered hook '{hook._name}' for function "
                f"'{hook._original_detour.__name__}'"
            )
            self.hooks[hook._name] = hook
            if enable and hook._should_enable:
                try:
                    hook.enable()
                except:
                    hook_logger.info(traceback.format_exc())

    def enable(self, func_name: str):
        """ Enable the hook for the provided function name. """
        if hook := self.hooks.get(func_name):
            hook.enable()
        elif hook := self.compound_hooks.get(func_name):
            hook.enable()
        else:
            return
        hook_logger.info(f"Enabled hook for function '{func_name}'")

    def disable(self, func_name: str):
        """ Disable the hook for the provided function name. """
        if hook := self.hooks.get(func_name):
            hook.disable()
        elif hook := self.compound_hooks.get(func_name):
            hook.disable()
        else:
            return
        hook_logger.info(f"Disabled hook for function '{func_name}'")

    @property
    def states(self):
        # Return the states of all the registered hooks
        for func_name, hook in self.hooks.items():
            yield f"{func_name}: {hook.state}"
