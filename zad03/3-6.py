#!/usr/bin/env python


def rect(x: int, y: int) -> str:
    return ("\n" + "   ".join("|" for _ in range(x + 1)) + "\n").join(
        "---".join("+" for _ in range(x + 1)) for _ in range(y + 1)
    )


if __name__ == "__main__":
    assert rect(0, 0) == "+"
    assert rect(3, 0) == "+---+---+---+"
    assert rect(0, 2) == "+\n|\n+\n|\n+"
    assert (
        rect(2, 3)
        == "+---+---+\n|   |   |\n+---+---+\n|   |   |\n+---+---+\n|   |   |\n+---+---+"
    )
