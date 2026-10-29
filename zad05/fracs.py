from __future__ import annotations

from decimal import DivisionByZero
from typing import override


def gcd(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


class Fraction:
    num: int
    den: int

    def __init__(self, num: int, den: int):
        if den == 0:
            raise ValueError("Denumerator of a fraction cannot be zero")

        s = 1 if num * den >= 0 else -1
        num = abs(num)
        den = abs(den)

        coeff = gcd(num, den)

        self.num = s * num // coeff
        self.den = den // coeff

    @override
    def __str__(self) -> str:
        return f"{self.num}/{self.den}" if self.den != 1 else f"{self.num}"

    @override
    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"

    def __add__(self, other: Fraction) -> Fraction:
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den

        return Fraction(num, den)

    def __mul__(self, other: Fraction) -> Fraction:
        num = self.num * other.num
        den = self.den * other.den

        return Fraction(num, den)

    def __neg__(self) -> Fraction:
        return Fraction(-self.num, self.den)

    def __sub__(self, other: Fraction) -> Fraction:
        return self + (-other)

    def __pos__(self) -> Fraction:
        return self

    def __invert__(self) -> Fraction:
        return Fraction(self.den, self.num)

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.num == other.num and self.den == other.den

    @override
    def __ne__(self, value: object, /) -> bool:
        return not self == value

    def __truediv__(self, other: Fraction) -> Fraction:
        if other == Fraction(0, 1):
            raise DivisionByZero

        return self * (~other)

    def __float__(self) -> float:
        return self.num / self.den

    def __gt__(self, other: Fraction) -> bool:
        return self.num * other.den > other.num * self.den

    def __lt__(self, other: Fraction) -> bool:
        return self.num * other.den < other.num * self.den

    def __ge__(self, other: Fraction) -> bool:
        return self.num * other.den >= other.num * self.den

    def __le__(self, other: Fraction) -> bool:
        return self.num * other.den <= other.num * self.den

    @override
    def __hash__(self):
        return hash(float(self))
