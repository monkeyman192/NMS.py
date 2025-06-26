from pymhf.core._types import DetourTime
from pymhf.core._types import HookProtocol


class main_loop:
    @staticmethod
    def before(func: HookProtocol):
        func._custom_trigger = "MAIN_LOOP"
        func._hook_time = DetourTime.BEFORE
        return func

    @staticmethod
    def after(func: HookProtocol):
        func._custom_trigger = "MAIN_LOOP"
        func._hook_time = DetourTime.AFTER
        return func


def on_fully_booted(func: HookProtocol):
    """
    Configure the decorated function to be run once the game is considered
    "fully booted".
    This occurs when the games' internal state first changes to "mode selector"
    (ie. just before the game mode selection screen appears).
    """
    func._custom_trigger = "MODESELECTOR"
    return func


def on_state_change(state: str):
    def _inner(func: HookProtocol):
        func._custom_trigger = state
        return func

    return _inner
