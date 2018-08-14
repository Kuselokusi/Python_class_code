import unittest
from simple_math import divide
from simple_math import square
from simple_math import multiply


class TestSimpleMath(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide.divide(10, 2), 5)

    def test_square(self):
        self.assertEqual(square.square(2), 4)

    def test_multiply(self):
        self.assertEqual(multiply.multiply(2, 5), 10)


if __name__ == "__main__":
    unittest.main()
