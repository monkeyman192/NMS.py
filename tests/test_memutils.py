from nmspy.memutils import pattern_to_bytes

import pytest


def test_pattern_to_bytes():
    patt = "AB CD EF"
    assert list(pattern_to_bytes(patt)) == [0xAB, 0xCD, 0xEF]
    patt = "1 2 3 4 5"
    assert list(pattern_to_bytes(patt)) == [1, 2, 3, 4, 5]
    patt = "01 ?? 02"
    assert list(pattern_to_bytes(patt)) == [0x01, 0x100, 0x02]
    with pytest.raises(ValueError):
        pattern_to_bytes("123 04")
