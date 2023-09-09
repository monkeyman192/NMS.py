import json
import os.path as op

from nmspy import _internal


def dump_resource(res, fname):
    with open(op.join(_internal.CWD, fname), "w") as f:
        f.write(json.dumps(res, indent=2))
