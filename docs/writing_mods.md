## Writing a mod using NMS.py

NMS.py contains offsets and mappings for many functions in the game.
It aims to make hooking the various game functions as simple as possible with an easy to understand syntax.

First, we need a mod class which will contain all the relevant hooks for your mod.

The basics look something like this:

```py
from nmspy.mod_loader import NMSMod

class MyMod(NMSMod):
    __author__ = "you!"
    __description__ = "Your fantastic mod!"
    __version__ = "1.0"
```

This will do nothing, and the 3 fields provided are not required, but are useful to tell others what your mod does and who made it.

To make the mod do something we need to add some function hooks. These are methods defined on the class which are [decorated](https://docs.python.org/3/glossary.html#term-decorator) by the function you wish to hook.

This is best shown with an example:

```py
import logging
import nmspy.data.function_hooks as hooks

class MyMod(NMSMod):
    ...

    @hooks.cGcGameState.LoadSpecificSave
    def load_specific_save(self, this, leSpecificSave):
        logging.info(f"cGcGameState*: {this}, save type: {leSpecificSave}")
        ret = hooks.cGcGameState.LoadSpecificSave.original(this, leSpecificSave)
        logging.info(str(ret))
        return ret
```

The above mod will hook the `cGcGameState::LoadSpecificSave` function in the game. This function requires two arguments; `this` which is a pointer to the `cGcGameState` class, and `leSpecificSave` which is an enum. Currently there is no easy way to look up the arguments a function takes or the types, however if you are unsure, the safest method is to  define the function like so:

```py
    @hooks.cGcGameState.LoadSpecificSave
    def load_specific_save(self, *args):
```

This way you don't need to know what arguments are required, but the arguments can still be inspected.

You will notice that in the above example we had to call the `original` version of the function.
This is REQUIRED when you are decorating the method with the raw function.

If you are just interested in having some code run before or after the original function, the hook functions define a `before` and `after` attribute which will do just that.

This looks like:

```py
import logging
import nmspy.data.function_hooks as hooks

class MyMod(NMSMod):
    ...

    @hooks.cGcGameState.LoadSpecificSave.before
    def load_specific_save(self, *args):
        logging.info(f"[before] cGcGameState::LoadSpecificSave called with {args}")
```

and

```py
import logging
import nmspy.data.function_hooks as hooks

class MyMod(NMSMod):
    ...

    @hooks.cGcGameState.LoadSpecificSave.after
    def load_specific_save(self, *args):
        logging.info(f"[[after] cGcGameState::LoadSpecificSave called with {args}")
```
