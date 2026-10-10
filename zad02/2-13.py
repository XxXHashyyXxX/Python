#!/usr/bin/env python


def total_length(line: str) -> int:
    words = line.split()
    lengths = [len(word) for word in words]
    return sum(lengths)


tests = [("short line", 9), ("this is a longer line for testing", 27)]
for test in tests:
    line = test[0]
    expected_length = test[1]
    length = total_length(line)
    assert length == expected_length
