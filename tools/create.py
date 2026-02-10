import json
import keyword
import os.path as op
import subprocess
from typing import Union, TypedDict, Optional

import libcst as cst

from ruff.__main__ import (  # type: ignore[import-untyped]  # pyright: ignore[reportMissingTypeStubs]
    find_ruff_bin,  # noqa: PLC2701
)


DRYRUN = False


def ruff_format(source: str) -> str:
    result = subprocess.run(
        [find_ruff_bin(), "format", source],
        text=True,
        capture_output=True,
        check=True,
    )
    result.check_returncode()
    return result.stdout


# TODO: Parse the internal_enums.py file to get the names and then write this all dynamically.
ENUM_IMPORT_START = """# flake8: noqa
# ruff: noqa
from .internal_enums import (
    ResourceTypes,
    RespawnReason,
    StateEnum,
    eStormState,
    eLanguageRegion,
    EnvironmentLocation,
    EPulseDriveState,
    eFileOpenMode,
    eGraphicsDetail,
)

# The following list is auto-generated.
"""


class FieldData(TypedDict):
    Name: str
    Type: str
    Offset: int
    List: Optional[bool]
    Array_Size: Optional[int]
    Array_Enum: Optional[list]
    HashMap: Optional[bool]
    GenericTypeArgs: Optional[list[Union[str, int]]]


dirname = op.dirname(__file__)
struct_data = op.join(dirname, "struct_data.json")
ENUM_STRUCTS = []
NMSPY_DATA_DIR = op.realpath(op.join(dirname, "..", "nmspy", "data"))


def fix_name(value: str) -> str:
    if value == "":
        return "empty"
    elif value.isnumeric() or value[0].isnumeric():
        # Prefix numeric values with an underscore
        return f"_{value}"
    elif keyword.iskeyword(value):
        # Postfix keywords with an underscore
        return f"{value}_"
    return value.strip()


def upper_hex(num: int) -> str:
    hex_ = hex(num)
    return "0x" + hex_[2:].upper()


CTYPES_MAPPING = {
    "byte": "c_byte",
    "char": "c_char",
    "wchar": "c_wchar",
    "float": "c_float",
    "bool": "c_bool",
    "int8": "c_int8",
    "int16": "c_int16",
    "int32": "c_int32",
    "int64": "c_int64",
    "uint8": "c_uint8",
    "uint16": "c_uint16",
    "uint32": "c_uint32",
    "uint64": "c_uint64",
}

PYTYPES_MAPPING = {
    "byte": "bytes",
    "char": "bytes",
    "wchar": "bytes",
    "float": "float",
    "bool": "bool",
    "int8": "int",
    "int16": "int",
    "int32": "int",
    "int64": "int",
    "uint8": "int",
    "uint16": "int",
    "uint32": "int",
    "uint64": "int",
}

BASIC_TYPES = {
    "Colour",
    "Colour32",
    "GcNodeID",
    "GcResource",
    "GcSeed",
    "halfVector4",
    "HashedString",
    "TkID0x10",
    "TkID0x20",
    "cTkFixedString",
    "Vector2f",
    "Vector3f",
    "Vector4f",
    "Vector4i",
    "cTkDynamicArray",
    "VariableSizeString",
    "VariableSizeWString",
    "NMSTemplate",
    "LinkableNMSTemplate",
    "cTkFixedString0x20",
    "cTkFixedString0x40",
    "cTkFixedString0x80",
    "cTkFixedString0x100",
    "cTkFixedString0x200",
    "cTkFixedString0x400",
    "cTkFixedString0x800",
}

IGNORE_TYPES = {"ENUM"}


