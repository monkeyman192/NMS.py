from importlib.metadata import version, PackageNotFoundError


try:
    __version__ = version("nmspy")
except PackageNotFoundError:
    __version__ = "0.6.11"
