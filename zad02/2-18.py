#!/usr/bin/env python


def count_zeros(num: int) -> int:
    line = str(num)
    return line.count("0")


tests = [(1000230, 4), (69420, 1), (1111111, 0)]
for test in tests:
    num = test[0]
    expected_result = test[1]
    result = count_zeros(num)
    assert result == expected_result
