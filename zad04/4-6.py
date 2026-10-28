#!/usr/bin/env python

from collections.abc import Sequence
from typing import Any


def sum_seq(sequence: Sequence[Any]) -> int:
    value = 0

    for sub in sequence:
        if isinstance(sub, (list, tuple)):
            value += sum_seq(sub)
        else:
            value += sub

    return value


if __name__ == "__main__":
    assert sum_seq([1, (2, 3), [4, 5, (6, 7)], 8, [9], 10]) == 55
    assert sum_seq([[[[[6]]]], [[[7]]]]) == 13
