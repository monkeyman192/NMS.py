import json
import shutil

import libcst as cst
from libcst.helpers import parse_template_module


class FuncTransformer(cst.CSTTransformer):
    def __init__(self, data: dict):
        super().__init__()
        self.data = data
        self.visited_decorators = set()
        self.current_class_stack = []
        self.pattern_mapping = {}
        self.visited_classes = set()

    def get_func_signature(self, node: cst.FunctionDef):
        for _decorator in node.decorators:
            decorator = _decorator.decorator
            if isinstance(decorator, cst.Call):
                if isinstance(decorator.func, cst.Name):
                    decorator_func_name = decorator.func.value
                    if decorator_func_name in ("function_hook", "static_function_hook"):
                        current_function = "::".join([*self.current_class_stack, node.name.value])
                        expected_pattern = self.data.get(current_function)
                        decorator_args = decorator.args
                        for arg in decorator_args:
                            if arg.keyword is not None:
                                if arg.keyword.value == "signature":
                                    self.visited_decorators.add(current_function)
                                    sig_value: cst.SimpleString = arg.value
                                    if sig_value.raw_value != expected_pattern:
                                        self.pattern_mapping[sig_value.raw_value] = expected_pattern
                                        # print(self.pattern_mapping)
                                    return
                        if len(decorator_args) > 0:
                            self.visited_decorators.add(current_function)
                            sig_value: cst.SimpleString = decorator_args[0].value
                            if sig_value.raw_value != expected_pattern:
                                self.pattern_mapping[sig_value.raw_value] = expected_pattern
                                # print(self.pattern_mapping)
                            return

    def visit_FunctionDef(self, node: cst.FunctionDef):
        self.get_func_signature(node)
        return len(node.decorators) != 0

    def leave_SimpleString(self, original_node: cst.SimpleString, updated_node: cst.SimpleString):
        if (replacement_str := self.pattern_mapping.get(original_node.raw_value)) is not None:
            print("Updating")
            return updated_node.with_changes(value=f'"{replacement_str}"')
        return updated_node

    def visit_ClassDef(self, node):
        self.current_class_stack.append(node.name.value)
        self.visited_classes.add(node.name.value)
        return True

    def leave_ClassDef(self, original_node, updated_node):
        self.current_class_stack.pop(-1)
        return updated_node


def update_decorator_info(source_code: str, data: dict) -> cst.Module:
    tree = cst.parse_module(source_code)
    transformer = FuncTransformer(data)
    new_tree = tree.visit(transformer)
    added_functions = set(data.keys()) - transformer.visited_decorators
    print(added_functions)

    # for added_func in added_functions:
    #     func_path = added_func.split("::")
    #     if len(func_path) == 1:
    #         print("Adding just a function...")
    #     else:
    #         class_name = func_path[0]
    #         func_name = func_path[-1]
    #         if added_func in transformer.visited_classes:
    #             print(f"Adding the function to an existing class - {class_name}")
    #         else:
    #             print(f"Adding a new class - {class_name}")
    #         new_sig = data[added_func]
    #         func = add_function(func_name, new_sig, False)
    #         add_class(class_name, func)

    return new_tree


def add_function(name: str, pattern: str, is_static: bool = False) -> cst.Module:
    if is_static:
        template = """
@static_function_hook({pattern})
def {name}():
    # TODO: Add parameters and return values
    pass
"""
    else:
        template = """
@function_hook({pattern})
def {name}(self):
    # TODO: Add parameters and return values
    pass
"""
    func = parse_template_module(
        template,
        name=cst.Name(name),
        pattern=cst.SimpleString(f'"{pattern}"'),
    )

    print(func.code)

    return func


def add_class(name: str, function: cst.Module):
    template = """
@partial_struct
class {name}(Structure):
    pass
"""
    cls_ = parse_template_module(
        template,
        name=cst.Name(name),
    )
    print(cls_.body[0])
    print("-----------")
    new_cls = cls_.with_changes(
        body=[*cls_.body[:-3], cst.IndentedBlock([function])]
    )

    print(new_cls.code)


if __name__ == "__main__":
    with open("data.json", "r") as f:
        _data = json.load(f)
        data = {x["name"]: x["signature"] for x in _data}
    with open("nmspy/data/types.py", "r") as f:
        original_file = f.read()
    new_tree = update_decorator_info(original_file, data)
    shutil.move("nmspy/data/types.py", "nmspy/data/types.py.bak")
    with open("nmspy/data/types.py", "w") as f:
        f.write(new_tree.code)
