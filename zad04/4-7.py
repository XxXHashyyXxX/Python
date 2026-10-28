#!/usr/bin/env python

from collections.abc import Sequence
from typing import Any


def flatten(sequence: Sequence[Any]) -> list[int]:
    output = []

    for sub in sequence:
        if isinstance(sub, (list, tuple)):
            output.extend(flatten(sub))
        else:
            output.append(sub)

    return output


if __name__ == "__main__":
    assert flatten([1, (2, [3, 4, (5, 6, [7])])]) == [1, 2, 3, 4, 5, 6, 7]
    assert flatten([[[6]], [[[[[[7]]]]]]]) == [6, 7]
