from typing import Any

from pymhf import Mod


def _state_change_hook_predicate(value: Any) -> bool:
    """ Determine if the object has the _trigger_on_state property.
    This will only be methods on NMSMod classes which are decorated with
    @on_state_change or on_fully_booted.
    """
    return hasattr(value, "_trigger_on_state")


def _main_loop_predicate(value: Any) -> bool:
    """ Determine if the objecy has the _is_main_loop_func property.
    This will only be methods on Mod classes which are decorated with either
    @main_loop.before or @main_loop.after
    """
    return getattr(value, "_is_main_loop_func", False)


def _state_change_hook_predicate(value: Any) -> bool:
    """ Determine if the object has the _trigger_on_state property.
    This will only be methods on Mod classes which are decorated with
    @on_state_change or on_fully_booted.
    """
    return hasattr(value, "_trigger_on_state")


class NMSMod(Mod):
    def __init__(self):
        super().__init__()
