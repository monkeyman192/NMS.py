from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("nmspy")
except PackageNotFoundError:
    pass

import nmspy.data  # noqa
