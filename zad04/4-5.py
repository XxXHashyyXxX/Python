#!/usr/bin/env python

from typing import Any


def reverse_iter(L: list[Any], left: int, right: int) -> None:
    for i in range((right - left + 1) // 2):
        L[left + i], L[right - i] = L[right - i], L[left + i]


def reverse_rec(L: list[Any], left: int, right: int) -> None:
    if left >= right:
        return

    L[left], L[right] = L[right], L[left]
    reverse_rec(L, left + 1, right - 1)


if __name__ == "__main__":

    def test_iter(inputs: tuple[list[Any], int, int], expected: list[Any]) -> bool:
        reverse_iter(*inputs)
        return inputs[0] == expected

    def test_rec(inputs: tuple[list[Any], int, int], expected: list[Any]) -> bool:
        reverse_rec(*inputs)
        return inputs[0] == expected

    assert test_iter(([1, 2, 3], 1, 2), [1, 3, 2])
    assert test_iter(
        ([1, 2, 3, 4, 8, 7, 6, 5, 9, 10], 4, 7), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

    assert test_rec(([1, 2, 3], 1, 2), [1, 3, 2])
    assert test_rec(
        ([1, 2, 3, 4, 8, 7, 6, 5, 9, 10], 4, 7), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
