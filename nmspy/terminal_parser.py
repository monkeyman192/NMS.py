from typing import NamedTuple, Optional


def generate_full_description(command: str, description: Optional[str] = None):
    """Generate a full description based on the function."""
    if description is not None:
        return f"<TITLE>'{command}': {description}<>"
    else:
        return f"<TITLE>'{command}'<>"


def split_key(key: str) -> tuple[str, str]:
    _split = key.split("::")
    if len(_split) != 3:
        raise ValueError(f"key {key} is invalid")
    _, mod, command = _split
    return mod, command


class TerminalCommand(NamedTuple):
    mod_name: str
    command_name: str
    args: list[str]

    @staticmethod
    def generate_key(mod_name: str, command: str):
        return f"tc::{mod_name}::{command}"

    @property
    def callback_key(self) -> str:
        return TerminalCommand.generate_key(self.mod_name, self.command_name)
