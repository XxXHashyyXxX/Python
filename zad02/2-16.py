#!/usr/bin/env python


def gvr(line: str) -> str:
    return line.replace("GvR", "Guido van Rossum")


tests = [
    ("line without a phrase", "line without a phrase"),
    ("line with a GvR phrase", "line with a Guido van Rossum phrase"),
]
for test in tests:
    line = test[0]
    expected_output = test[1]
    output = gvr(line)
    assert output == expected_output
