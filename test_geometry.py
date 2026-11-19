import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_with_integer_radius(self):
        self.assertAlmostEqual(circle.area(3), 28.274333882308, places=9)

    def test_area_with_zero_radius(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_with_fractional_radius(self):
        self.assertAlmostEqual(circle.area(0.5), 0.785398163397, places=9)

    def test_perimeter_with_integer_radius(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.849555921539, places=9)

    def test_perimeter_with_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_with_fractional_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.5), 3.141592653590, places=9)


class SquareTestCase(unittest.TestCase):
    def test_area_with_integer_side(self):
        self.assertEqual(square.area(5), 25)

    def test_area_with_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_area_with_fractional_side(self):
        self.assertEqual(square.area(2.5), 6.25)

    def test_perimeter_with_integer_side(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_with_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_with_fractional_side(self):
        self.assertEqual(square.perimeter(2.5), 10)


class RectangleTestCase(unittest.TestCase):
    def test_area_with_unequal_sides(self):
        self.assertEqual(rectangle.area(5, 10), 50)

    def test_area_with_zero_width(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_with_equal_sides(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_perimeter_with_unequal_sides(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)

    def test_perimeter_with_zero_width(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_perimeter_with_fractional_sides(self):
        self.assertEqual(rectangle.perimeter(2.5, 3.5), 12)


class TriangleTestCase(unittest.TestCase):
    def test_area_with_integer_dimensions(self):
        self.assertEqual(triangle.area(6, 4), 12)

    def test_area_with_zero_height(self):
        self.assertEqual(triangle.area(6, 0), 0)

    def test_area_with_fractional_dimensions(self):
        self.assertEqual(triangle.area(2.5, 3), 3.75)

    def test_perimeter_with_unequal_sides(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_with_equal_sides(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)

    def test_perimeter_with_fractional_sides(self):
        self.assertEqual(triangle.perimeter(2.5, 3.25, 4), 9.75)
