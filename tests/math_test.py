import unittest
import sys
sys.path.append('srcs')
from math_add import addition


class MathTest(unittest.TestCase):
    def test_addition(self):
        actual = addition(3, 4)
        exceeded = 7
        self.assertEqual(actual, exceeded)


if __name__ == "__main__":
    unittest.main()
