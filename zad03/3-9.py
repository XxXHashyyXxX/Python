#!/usr/bin/env python


from collections.abc import Sequence


def sum_all(a: list[Sequence[int]]) -> list[int]:
    return [sum(seq) for seq in a]


if __name__ == "__main__":
    assert sum_all([[], [4], (1, 2), [3, 4], (5, 6, 7)]) == [0, 4, 3, 7, 18]
