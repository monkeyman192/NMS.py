from pymhf.core._types import DetourTime


class main_loop:
    @staticmethod
    def before(func):
        func._custom_trigger = "MAIN_LOOP"
        func._hook_time = DetourTime.BEFORE
        return func

    @staticmethod
    def after(func):
        func._custom_trigger = "MAIN_LOOP"
        func._hook_time = DetourTime.AFTER
        return func


def on_fully_booted(func):
    """
    Configure the decorated function to be run once the game is considered
    "fully booted".
    This occurs when the games' internal state first changes to "mode selector"
    (ie. just before the game mode selection screen appears).
    """
    func._custom_trigger = "MODESELECTOR"
    return func


def on_state_change(state):
    def _inner(func):
        func._custom_trigger = state
        return func
    return _inner