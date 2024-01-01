# Quick Reference

## Hooking

### Useful Imports

`import nmspy.data.function_hooks as hooks`

### Function Decorators

`@hooks.<function name>`:
Need to call original manually.

`@hooks.<function name>.before`:
No need to call the original function manually.
The callback will be run *before* the original function.

It is possible to pass modified arguments into the original function by returning these arguments. It is important that you pass the entire tuple of arguments required for the function. None can be omitted.

Note: You generally don't want to do a `before` hook unless you are wanting to specifically change something right before the function is called. If you want to see the state of something, check it in an `after` hook.

`@hooks.<function name>.after`:
No need to call the original function manually.
The callback will be run *after* the original function.

The function should take the same number of arguments as the original function, however you may add a `_result_` argument to the end of the result list which will contain the result of the original function.

Note: This hook is generally what you want when you are trying to inspect the state of something. This is because the original function generally modifies or sets the state.


## Keyboard bindings
