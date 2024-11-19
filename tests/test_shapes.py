import unittest
import math

from src import circle, rectangle, square, triangle

class ShapesTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = circle.area(4)
        self.assertEqual(res, 16 * math.pi)
    
    def test_circle_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 10 * math.pi)
    
    def test_reactangle_area(self):
        res = rectangle.area(3, 9)
        self.assertEqual(res, 27)
    
    def test_rectangle_perimeter(self):
        res = rectangle.perimeter(9, 2)
        self.assertEqual(res, 22)
    
    def test_triangle_area(self):
        res = triangle.area(9, 5)
        self.assertEqual(res, 22.5)
    
    def test_triangle_perimeter(self):
        res = triangle.perimeter(5, 1, 3)
        self.assertEqual(res, 9)
   
    def test_square_area(self):
        res = square.area(2)
        self.assertEqual(res, 4)
    
    def test_square_perimeter(self):
        res = square.perimeter(7)
        self.assertEqual(res, 28)
    
