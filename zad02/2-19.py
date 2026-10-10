#!/usr/bin/env python


def add_padding(nums: list[int]) -> list[str]:
    return [str(num).zfill(3) for num in nums]


tests = [([123, 12, 1], ["123", "012", "001"]), ([0], ["000"])]
for test in tests:
    nums = test[0]
    expected_result = test[1]
    result = add_padding(nums)
    assert result == expected_result
