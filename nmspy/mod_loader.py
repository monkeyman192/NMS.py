# Main functionality for loading mods.

# Mods will consist of a single file which will generally contain a number of
# hooks.

import inspect
import importlib.util
import logging
import os.path as op
import os
from types import ModuleType
from typing import Any
import string
import sys
from functools import partial

from nmspy._types import NMSHook
from nmspy._internal import CWD
from nmspy.hooking import HookManager, _NMSHook


mod_logger = logging.getLogger("ModManager")


VALID_CHARS = string.ascii_letters + string.digits + "_"

# This will fail when not injected. Just have some dummy fallback for now.
try:
    fpath = op.join(CWD, "mods")
except TypeError:
    fpath = "mods"


def _clean_name(name: str) -> str:
    """ Remove any disallowed characters from the filename so that we get a
    valid module name."""
    out = ''
    for char in name:
        if char not in VALID_CHARS:
            out += "_"
        else:
            out += char
    return out


def _is_mod_predicate(obj, ref_module) -> bool:
    if inspect.getmodule(obj) == ref_module and inspect.isclass(obj):
        return issubclass(obj, NMSMod)
    return False


def _partial_predicate(value: Any) -> bool:
    try:
        return isinstance(value, partial) and isinstance(value.func.__self__, _NMSHook)
    except TypeError:
        return False


def _main_loop_predicate(value: Any) -> bool:
    """ Determine if the objecy has the _is_main_loop_func property.
    This will only be methods on NMSMod classes which are decorated with either
    @main_loop.before or @main_loop.after
    """
    return getattr(value, "_is_main_loop_func", False)


def _import_file(fpath: str) -> ModuleType:
    module_name = _clean_name(op.splitext(op.basename(fpath))[0])
    spec = importlib.util.spec_from_file_location(module_name, fpath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class NMSMod():
    def __init__(self):
        # Find all the hooks defined for the mod.
        self.hooks: list[NMSHook] = [
            x[1].func.__self__ for x in inspect.getmembers(self, _partial_predicate)
        ]

        self._main_funcs = [
            x[1] for x in inspect.getmembers(self, _main_loop_predicate)
        ]


class ModManager():
    def __init__(self, hook_manager: HookManager):
        # Internal mapping of mods.
        self._mods: dict[str, type[NMSMod]] = {}
        # Actual mapping of mods.
        self.mods: dict[str, NMSMod] = {}
        self.hook_manager = hook_manager

    def load_mod(self, fpath) -> bool:
        mod = _import_file(fpath)
        d: dict[str, type[NMSMod]] = dict(
            inspect.getmembers(
                mod,
                partial(_is_mod_predicate, ref_module=mod)
            )
        )
        self._mods.update(d)
        return True

    def load_mod_folder(self, folder: str):
        for file in os.listdir(folder):
            if file.endswith(".py"):
                self.load_mod(op.join(folder, file))

    def enable_all(self):
        """ Enable all mods loaded by the manager. """
        for name, _mod in self._mods.items():
            mod_logger.info(f"Loading hooks for {name}")
            # Instantiate the mod, and then overwrite the object in the mods
            # attribute with the instance.
            mod = _mod()
            self.mods[name] = mod
            if not hasattr(mod, "hooks"):
                mod_logger.error(f"The mod {mod.__class__.__name__} is not initialised properly. Please ensure that `super().__init__()` is included in the `__init__` method of this mod!")
                mod_logger.warning(f"Could not enable {mod.__class__.__name__}")
                continue
            for hook in mod.hooks:
                self.hook_manager.register_function(hook, True, mod)
            for main_loop_func in mod._main_funcs:
                self.hook_manager.add_main_loop_func(main_loop_func)

    def reload(self):
        # TODO
        pass
