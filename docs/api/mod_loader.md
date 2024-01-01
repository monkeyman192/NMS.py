# Mod Loader

The `mod_loader.py` file contains a number of functions and classes related to loading of mods.

## Classes

### `class ModState(ABC)`:
    This class is the Base class which is used to indicate that the inheriting class is a "Mod State" (see docs...) # TODO: add link.

### `class NMSMod(ABC)`:
    The base class for any mod.
    No methods are currently defined on this class, however, if your mod class has its own `__init__` method, then you MUST call `super().__init__()` in it otherwise the mod will not be properly initialised and an error will be raised to indicate this.

### `class ModManager()`:
    # TODO
