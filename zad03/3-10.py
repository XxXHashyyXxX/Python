#!/usr/bin/env python

from itertools import pairwise

roman2int_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman2int(roman: str) -> int:
    values = [roman2int_dict[c] for c in roman.upper()]
    value = 0

    for current, next in pairwise(values + [0]):
        value += -current if current < next else current

    return value


if __name__ == "__main__":
    assert roman2int("MMCXXXVII") == 2137
    assert roman2int("LXIX") == 69
    assert roman2int("CDXX") == 420
