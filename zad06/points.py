from __future__ import annotations

from math import sqrt
from typing import overload, override


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @override
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @override
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    @override
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented

        return self.x != other.x or self.y != other.y

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    @overload
    def __mul__(self, other: Point) -> float:
        return self.x * other.x + self.y * other.y

    @overload
    def __mul__(self, other: float) -> Point:
        return Point(self.x * other, self.y * other)

    def __mul__(self, other: float | Point) -> Point | float:
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        else:
            return Point(self.x * other, self.y * other)

    def __rmul__(self, other: float) -> Point:
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> Point:
        return Point(self.x / other, self.y / other)

    def cross(self, other: Point) -> float:
        return self.x * other.y - self.y * other.x

    def length(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y)

    @override
    def __hash__(self) -> int:
        return hash((self.x, self.y))
