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


def _is_mod_predicate(obj, ref_module):
    if inspect.getmodule(obj) == ref_module:
        return issubclass(obj, NMSMod)


def _hook_predicate(value: Any) -> bool:
    """ Filter function to only return classes which subclass NMSHook"""
    try:
        return issubclass(value, NMSHook)
    except TypeError:
        return False


def _partial_predicate(value: Any) -> bool:
    try:
        return isinstance(value, partial) and isinstance(value.func.__self__, _NMSHook)
    except TypeError:
        return False


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
            x[1] for x in inspect.getmembers(self, _hook_predicate)
        ]
        # For each hook, associate the mod with it so that it can reference it.
        for hook in self.hooks:
            hook.mod = self
        # Get members which are functional hooks
        self.func_hooks: list[NMSHook] = [
            x[1].func.__self__ for x in inspect.getmembers(self, _partial_predicate)
        ]


class ModManager():
    def __init__(self, hook_manager: HookManager):
        self.mods: dict[str, NMSMod] = {}
        self.hook_manager = hook_manager

    @staticmethod
    def load_mod(fpath) -> dict:
        mod = _import_file(fpath)
        return dict(inspect.getmembers(mod, partial(_is_mod_predicate, ref_module=mod)))

    def load_mod_folder(self, folder: str):
        for file in os.listdir(folder):
            if file.endswith(".py"):
                self.mods.update(ModManager.load_mod(op.join(folder, file)))

    def enable_all(self):
        """ Enable all mods loaded by the manager. """
        for name, mod in self.mods.items():
            mod_logger.info(f"Loading hooks for {name}")
            # Instantiate the mod, and then overwrite the object in the mods
            # attribute with the instance.
            mod: NMSMod = mod()
            self.mods[name] = mod
            for hook in mod.hooks:
                self.hook_manager.register(hook)
            for hook in mod.func_hooks:
                self.hook_manager.register_function(hook, True, mod)

    def reload(self):
        # TODO
        pass
