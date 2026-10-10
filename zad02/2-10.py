#!/usr/bin/env python


def words_count(lines: str):
    return len(lines.split())


tests = [
    ("""a short line""", 3),
    ("""this is a longer line""", 5),
    (
        """this is an
    even longer line
    with a lot
    of newlines
    for testing""",
        13,
    ),
]

for test in tests:
    lines = test[0]
    expected_count = test[1]
    count = words_count(lines)
    assert count == expected_count
