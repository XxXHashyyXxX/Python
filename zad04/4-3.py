#!/usr/bin/env python


def factorial(n: int) -> int:
    value = 1
    for i in range(n):
        value *= i + 1
    return value


if __name__ == "__main__":
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120
