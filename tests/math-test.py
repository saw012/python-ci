import unittest
import sys
sys.path.append('../src')
from math_add import addition

class MathTest(unittest.TestCase):
    def test_addition(self):
        actual = addition(3,4)
        exceeded = 8
        self.assertEqual(actual , exceeded)