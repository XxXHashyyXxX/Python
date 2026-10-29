import random
from itertools import cycle


def iter_01():
    return cycle([0, 1])


def iter_direction():
    while True:
        yield random.choice(["N", "E", "S", "W"])


def iter_weekdays():
    return cycle(range(7))


if __name__ == "__main__":
    iter_01_instance = iter_01()
    iter_direction_instance = iter_direction()
    iter_weekdays_instance = iter_weekdays()

    assert [next(iter_01_instance) for _ in range(10)] == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert [next(iter_weekdays_instance) for _ in range(10)] == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        0,
        1,
        2,
    ]

    directions = [next(iter_direction_instance) for _ in range(10)]
    assert len(directions) == 10
    assert all(d in {"N", "E", "S", "W"} for d in directions)
