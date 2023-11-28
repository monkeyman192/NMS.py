FNV_offset_basis = 0xCBF29CE484222325
FNV_prime = 0x100000001B3


def fnv_1a(input: str, length: int):
    _input = input.ljust(length, "\x00")
    _hash = FNV_offset_basis
    for char in _input:
        _hash = (ord(char) ^ _hash) & 0xFFFFFFFFFFFFFFFF
        _hash = (_hash * FNV_prime) & 0xFFFFFFFFFFFFFFFF
    return _hash
