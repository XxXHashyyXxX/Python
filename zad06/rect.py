from typing import override

from points import Point


class Rectangle:
    pt1: Point
    pt2: Point

    def __init__(self, pt1: Point, pt2: Point):
        self.pt1 = pt1
        self.pt2 = pt2

    @override
    def __str__(self) -> str:
        return f"[{self.pt1}, {self.pt2}]"

    @override
    def __repr__(self) -> str:
        return f"Rectangle({self.pt1}, {self.pt2})"

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented

        return {self.pt1, self.pt2} == {other.pt1, other.pt2}

    @override
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented

        return {self.pt1, self.pt2} != {other.pt1, other.pt2}

    def center(self) -> Point:
        return (self.pt1 + self.pt2) / 2

    def area(self) -> float:
        t = self.pt2 - self.pt1
        return abs(t.x * t.y)

    def circumference(self) -> float:
        t = self.pt2 - self.pt1
        return 2 * (abs(t.x) + abs(t.y))

    def move(self, vec: Point):
        self.pt1 += vec
        self.pt2 += vec
