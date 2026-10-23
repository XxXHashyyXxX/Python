#!/usr/bin/env python


def gen_meter(x: int) -> str:
    return (
        "....".join(["|" for _ in range(x)])
        + "\n"
        + "".join([f"{counter:>5}" for counter in range(x)]).lstrip()
    )


if __name__ == "__main__":
    assert gen_meter(0) == "\n"
    assert gen_meter(1) == "|\n0"
    assert gen_meter(2) == "|....|\n0    1"
    assert gen_meter(3) == "|....|....|\n0    1    2"
    assert (
        gen_meter(13)
        == "|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12"
    )