def pythonise_type(class_name: str, field_info: FieldData, force_ctypes: bool = True) -> cst.BaseExpression:
    type_ = field_info["Type"]
    generic_type_args = field_info.get("GenericTypeArgs")
    field_name = field_info["Name"]
    array_size = field_info.get("Array_Size")
    if force_ctypes is False:
        # In this case, we can return a python type.
        # First check whether we have an array type. If so then return the type as a tuple with some
        # unspecified number of elements.
        if (pytype_val := PYTYPES_MAPPING.get(type_)) is not None:
            if array_size is not None:
                return cst.Subscript(
                    value=cst.Name(value="tuple"),
                    slice=[
                        cst.SubscriptElement(slice=cst.Index(value=cst.Name(value=pytype_val))),
                        cst.SubscriptElement(slice=cst.Index(value=cst.Ellipsis())),
                    ]
                )
            else:
                return cst.Name(value=pytype_val)
        elif array_size is not None:
            if type_ in BASIC_TYPES:
                first_element = cst.Attribute(value=cst.Name(value="basic"), attr=cst.Name(value=type_))
            elif type_ in ENUM_STRUCTS:
                first_element = cst.Attribute(value=cst.Name(value="enums"), attr=cst.Name(value=type_))
            else:
                first_element = cst.Name(value=type_)
            return cst.Subscript(
                value=cst.Name(value="tuple"),
                slice=[
                    cst.SubscriptElement(slice=cst.Index(value=first_element)),
                    cst.SubscriptElement(slice=cst.Index(value=cst.Ellipsis())),
                ]
            )
    if (ctype_val := CTYPES_MAPPING.get(type_)) is not None:
        obj = cst.Attribute(value=cst.Name(value="ctypes"), attr=cst.Name(value=ctype_val))
        if array_size is not None:
            return cst.BinaryOperation(
                left=obj,
                operator=cst.Multiply(),
                right=cst.Integer(value=str(array_size))
            )
        return obj
    elif type_ in BASIC_TYPES:
        if generic_type_args is not None:
            elements = []
            for gtype in generic_type_args:
                if isinstance(gtype, int):
                    elements.append(cst.SubscriptElement(slice=cst.Index(value=cst.Integer(value=upper_hex(gtype)))))
                else:
                    if gtype[0] in ("'", '"'):
                        value = cst.SimpleString(value=gtype)
                    else:
                        if "." in gtype and gtype.count(".") == 1:
                            module, obj = gtype.split(".")
                            value = cst.Attribute(value=cst.Name(value=module), attr=cst.Name(value=obj))
                        else:
                            # Check to see if the type is the same as the name of the class. If it is we need
                            # to write it as a string instead.
                            if gtype == class_name:
                                # Just return because there can't be more than one generic arg in this case.
                                return cst.SimpleString(value=f'"basic.{type_}[{gtype}]"')
                            if (ctype_val := CTYPES_MAPPING.get(gtype)) is not None:
                                value = cst.Attribute(value=cst.Name(value="ctypes"), attr=cst.Name(value=ctype_val))
                            elif gtype in BASIC_TYPES:
                                value = cst.Attribute(value=cst.Name(value="basic"), attr=cst.Name(value=gtype))
                            elif gtype in ENUM_STRUCTS:
                                # Enums need to be wrapped in a c_enum32 generic type.
                                value = cst.Subscript(
                                    value=cst.Name(value="c_enum32"),
                                    slice=[
                                        cst.SubscriptElement(
                                            slice=cst.Index(
                                                cst.Attribute(
                                                    value=cst.Name(value="enums"), attr=cst.Name(value=gtype)
                                                )
                                            )
                                        )
                                    ]
                                )
                            else:
                                value = cst.Name(value=gtype)
                    elements.append(cst.SubscriptElement(slice=cst.Index(value=value)))
            obj = cst.Subscript(
                value=cst.Attribute(value=cst.Name(value="basic"), attr=cst.Name(value=type_)),
                slice=elements,
            )
            if array_size is not None:
                return cst.BinaryOperation(
                    left=obj,
                    operator=cst.Multiply(),
                    right=cst.Integer(value=str(array_size))
                )
            return obj
        else:
            obj = cst.Attribute(value=cst.Name(value="basic"), attr=cst.Name(value=type_))
            if array_size is not None:
                return cst.BinaryOperation(
                    left=obj,
                    operator=cst.Multiply(),
                    right=cst.Integer(value=str(array_size))
                )
            return obj
    elif type_ in ENUM_STRUCTS:
        # Enums need to be wrapped in a c_enum32 generic type.
        obj = cst.Subscript(
            value=cst.Name(value="c_enum32"),
            slice=[
                cst.SubscriptElement(
                    slice=cst.Index(
                        cst.Attribute(
                            value=cst.Name(value="enums"),
                            attr=cst.Name(value=type_)
                        )
                    )
                )
            ]
        )
        if array_size is not None:
            return cst.BinaryOperation(
                left=obj,
                operator=cst.Multiply(),
                right=cst.Integer(value=str(array_size))
            )
        return obj
    elif type_ == "ENUM":
        # For the inline enums, we need to create a c_enum32 like above, but with a
        # constructed name.
        return cst.Subscript(
            value=cst.Name(value="c_enum32"),
            slice=[
                cst.SubscriptElement(
                    slice=cst.Index(
                        cst.Name(value=f"e{field_name}Enum")
                    )
                )
            ]
        )
    # Must be another struct (hopefully) already defined.
    obj = cst.Name(value=type_)
    if array_size is not None:
        return cst.BinaryOperation(
            left=obj,
            operator=cst.Multiply(),
            right=cst.Integer(value=str(array_size))
        )
    return obj


