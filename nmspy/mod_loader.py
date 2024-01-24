# Main functionality for loading mods.

# Mods will consist of a single file which will generally contain a number of
# hooks.

from abc import ABC
from dataclasses import fields
from functools import partial
import inspect
import importlib
import importlib.util
import json
import logging
import os.path as op
import os
import traceback
from types import ModuleType
from typing import Any, Optional
import string
import sys

from nmspy import __version__ as _nmspy_version
from nmspy.errors import NoSaveError
from nmspy._types import NMSHook
from nmspy._internal import CWD
from nmspy.hooking import HookManager, _NMSHook
import nmspy.common as nms

import keyboard
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
        return issubclass(obj, NMSMod) and getattr(obj, "_should_enable", True)
    return False


def _is_mod_state_predicate(obj) -> bool:
    return isinstance(obj, ModState)


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


def _state_change_hook_predicate(value: Any) -> bool:
    """ Determine if the object has the _trigger_on_state property.
    This will only be methods on NMSMod classes which are decorated with
    @on_state_change or on_fully_booted.
    """
    return hasattr(value, "_trigger_on_state")


def _has_hotkey_predicate(value: Any) -> bool:
    """ Determine if the objecy has the _is_main_loop_func property.
    This will only be methods on NMSMod classes which are decorated with either
    @main_loop.before or @main_loop.after
    """
    return getattr(value, "_hotkey", False)


def _import_file(fpath: str) -> Optional[ModuleType]:
    try:
        module_name = _clean_name(op.splitext(op.basename(fpath))[0])
        if spec := importlib.util.spec_from_file_location(module_name, fpath):
            module = importlib.util.module_from_spec(spec)
            module.__name__ = module_name
            module.__spec__ = spec
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            return module
    except Exception:
        mod_logger.error(f"Error loading {fpath}")
        mod_logger.exception(traceback.format_exc())


class StructEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__json__"):
            return {
                "struct": obj.__class__.__qualname__,
                "module": obj.__class__.__module__,
                "fields": obj.__json__()
            }
        return json.JSONEncoder.default(self, obj)


class StructDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook)

    def object_hook(seld, obj: dict):
        if (module := obj.get("module")) is not None:
            mod_logger.info(module)
            if module == "__main__":
                return globals()[obj["struct"]](**obj["fields"])
            else:
                try:
                    module_ = importlib.import_module(module)
                    return getattr(module_, obj["struct"])(**obj["fields"])
                except ImportError:
                    mod_logger.error(f"Cannot import {module}")
                    return
                except AttributeError:
                    mod_logger.error(
                        f"Cannot find {obj['struct']} in {module}"
                    )
                    return
        return obj


class ModState(ABC):
    """A class which is used as a base class to indicate that the class is to be
    used as a mod state.
    Mod State classes will persist across mod reloads so any variables set in it
    will have the same value after the mod has been reloaded.
    """
    _save_fields_: tuple[str]

    def save(self, name: str):
        _data = {}
        if hasattr(self, "_save_fields_") and self._save_fields_:
            for field in self._save_fields_:
                _data[field] = getattr(self, field)
        else:
            try:
                for f in fields(self):
                    _data[f.name] = getattr(self, f.name)
            except TypeError:
                mod_logger.error(
                    "To save a mod state it must either be a dataclass or "
                    "have the _save_fields_ attribute. State was not saved"
                )
                return
        with open(op.join(nms.mod_save_dir, name), "w") as fobj:
            json.dump(_data, fobj, cls=StructEncoder, indent=1)

    def load(self, name: str):
        try:
            with open(op.join(nms.mod_save_dir, name), "r") as f:
                data = json.load(f, cls=StructDecoder)
        except FileNotFoundError as e:
            raise NoSaveError from e
        for key, value in data.items():
            setattr(self, key, value)


class NMSMod(ABC):
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

        self._state_change_funcs = [
            x[1] for x in inspect.getmembers(self, _state_change_hook_predicate)
        ]

        self._hotkey_funcs = [
            x[1] for x in inspect.getmembers(self, _has_hotkey_predicate)
        ]


