#!/usr/bin/env python


def sort_alphabetically(lines: list[str]) -> list[str]:
    result = sorted(lines)
    return result


def sort_by_length(lines: list[str]) -> list[str]:
    result = sorted(lines, key=lambda s: len(s))
    return result


tests = [(["bb", "aaa", "c"], ["aaa", "bb", "c"], ["c", "bb", "aaa"])]
for test in tests:
    lines = test[0]
    expected_alpha = test[1]
    expected_len = test[2]

    alpha = sort_alphabetically(lines)
    by_len = sort_by_length(lines)

    assert alpha == expected_alpha
    assert by_len == expected_len
