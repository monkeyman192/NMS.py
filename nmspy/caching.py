# A collection of functions which will hash and cache things.

import hashlib
from io import BufferedReader
import json
import os
import os.path as op
from typing import Optional

import nmspy._internal as _internal


CACHE_DIR = ".cache"


def hash_bytes(fileobj: BufferedReader, _bufsize: int = 2 ** 18) -> str:
    # Essentially implement hashlib.file_digest since it's python 3.11+
    # cf. https://github.com/python/cpython/blob/main/Lib/hashlib.py#L195
    digestobj = hashlib.sha1()
    buf = bytearray(_bufsize)  # Reusable buffer to reduce allocations.
    view = memoryview(buf)
    while True:
        size = fileobj.readinto(buf)
        if size == 0:
            break  # EOF
        digestobj.update(view[:size])
    return digestobj.hexdigest()


class OffsetCache():
    def __init__(self, path: str):
        self._path = path
        self._binary_hash: Optional[str] = None
        self._lookup: dict[str, int] = {}

    @property
    def path(self) -> str:
        return op.join(
            _internal.CWD,
            CACHE_DIR,
            f"{self._binary_hash}_{self._path}.json"
        )

    def load(self, binary_hash: str):
        """ Load the data. """
        self._binary_hash = binary_hash
        if op.exists(self.path):
            with open(self.path, "r") as f:
               self._lookup = json.load(f)

    def save(self):
        """ Persist the cache to disk. """
        with open(self.path, "w") as f:
            json.dump(self._lookup, f)

    def get(self, name: str) -> Optional[int]:
        """ Get the offset based on the key provided. """
        return self._lookup.get(name)

    def set(self, key: str, value: int, save: bool = True):
        """ Set the key with the given value and optionally save."""
        self._lookup[key] = value
        if save:
            self.save()

    def items(self):
        for key, value in self._lookup.items():
            yield key, value


function_cache = OffsetCache("function_cache")
pattern_cache = OffsetCache("pattern_cache")
globals_cache = OffsetCache("globals_cache")
builtins_cache = OffsetCache("builtins_cache")


def load_caches(binary_hash: str):
    if not op.exists(op.join(_internal.CWD, CACHE_DIR)):
        os.makedirs(op.join(_internal.CWD, CACHE_DIR))
    function_cache.load(binary_hash)
    pattern_cache.load(binary_hash)
    globals_cache.load(binary_hash)
    builtins_cache.load(binary_hash)
