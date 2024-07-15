import unittest
from circles import circleArea
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circleArea(1),pi)
    
    def test_errors(self):
        self.assertRaises(ValueError,circleArea,-3)
    
unittest.main()