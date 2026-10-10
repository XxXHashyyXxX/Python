#!/usr/bin/env python


def stringify(nums: list[int]) -> str:
    return "".join([str(num) for num in nums])


tests = [([1, 2, 3], "123"), ([0, 0, 0], "000")]
for test in tests:
    nums = test[0]
    expected_line = test[1]
    line = stringify(nums)
    assert line == expected_line
