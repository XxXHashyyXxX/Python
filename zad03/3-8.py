#!/usr/bin/env python


from collections.abc import Hashable


def union[T: Hashable](a: list[T], b: list[T]) -> list[T]:
    return list(dict.fromkeys(a + b))


def intersection[T: Hashable](a: list[T], b: list[T]) -> list[T]:
    return list(dict.fromkeys(x for x in a if x in set(b)))


if __name__ == "__main__":
    assert union([1, 2, 3], [2, 3, 4]) == [1, 2, 3, 4]
    assert union(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c", "d", "e", "f"]
    assert union([1, 2, 3], []) == [1, 2, 3]

    assert intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersection(["a", "b"], ["b", "c"]) == ["b"]
    assert intersection([1, 2, 3], []) == []
