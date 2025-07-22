import ast
import json


def get_func_signature(node: ast.FunctionDef):
    for decorator in node.decorator_list:
        if isinstance(decorator, ast.Call):
            if isinstance(decorator.func, ast.Name):
                decorator_func_name = decorator.func.id
                if decorator_func_name in ("function_hook", "static_function_hook"):
                    decorator_args = decorator.args
                    decorator_kwargs = decorator.keywords
                    if len(decorator_args) > 0:
                        return decorator_args[0].value
                    elif "signature" in decorator_kwargs:
                        return decorator_kwargs["signature"].value


class FuncLister(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.current_class_stack = []
        self.data = []

    def visit_FunctionDef(self, node):
        if (signature := get_func_signature(node)) is not None:
            if self.current_class_stack:
                curr_class_name = "::".join(self.current_class_stack)
                self.data.append(
                    {"name": f"{curr_class_name}.{node.name}", "signature": signature, "mangled_name": ""}
                )
            else:
                self.data.append(
                    {"name": node.name, "signature": signature, "mangled_name": ""}
                )
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        # print(f"Class: {node.name}")
        self.current_class_stack.append(node.name)
        self.generic_visit(node)
        self.current_class_stack.pop(-1)


def get_decorator_info(source_code):
    tree = ast.parse(source_code)
    parser = FuncLister()
    parser.visit(tree)
    # print(parser.data)
    # print(len(parser.data))
    with open("patterns.txt", "w") as f:
        for pattern in parser.data:
            f.write(f"{pattern['signature']}\n")
    with open("data.json", "w") as f:
        json.dump(parser.data, f, indent=1)


if __name__ == "__main__":
    with open("nmspy/data/types.py", "r") as f:
        data = get_decorator_info(f.read())
