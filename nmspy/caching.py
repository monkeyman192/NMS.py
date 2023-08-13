# A collection of functions which will hash and cache things.

import hashlib
from io import BufferedReader


def hash_bytes(fileobj: BufferedReader, _bufsize: int = 2 ** 18) -> str:
    # Essentially implement hashlib.file_digest since it's python 3.11+
    # cf. https://github.com/python/cpython/blob/main/Lib/hashlib.py#L195
    digestobj = hashlib.sha256()
    buf = bytearray(_bufsize)  # Reusable buffer to reduce allocations.
    view = memoryview(buf)
    while True:
        size = fileobj.readinto(buf)
        if size == 0:
            break  # EOF
        digestobj.update(view[:size])
    return digestobj.hexdigest()


class HashCache():
    pass
