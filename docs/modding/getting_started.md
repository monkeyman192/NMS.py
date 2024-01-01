# Concepts

Memory modding a deep and complicated topic. I won't cover all the details here but I will try and explain some useful concepts which will hopefully make writing mods with NMS.py and any other similar tools easier.

## Hooking

A key concept we shall be using regularly is that of *function hooking*, or just *hooking* for short. This is the process of replacing one function with a different one.
We shall refer to the function we are hooking the *original* function, and the function we are replacing it with as the *detour* function.

The function which replaces the original one must take the same arguments and return the same data type as the original function.

In NMS.py we achieve this by decorating the function which we wish to use as the *detour* function with a function which is the name of the *original* function.
For example if you wish to create a hook for the `cGcVehicleComponent::GetUnderwaterDepth` function, you would decorate the function with the `hooks.cGcVehicleComponent.GetUnderwaterDepth` decorator.
All the available functions to hook are found via code completion, so you'll be able to see the full list in your IDE.

Normally when hooking a function you would need to explicitly call the original function so that any logic done by the executable can still be ran, then you'd either make some changes to the arguments passed in to this call, or do something with the result. This is true in NMS.py, however there are some conveniences which make this much easier.
When decorating a function, you can add `.before` or `.after` to the end of the decorator and it will run your detour function either before or after the original function, without you needing to call the original function yourself.

## Structs

As with all applications, NMS has a large number of structs which are used internally by the games to keep track of everything happening, from player position, to the loaded asteroid fields, to the state of vegetation on a planet.

NMS.py exposes as many of these as possible and tries to make it as easy as possible to read and modify these so that you can make deep changes to the game easily.

Many functions will take a pointer to the instance of the object it is acting on (aka `this`), which is often what you will be wanting to convert to an actual object.
NMS.py provides the convenience method `map_struct` which takes in the offset of an object and returns the object itself. This object then may have any number of fields which are exposed and searchable in your IDE.
