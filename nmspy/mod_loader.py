# Main functionality for loading mods.

# Mods will consist of a single file which will generally contain a number of
# hooks.

from functools import partial
import inspect
import importlib.util
import logging
import os.path as op
import os
from types import ModuleType
from typing import Any, Optional
import string
import sys

from nmspy import __version__ as _nmspy_version
from nmspy._types import NMSHook
from nmspy._internal import CWD
from nmspy.hooking import HookManager, _NMSHook

import semver


mod_logger = logging.getLogger("ModManager")


VALID_CHARS = string.ascii_letters + string.digits + "_"

# This will fail when not injected. Just have some dummy fallback for now.
try:
    fpath = op.join(CWD, "mods")
except TypeError:
    fpath = "mods"


nmspy_version = semver.Version.parse(_nmspy_version)


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


def _fully_booted_ready_predicate(value: Any) -> bool:
    """ Determine if the objecy has the _run_on_fully_booted property.
    This will only be methods on NMSMod classes which are decorated with
    @on_fully_booted
    """
    return getattr(value, "_run_on_fully_booted", False)


def _import_file(fpath: str) -> ModuleType:
    module_name = _clean_name(op.splitext(op.basename(fpath))[0])
    spec = importlib.util.spec_from_file_location(module_name, fpath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class NMSMod():
    __author__: str = "Name(s) of the mod author(s)"
    __description__: str = "Short description of the mod"
    __version__: str = "Mod version"
    # Minimum required NMS.py version for this mod.
    __NMSPY_required_version__: Optional[str] = None

    def __init__(self):
        # Find all the hooks defined for the mod.
        self.hooks: list[NMSHook] = [
            x[1].func.__self__ for x in inspect.getmembers(self, _partial_predicate)
        ]

        self._main_funcs = [
            x[1] for x in inspect.getmembers(self, _main_loop_predicate)
        ]

        # TODO: Add an inspect to make sure the method has no arguments other
        # than `self`.
        self._on_fully_booted_funcs = [
            x[1] for x in inspect.getmembers(self, _fully_booted_ready_predicate)
        ]


class ModManager():
    def __init__(self, hook_manager: HookManager):
        # Internal mapping of mods.
        self._preloaded_mods: dict[str, type[NMSMod]] = {}
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
        for mod_name, mod in d.items():
            if mod.__NMSPY_required_version__ is not None:
                try:
                    mod_version = semver.Version.parse(mod.__NMSPY_required_version__)
                except ValueError:
                    mod_logger.warning(
                        "__NMSPY_required_version__ defined on mod "
                        f"{mod.__name__} is not a valid version string"
                    )
                    mod_version = None
                if mod_version is None or mod_version <= nmspy_version:
                    self._preloaded_mods[mod_name] = mod
                else:
                    mod_logger.error(
                        f"Mod {mod.__name__} requires a newer verison of "
                        f"NMS.py ({mod_version} ≥ {nmspy_version})! "
                        "Please update"
                    )
            else:
                self._preloaded_mods[mod_name] = mod
            
        return True

    def load_mod_folder(self, folder: str):
        for file in os.listdir(folder):
            if file.endswith(".py"):
                self.load_mod(op.join(folder, file))

    def enable_all(self, quiet: bool = False) -> int:
        """ Enable all mods loaded by the manager that haven't been enabled yet.
        Returns the number of mods enabled. """
        _loaded_mod_names = set()
        for name, _mod in self._preloaded_mods.items():
            if not quiet:
                mod_logger.info(f"- Loading hooks for {name}")
            # Instantiate the mod, and then overwrite the object in the mods
            # attribute with the instance.
            mod = _mod()
            self.mods[name] = mod
            if not hasattr(mod, "hooks"):
                mod_logger.error(
                    f"The mod {mod.__class__.__name__} is not initialised "
                    "properly. Please ensure that `super().__init__()` is "
                    "included in the `__init__` method of this mod!"
                )
                mod_logger.warning(f"Could not enable {mod.__class__.__name__}")
                continue
            for hook in mod.hooks:
                self.hook_manager.register_function(hook, True, mod, quiet)
            for main_loop_func in mod._main_funcs:
                self.hook_manager.add_main_loop_func(main_loop_func)
            for on_ready_func in mod._on_fully_booted_funcs:
                self.hook_manager.add_on_fully_booted_func(on_ready_func)
            # If we get here, then the mod has been loaded successfully.
            # Add the name to the loaded mod names set so we can then remove the
            # mod from the preloaded mods dict.
            _loaded_mod_names.add(name)
        for name in _loaded_mod_names:
            self._preloaded_mods.pop(name)
        return len(_loaded_mod_names)

    def reload(self):
        # TODO
        pass
