import unittest

from points import Point
from rect import Rectangle


class PointsTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Point(0, 1) + Point(1, 0), Point(1, 1))

    def test_sub(self):
        self.assertEqual(Point(2, 1) - Point(1, 2), Point(1, -1))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(4, -2), 0)

    def test_cross(self):
        self.assertEqual(Point(1, 1).cross(Point(2, 1)), -1)

    def test_len(self):
        self.assertEqual(Point(3, 4).length(), 5)


class RectTests(unittest.TestCase):
    def test_cmp(self):
        self.assertEqual(
            Rectangle(Point(1, 2), Point(3, 4)), Rectangle(Point(3, 4), Point(1, 2))
        )
        self.assertNotEqual(
            Rectangle(Point(6, 7), Point(2, 9)), Rectangle(Point(6, 9), Point(2, 7))
        )

    def test_center(self):
        self.assertEqual(Rectangle(Point(1, 5), Point(3, 7)).center(), Point(2, 6))

    def test_area(self):
        self.assertEqual(Rectangle(Point(3, 3), Point(4, 5)).area(), 2)

    def test_circumference(self):
        self.assertEqual(Rectangle(Point(1, 2), Point(3, 4)).circumference(), 8)

    def test_move(self):
        r = Rectangle(Point(1, 1), Point(2, 2))
        r.move(Point(-1, 0))
        self.assertEqual(
            r,
            Rectangle(Point(0, 1), Point(1, 2)),
        )


if __name__ == "__main__":
    _ = unittest.main()
