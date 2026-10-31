from dataclasses import dataclass, field

from nmspy.data.xml_mixin import XmlMixin


@dataclass
class mdModInfo(XmlMixin):
    Name: str = ""
    Authors: list[str] = field(default_factory=list)
    Description: str = ""
    Version: str = ""
    IncludedMods: list["mdModInfo"] | None = None
