import unittest
import math

from src import circle, rectangle, square, triangle

class ShapesTestCase(unittest.TestCase):
    # Circle tests
    def test_circle_large_values(self):
        cases = [
            (1e6, math.pi * 1e6 ** 2),
            (1e9, math.pi * 1e9 ** 2)
        ]
        for radius, expected in cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(circle.area(radius), expected, delta=1e-5)

    def test_circle_negative_values(self):
        with self.subTest("Negative radius"):
            with self.assertRaises(ValueError):
                circle.area(-10)

    def test_circle_zero_value(self):
        with self.subTest("Zero radius"):
            self.assertEqual(circle.area(0), 0)

    def test_circle_invalid_format(self):
        cases = ["string", None, [1, 2, 3], {"radius": 5}]
        for invalid_input in cases:
            with self.subTest(input=invalid_input):
                with self.assertRaises(TypeError):
                    circle.area(invalid_input)

    # Rectangle tests
    def test_rectangle_large_values(self):
        cases = [
            ((1e6, 2e6), 2e12),
            ((1e9, 1e9), 1e18)
        ]
        for (length, width), expected in cases:
            with self.subTest(length=length, width=width):
                self.assertEqual(rectangle.area(length, width), expected)

    def test_rectangle_negative_values(self):
        cases = [(-10, 5), (5, -10), (-5, -5)]
        for length, width in cases:
            with self.subTest(length=length, width=width):
                with self.assertRaises(ValueError):
                    rectangle.area(length, width)

    def test_rectangle_zero_value(self):
        cases = [(0, 5), (5, 0), (0, 0)]
        for length, width in cases:
            with self.subTest(length=length, width=width):
                self.assertEqual(rectangle.area(length, width), 0)

    def test_rectangle_invalid_format(self):
        cases = [("string", 5), (5, None), (None, None), [{}, []]]
        for length, width in cases:
            with self.subTest(length=length, width=width):
                with self.assertRaises(TypeError):
                    rectangle.area(length, width)

    # Square tests
    def test_square_large_values(self):
        cases = [
            (1e6, 1e12),
            (1e9, 1e18)
        ]
        for side, expected in cases:
            with self.subTest(side=side):
                self.assertEqual(square.area(side), expected)

    def test_square_negative_values(self):
        with self.subTest("Negative side"):
            with self.assertRaises(ValueError):
                square.area(-10)

    def test_square_zero_value(self):
        with self.subTest("Zero side"):
            self.assertEqual(square.area(0), 0)

    def test_square_invalid_format(self):
        cases = ["string", None, [1, 2, 3], {"side": 5}]
        for invalid_input in cases:
            with self.subTest(input=invalid_input):
                with self.assertRaises(TypeError):
                    square.area(invalid_input)

    # Triangle tests
    def test_triangle_large_values(self):
        cases = [
            ((1e6, 2e6), 1e6 * 2e6 / 2),
            ((1e9, 1e9), 1e9 * 1e9 / 2)
        ]
        for (base, height), expected in cases:
            with self.subTest(base=base, height=height):
                self.assertEqual(triangle.area(base, height), expected)

    def test_triangle_negative_values(self):
        cases = [(-10, 5), (5, -10), (-5, -5)]
        for base, height in cases:
            with self.subTest(base=base, height=height):
                with self.assertRaises(ValueError):
                    triangle.area(base, height)

    def test_triangle_zero_value(self):
        cases = [(0, 5), (5, 0), (0, 0)]
        for base, height in cases:
            with self.subTest(base=base, height=height):
                self.assertEqual(triangle.area(base, height), 0)
    
    def test_triangle_invalid_format(self):
        cases = [("string", 5), (5, None), (None, None), [{}, []]]
        for base, height in cases:
            with self.subTest(base=base, height=height):
                with self.assertRaises(TypeError):
                    triangle.area(base, height)