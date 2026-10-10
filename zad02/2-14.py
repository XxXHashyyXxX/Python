#!/usr/bin/env python


def longest_word(line: str) -> str:
    return max(line.split(), key=len)


def longest_word_len(line: str) -> int:
    return len(longest_word(line))


tests = [
    ("short test abcdefghijklmnop", "abcdefghijklmnop", 16),
    ("this is a long test with an incredibly long word", "incredibly", 10),
]
for test in tests:
    line = test[0]
    expected_word = test[1]
    expected_len = test[2]

    word = longest_word(line)
    found_len = longest_word_len(line)
    assert word == expected_word
    assert found_len == expected_len
