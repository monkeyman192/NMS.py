from importlib.metadata import version, PackageNotFoundError


try:
    __version__ = version("nmspy")
except PackageNotFoundError:
    pass

import nmspy.data  # noqa
