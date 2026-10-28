import unittest

from fracs import Fraction


class Tests(unittest.TestCase):
    zero: Fraction = Fraction(0, 1)

    def test_add(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))

    def test_sub_frac(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))

    def test_mul_frac(self):
        self.assertEqual(Fraction(2, 3) * Fraction(3, 8), Fraction(1, 4))

    def test_div_frac(self):
        self.assertEqual(Fraction(8, 15) / Fraction(2, 3), Fraction(4, 5))

    def test_is_positive(self):
        self.assertGreater(Fraction(1, 2), self.zero)

    def test_is_zero(self):
        self.assertEqual(Fraction(0, 3), self.zero)

    def test_cmp_frac(self):
        self.assertTrue(Fraction(2, 3) == Fraction(2, 3))
        self.assertFalse(Fraction(6, 7) == Fraction(6, 11))

    def test_frac2float(self):
        self.assertEqual(Fraction(1, 4).to_float(), 0.25)


if __name__ == "__main__":
    _ = unittest.main()