class ModManager():
    def __init__(self, hook_manager: HookManager):
        # Internal mapping of mods.
        self._preloaded_mods: dict[str, type[NMSMod]] = {}
        # Actual mapping of mods.
        self.mods: dict[str, NMSMod] = {}
        self._mod_hooks: dict[str, list] = {}
        self.mod_states: dict[str, list[tuple[str, ModState]]] = {}
        self._mod_paths: dict[str, ModuleType] = {}
        self.hook_manager = hook_manager
        # Keep a mapping of the hotkey callbacks
        self.hotkey_callbacks: dict[tuple[str, str], Any] = {}

    def _load_module(self, module: ModuleType) -> bool:
        """ Load a mod from the provided module.
        This will be called when initially loading the mods, and also when we
        wish to reload a mod.
        """
        d: dict[str, type[NMSMod]] = dict(
            inspect.getmembers(
                module,
                partial(_is_mod_predicate, ref_module=module)
            )
        )
        if not len(d) >= 1:
            mod_logger.error(
                f"The file {module.__file__} has more than one mod defined in it. "
                "Only define one mod per file."
            )
        if len(d) == 0:
            # No mod in the file. Just return
            return False
        mod_name = list(d.keys())[0]
        mod = d[mod_name]
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
        # Only get mod states if the mod name doesn't already have a cached
        # state, otherwise it will override it.
        if mod_name not in self.mod_states:
            mod_states = list(
                inspect.getmembers(
                    mod,
                    _is_mod_state_predicate
                )
            )
            self.mod_states[mod_name] = mod_states
        if not mod_name.startswith("_INTERNAL_"):
            self._mod_paths[mod_name] = module

        return True

    def load_mod(self, fpath) -> bool:
        """ Load a mod from the given filepath. """
        module = _import_file(fpath)
        if module is None:
            return False
        return self._load_module(module)


    def load_mod_folder(self, folder: str):
        for file in os.listdir(folder):
            if file.endswith(".py"):
                self.load_mod(op.join(folder, file))

    def _register_funcs(self, mod: NMSMod, quiet: bool):
        for hook in mod.hooks:
            self.hook_manager.register_function(hook, True, mod, quiet)
        for main_loop_func in mod._main_funcs:
            self.hook_manager.add_main_loop_func(main_loop_func)
        for func in mod._state_change_funcs:
            self.hook_manager.add_state_change_func(func._trigger_on_state, func)
        for hotkey_func in mod._hotkey_funcs:
            # Don't need to tell the hook manager, register the keyboard
            # hotkey here...
            # NOTE: The below is a "hack"/"solution" to an issue that the
            # keyboard library has.
            # cf. https://github.com/boppreh/keyboard/issues/584
            cb = keyboard.hook(
                lambda e, func=hotkey_func, name=hotkey_func._hotkey, event_type=hotkey_func._hotkey_press: (
                    e.name == name and
                    e.event_type == event_type and
                    nms.GcApplication is not None and
                    nms.GcApplication.hasFocus and
                    func()
                )
            )
            self.hotkey_callbacks[
                (hotkey_func._hotkey, hotkey_func._hotkey_press)
            ] = cb

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
            self._register_funcs(mod, quiet)
            # If we get here, then the mod has been loaded successfully.
            # Add the name to the loaded mod names set so we can then remove the
            # mod from the preloaded mods dict.
            _loaded_mod_names.add(name)
        for name in _loaded_mod_names:
            self._preloaded_mods.pop(name)
        return len(_loaded_mod_names)

    def reload(self, name):
        if (mod := self.mods.get(name)) is not None:
            # First, remove everything.
            for hook in mod.hooks:
                mod_logger.info(f"Disabling hook {hook}: {hook._name}")
                hook.disable()
                hook.close()
                del hook
            for main_loop_func in mod._main_funcs:
                self.hook_manager.remove_main_loop_func(main_loop_func)
            for func in mod._state_change_funcs:
                self.hook_manager.remove_state_change_func(func._trigger_on_state, func)
            for hotkey_func in mod._hotkey_funcs:
                cb = self.hotkey_callbacks.pop(
                    (hotkey_func._hotkey, hotkey_func._hotkey_press)
                )
                keyboard.unhook(cb)

            # Then, reload the module
            module = self._mod_paths[name]
            del sys.modules[module.__name__]
            # Then, add everything back.
            self.load_mod(module.__file__)
            _loaded_mod_names = set()
            for name, _mod in self._preloaded_mods.items():
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
                self._register_funcs(mod, False)
                if mod_state := self.mod_states.get(name):
                    for ms in mod_state:
                        field, state = ms
                        setattr(mod, field, state)
                _loaded_mod_names.add(name)
            for name in _loaded_mod_names:
                self._preloaded_mods.pop(name)
            mod_logger.info(f"Finished reloading {name}")
