#!/usr/bin/env python


def first_chars(line: str, n: int) -> str:
    return line[:n]


def last_chars(line: str, n: int) -> str:
    return line[-n:]


tests = [
    ("shorter line", 3, "sho", "ine"),
    ("this is a longer line for testing", 5, "this ", "sting"),
    ("too short", 20, "too short", "too short"),
]

for test in tests:
    line = test[0]
    count = test[1]
    expected_prefix = test[2]
    expected_postfix = test[3]

    prefix = first_chars(line, count)
    postfix = last_chars(line, count)

    assert prefix == expected_prefix
    assert postfix == expected_postfix
