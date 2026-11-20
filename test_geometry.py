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

    def test_area_rejects_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-3)

    def test_area_rejects_letter(self):
        with self.assertRaises(TypeError):
            circle.area("a")

    def test_perimeter_rejects_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-3)

    def test_perimeter_rejects_letter(self):
        with self.assertRaises(TypeError):
            circle.perimeter("a")


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

    def test_area_rejects_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_area_rejects_letter(self):
        with self.assertRaises(TypeError):
            square.area("a")

    def test_perimeter_rejects_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)

    def test_perimeter_rejects_letter(self):
        with self.assertRaises(TypeError):
            square.perimeter("a")


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

    def test_area_rejects_negative_length(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)

    def test_area_rejects_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle.area(5, -10)

    def test_area_rejects_letter_as_length(self):
        with self.assertRaises(TypeError):
            rectangle.area("a", 10)

    def test_area_rejects_letter_as_width(self):
        with self.assertRaises(TypeError):
            rectangle.area(5, "a")

    def test_perimeter_rejects_negative_length(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 10)

    def test_perimeter_rejects_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(5, -10)

    def test_perimeter_rejects_letter_as_length(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("a", 10)

    def test_perimeter_rejects_letter_as_width(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(5, "a")


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

    def test_area_rejects_negative_base(self):
        with self.assertRaises(ValueError):
            triangle.area(-6, 4)

    def test_area_rejects_negative_height(self):
        with self.assertRaises(ValueError):
            triangle.area(6, -4)

    def test_area_rejects_letter_as_base(self):
        with self.assertRaises(TypeError):
            triangle.area("a", 4)

    def test_area_rejects_letter_as_height(self):
        with self.assertRaises(TypeError):
            triangle.area(6, "a")

    def test_perimeter_rejects_negative_first_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_rejects_negative_second_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -4, 5)

    def test_perimeter_rejects_negative_third_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 4, -5)

    def test_perimeter_rejects_letter_as_first_side(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("a", 4, 5)

    def test_perimeter_rejects_letter_as_second_side(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, "a", 5)

    def test_perimeter_rejects_letter_as_third_side(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, 4, "a")