def create_enum(enum_name: str, enum_fields: list[tuple[str, int]], inline: bool = False):
    enum_class = cst.ClassDef(
        name=cst.Name(enum_name),
        body=cst.IndentedBlock(
            body=[
                cst.SimpleStatementLine(
                    body=[
                        cst.Assign(
                            targets=[
                                cst.AssignTarget(
                                    target=cst.Name(value=fix_name(name)
                                    )
                                )
                            ],
                            value=cst.Integer(
                                value=upper_hex(value)
                            ),
                        )
                    ]
                )
                for name, value in enum_fields
            ]
        ),
        bases=[cst.Arg(value=cst.Name(value="IntEnum"))],
        leading_lines=[cst.EmptyLine(indent=False)] * 2 * (not inline)
    )
    return enum_class


def convert_field(class_name: str, field: FieldData) -> Union[
    cst.SimpleStatementLine,
    tuple[cst.ClassDef, cst.SimpleStatementLine]
]:
    ctypetype = pythonise_type(class_name, field)
    pytype = pythonise_type(class_name, field, False)
    if pytype.deep_equals(ctypetype):
        field_line = cst.SimpleStatementLine(
            body=[
                cst.AnnAssign(
                    target=cst.Name(value=field["Name"]),
                    annotation=cst.Annotation(
                        annotation=cst.Subscript(
                            value=cst.Name(value="Annotated"),
                            slice=[
                                cst.SubscriptElement(
                                    slice=cst.Index(
                                        value=ctypetype,
                                    )
                                ),
                                cst.SubscriptElement(
                                    slice=cst.Index(
                                        value=cst.Integer(value=upper_hex(field["Offset"]))
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
        )
    else:
        field_line = cst.SimpleStatementLine(
            body=[
                cst.AnnAssign(
                    target=cst.Name(value=field["Name"]),
                    annotation=cst.Annotation(
                        annotation=cst.Subscript(
                            value=cst.Name(value="Annotated"),
                            slice=[
                                cst.SubscriptElement(
                                    slice=cst.Index(
                                        value=pytype,
                                    )
                                ),
                                cst.SubscriptElement(
                                    slice=cst.Index(
                                        value=cst.Call(
                                            func=cst.Name(value="Field"),
                                            args=[
                                                cst.Arg(
                                                    value=ctypetype,
                                                ),
                                                cst.Arg(
                                                    value=cst.Integer(value=upper_hex(field["Offset"]))
                                                )
                                            ]
                                        )
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
        )
    if field["Type"] == "ENUM":
        # We need to also create an inline enum.
        return (create_enum(f"e{field['Name']}Enum", field.get("Enum_Values", []), True), field_line,)
    else:
        return field_line


def create_class(class_name: str, class_fields: list[FieldData]):
    body_fields = []
    for field in class_fields:
        converted_field = convert_field(class_name, field)
        if isinstance(converted_field, tuple):
            body_fields.extend(converted_field)
        else:
            body_fields.append(converted_field)
    class_class = cst.ClassDef(
        name=cst.Name(value=class_name),
        body=cst.IndentedBlock(
            body=body_fields,
        ),
        bases=[cst.Arg(value=cst.Name(value="Structure"))],
        decorators=[
            cst.Decorator(decorator=cst.Name(value="partial_struct"))
        ],
        leading_lines=[cst.EmptyLine(indent=False)] * 2,
    )
    return class_class


def _extract_dependencies(fields: list[FieldData]) -> set[str]:
    dependencies = set()
    for field in fields:
        _type = field["Type"]
        if _type not in CTYPES_MAPPING and _type not in BASIC_TYPES and _type not in IGNORE_TYPES:
            dependencies.add(_type)
        if (gen_args := field.get("GenericTypeArgs")) is not None:
            for gen_arg in gen_args:
                if isinstance(gen_arg, str):
                    if gen_arg not in CTYPES_MAPPING and gen_arg not in BASIC_TYPES and gen_arg not in IGNORE_TYPES:
                        dependencies.add(gen_arg)
    return dependencies


def handle_dependencies(data: list[dict]) -> list[dict]:
    # Keep track of the structs we need to still do.
    total_count = len(data)
    curr_todo_list = data
    next_todo_list = []
    placed_dependencies: set[str] = set()
    new_order = []
    prev_count = 0
    i = 1
    while True:
        for struct in curr_todo_list:
            name = struct["Name"]
            deps = _extract_dependencies(struct.get("Fields", [{}]))
            # If all the dependencies are satisfied, then we add it to the array in the "new order".
            # Exclude the struct name from it's list of dependencies since we can resolve that.
            if (deps - {name,}) <= placed_dependencies:
                new_order.append(struct)
                placed_dependencies.add(name)
            else:
                next_todo_list.append(struct)
        print(f"After attempt {i}: {len(new_order)} / {total_count} placed")
        if prev_count == len(new_order):
            break
        else:
            prev_count = len(new_order)
            # Swap todo lists so that we only process the unplaced structs.
            curr_todo_list = next_todo_list
            next_todo_list = []
            i += 1
    for struct in curr_todo_list:
        print(struct["Name"], _extract_dependencies(struct.get("Fields", [{}])))
    return new_order


if __name__ == "__main__":
    with open(struct_data, "r") as f:
        struct_data = json.load(f)
    # Re-order structs so that any struct which depends on another is placed after it.
    struct_data = handle_dependencies(struct_data)
    enum_module_body: list[Union[cst.SimpleStatementLine, cst.BaseCompoundStatement]] = [
        cst.SimpleStatementLine(
            body=[
                cst.ImportFrom(
                    module=cst.Name("enum"),
                    names=[cst.ImportAlias(name=cst.Name("IntEnum"))]
                )
            ]
        )
    ]

    data_module_body: list[Union[cst.SimpleStatementLine, cst.BaseCompoundStatement]] = [
        cst.SimpleStatementLine(
            body=[cst.Import(names=[cst.ImportAlias(name=cst.Name("ctypes"))])]
        ),
        cst.SimpleStatementLine(
            body=[
                cst.ImportFrom(
                    module=cst.Name("enum"),
                    names=[cst.ImportAlias(name=cst.Name("IntEnum"))]
                )
            ]
        ),
        cst.SimpleStatementLine(
            body=[
                cst.ImportFrom(
                    module=cst.Name("typing"),
                    names=[cst.ImportAlias(name=cst.Name("Annotated"))]
                )
            ]
        ),
        cst.SimpleStatementLine(
            body=[
                cst.ImportFrom(
                    module=cst.Attribute(
                        value=cst.Attribute(
                            value=cst.Name(value="pymhf"),
                            attr=cst.Name("core")
                        ),
                        attr=cst.Name(value="hooking")
                    ),
                    names=[
                        cst.ImportAlias(
                            name=cst.Name(value="Structure")
                        )
                    ]
                )
            ],
            leading_lines=[cst.EmptyLine(indent=False)],
        ),
        cst.SimpleStatementLine(
            body=[
                cst.ImportFrom(
                    module=cst.Attribute(
                        value=cst.Attribute(
                            value=cst.Name(value="pymhf"),
                            attr=cst.Name("utils")
                        ),
                        attr=cst.Name(value="partial_struct")
                    ),
                    names=[
                        cst.ImportAlias(
                            name=cst.Name(value="partial_struct")
                        ),
                        cst.ImportAlias(
                            name=cst.Name(value="Field")
                        ),
                    ]
                )
            ],
        ),
        cst.SimpleStatementLine(
            body=[
                cst.ImportFrom(
                    module=cst.Attribute(
                        value=cst.Attribute(
                            value=cst.Name(value="pymhf"),
                            attr=cst.Name("extensions")
                        ),
                        attr=cst.Name(value="ctypes")
                    ),
                    names=[
                        cst.ImportAlias(
                            name=cst.Name(value="c_enum32")
                        ),
                    ]
                )
            ],
        ),
        cst.SimpleStatementLine(
            body=[
                cst.Import(
                    names=[
                        cst.ImportAlias(
                            name=cst.Attribute(
                                value=cst.Attribute(
                                    value=cst.Name(value="nmspy"),
                                    attr=cst.Name("data")
                                ),
                                attr=cst.Name(value="basic_types")
                            ),
                            asname=cst.AsName(
                                name=cst.Name(value="basic")
                            )
                        )
                    ]
                )
            ],
            leading_lines=[cst.EmptyLine(indent=False)],
        ),
        cst.SimpleStatementLine(
            body=[
                cst.Import(
                    names=[
                        cst.ImportAlias(
                            name=cst.Attribute(
                                value=cst.Attribute(
                                    value=cst.Name(value="nmspy"),
                                    attr=cst.Name("data")
                                ),
                                attr=cst.Name(value="enums")
                            ),
                            asname=cst.AsName(
                                name=cst.Name(value="enums")
                            )
                        )
                    ]
                )
            ],
        )
    ]

    # Extract the list of structs which are in the enums module
    for struct in struct_data:
        if struct.get("EnumClass") is True:
            ENUM_STRUCTS.append(struct["Name"])

    for struct in struct_data:
        name = struct["Name"]
        fields: list[FieldData] = struct.get("Fields", [{}])
        if struct.get("EnumClass") is True:
            members = fields[0].get("Enum_Values", [])
            enum_module_body.append(create_enum(name, members))
        else:
            data_module_body.append(create_class(name, fields))
    enum_module = cst.Module(body=enum_module_body)
    data_module = cst.Module(body=data_module_body)
    # Generate the code if not doing a dry run.
    if not DRYRUN:
        with open(op.join(NMSPY_DATA_DIR, "enums", "external_enums.py"), "w") as f:
            f.write("# ruff: noqa: E741\n")
            f.write(enum_module.code)
        ruff_format(op.join(NMSPY_DATA_DIR, "enums", "external_enums.py"))

        print("Wrote enum data")
        with open(op.join(NMSPY_DATA_DIR, "exported_types.py"), "w") as f:
            f.write(data_module.code)
        ruff_format(op.join(NMSPY_DATA_DIR, "exported_types.py"))

        print("Wrote struct data")
        with open(op.join(NMSPY_DATA_DIR, "enums", "__init__.py"), "w") as f:
            f.write(ENUM_IMPORT_START)
            f.write("from .external_enums import (\n")
            for struct in struct_data:
                if struct.get("EnumClass") is True:
                    f.write(f"    {struct['Name']},\n")
            f.write(")\n")
        ruff_format(op.join(NMSPY_DATA_DIR, "enums", "__init__.py"))
        print("wrote enum imports")
