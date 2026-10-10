#!/usr/bin/env python


def insert_underscores(line: str) -> str:
    return "_".join(list(line))


tests = [("input", "i_n_p_u_t"), ("longer input", "l_o_n_g_e_r_ _i_n_p_u_t"), ("", "")]
for test in tests:
    input = test[0]
    expected_result = test[1]
    result = insert_underscores(input)
    assert result == expected_result
