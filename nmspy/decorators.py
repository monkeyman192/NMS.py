from typing import Optional, Callable

from pymhf.core._types import CustomTriggerProtocol, DetourTime


class main_loop:
    @staticmethod
    def before(func: Callable) -> CustomTriggerProtocol:
        func._custom_trigger = "MAIN_LOOP"
        func._hook_time = DetourTime.BEFORE
        return func  # type: ignore

    @staticmethod
    def after(func: Callable) -> CustomTriggerProtocol:
        func._custom_trigger = "MAIN_LOOP"
        func._hook_time = DetourTime.AFTER
        return func  # type: ignore


def on_fully_booted(func: Callable) -> CustomTriggerProtocol:
    """
    Configure the decorated function to be run once the game is considered
    "fully booted".
    This occurs when the games' internal state first changes to "mode selector"
    (ie. just before the game mode selection screen appears).
    """
    func._custom_trigger = "MODESELECTOR"
    return func  # type: ignore


def on_state_change(state: str):
    def _inner(func: CustomTriggerProtocol):
        func._custom_trigger = state
        return func

    return _inner


def terminal_command(
    description: Optional[str] = None,
    mod_override: Optional[str] = None,
    command_override: Optional[str] = None,
):
    """Mark the function as a terminal command.
    The mod name and terminal command will automatically be determined from the name of this function and the
    name of the mod it belongs to.
    To override the name of the command specify the ``command_override`` argument.
    The optional ``description`` argument will be added to the help menu to aid users."""

    # TODO: Use inspect to automatically get arguments and types if they have any to show in the description.
    def _inner(func: Callable) -> CustomTriggerProtocol:
        func_name = func.__qualname__
        split_name = func_name.split(".")
        if len(split_name) != 2:
            raise ValueError(
                "@terminal_command can only be used as a decorator for bound methods."
            )
        mod_name, command = split_name
        if mod_override is not None:
            mod_name = mod_override
        if command_override is not None:
            command = command_override
        func._custom_trigger = f"tc::{mod_name.lower()}::{command.lower()}"
        func._description = description
        return func  # type: ignore

    return _inner
