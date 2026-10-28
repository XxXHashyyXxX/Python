#!/usr/bin/env python


def fibonacci(n: int) -> int:
    if n == 0:
        return 0

    previous, current = 0, 1

    for _ in range(n - 1):
        previous += current
        previous, current = current, previous

    return current


if __name__ == "__main__":
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(7) == 13
