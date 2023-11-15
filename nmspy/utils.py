import json
import os.path as op

from nmspy import _internal


def dump_resource(res, fname):
    with open(op.join(_internal.CWD, fname), "w") as f:
        f.write(json.dumps(res, indent=2))


def safe_assign_enum(enum, index: int):
    """ Safely try and get the enum with the associated integer value.
    If the index isn't one in the enum return the original index."""
    try:
        return enum(index)
    except ValueError:
        return index
