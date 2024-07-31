from importlib.metadata import version, PackageNotFoundError


try:
    __version__ = version("nmspy")
except PackageNotFoundError:
    pass

from nmspy._types import NMSMod  # noqa

import nmspy.data.structs
import nmspy.data

__pymhf_types__ = nmspy.data.structs
__pymhf_functions__ = nmspy.data.functions
