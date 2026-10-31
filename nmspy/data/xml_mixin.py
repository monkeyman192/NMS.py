# This will contain all the "modded types".
# These are basically community custom versions of all the types which can be found in MBINCompiler.

import types
import typing
import xml.etree.ElementTree as etree
from dataclasses import fields
from enum import Enum
from os import PathLike
from typing import Any, ClassVar, TypeVar, Union

T = TypeVar("T", bound="XmlMixin")

XML_DECLARATION = '<?xml version="1.0" encoding="utf-8"?>\n'
ROOT_TAG = "Data"
ITEM_TAG = "Property"


def _is_list(type_: Any) -> bool:
    # Determine whether the type of the object is a list or not.
    return type_ is list or typing.get_origin(type_) is list


def _strip_optional(type_: Any) -> Any:
    # Strip out any Optional cases (so `T | None` -> `T`).
    origin = typing.get_origin(type_)
    if origin is Union or origin is types.UnionType:
        args = [a for a in typing.get_args(type_) if a is not type(None)]
        if len(args) == 1:
            return args[0]
    return type_


class XmlMixin:
    """
    Mixin for dataclasses that reads/writes them as a tree of <Property> elements.

    Supported field types: str, int, float, bool, Enum, other dataclasses that
    also use XmlMixin, ``list[T]`` of any of these previous types, and optional types.
    Note that optional types will not be written out if they are set to None.
    Empty lists will be written as an empty element to distinguish it from None.
    """

    # Keep track of already handled classes so that we can avoid having to re-parse them every time we come
    # across them.
    _registry: ClassVar[dict[str, type]] = {}

    def __init_subclass__(cls, **kwargs: Any):
        super().__init_subclass__(**kwargs)
        XmlMixin._registry[cls.__name__] = cls

    @classmethod
    def _hints(cls) -> dict[str, Any]:
        # Get the type hints for the class.
        return typing.get_type_hints(cls, localns={cls.__name__: cls, **cls._registry})

    def _write_fields(self, parent: etree.Element):
        # Loop over the fields, encode them and add them to the parent.
        hints = self._hints()
        for f in fields(self):  # type: ignore[arg-type]
            if not f.init:
                continue
            child = self._encode(f.name, hints[f.name], getattr(self, f.name))
            if child is not None:
                parent.append(child)

    @classmethod
    def _encode(cls, name: str, type_: Any, value: Any) -> etree.Element | None:
        # Encode the values in the class with some name, type and value.
        # When value is None, it will also just return None.
        if value is None:
            return None
        type_ = _strip_optional(type_)
        el = etree.Element(ITEM_TAG, name=name)

        if _is_list(type_):
            (item_type,) = typing.get_args(type_) or (Any,)
            for item in value:
                child = cls._encode(name, item_type, item)
                if child is not None:
                    el.append(child)
        elif isinstance(value, XmlMixin):
            el.set("value", type(value).__name__)
            value._write_fields(el)
        elif isinstance(value, Enum):
            el.set("value", value.name)
        elif isinstance(value, bool):
            el.set("value", "true" if value else "false")
        else:
            el.set("value", str(value))
        return el

    @classmethod
    def _from_element(cls: type[T], root: etree.Element) -> T:
        # Read the template and read the fields in it.
        template = root.get("template")
        target = cls._registry.get(template, cls) if template else cls
        if not issubclass(target, cls):
            target = cls
        return target._read_fields(root)  # type: ignore[return-value]

    @classmethod
    def _read_fields(cls: type[T], element: etree.Element) -> T:
        # Iterate over the fields and decode them, constructing the class instance.
        hints = cls._hints()
        by_name = {c.get("name"): c for c in element if c.tag == ITEM_TAG}
        kwargs: dict[str, Any] = {}
        for f in fields(cls):  # type: ignore[arg-type]
            if f.init and f.name in by_name:
                kwargs[f.name] = cls._decode(hints[f.name], by_name[f.name])
        return cls(**kwargs)  # type: ignore[call-arg]

    @classmethod
    def _decode(cls, type_: Any, element: etree.Element) -> Any:
        # Main decode method. This will take the type as defined by the dataclass definition, and the element
        # which is to be decoded, and decode it based on this type info.
        # The result will be a concrete python object with the value.
        type_ = _strip_optional(type_)

        if _is_list(type_):
            (item_tp,) = typing.get_args(type_) or (Any,)
            return [cls._decode(item_tp, c) for c in element if c.tag == ITEM_TAG]

        if isinstance(type_, type) and issubclass(type_, XmlMixin):
            # `value` holds the concrete class name, allowing subclasses.
            target = cls._registry.get(element.get("value", ""), type_)
            if not issubclass(target, type_):
                target = type_
            return target._read_fields(element)

        # Read the raw value from the xml and convert to a python type.
        raw = element.get("value", "")
        if type_ is bool:
            return raw.strip().lower() in ("true", "1", "yes")
        if isinstance(type_, type) and issubclass(type_, Enum):
            return type_[raw]
        if type_ in (int, float, str):
            return type_(raw)
        if type_ is Any:
            return raw
        return type_(raw)

    @classmethod
    def read(cls: type[T], source: str | PathLike[str] | typing.IO[bytes]) -> T:
        """Read the class data from a source file."""
        tree = etree.parse(source)
        if (root := tree.getroot()) is not None:
            return cls._from_element(root)
        else:
            raise ValueError("Root of tree cannot be empty.")

    @classmethod
    def from_string(cls: type[T], text: str | bytes) -> T:
        """Read the class data from the string representation."""
        return cls._from_element(etree.fromstring(text))

    def to_string(self) -> str:
        """Write the current object to a string."""
        root = etree.Element(ROOT_TAG, template=type(self).__name__)
        self._write_fields(root)
        etree.indent(root, space="    ")
        return XML_DECLARATION + etree.tostring(root, encoding="unicode") + "\n"

    def write(self, path: str | PathLike[str]):
        """Write the current object to the provided file path."""
        with open(path, "w", newline="\n") as f:
            f.write(self.to_string())
