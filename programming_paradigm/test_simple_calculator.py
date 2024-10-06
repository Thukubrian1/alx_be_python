import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(3,5), -2)
        self.assertEqual(self.calc.subtract(-5,3), -2)
        self.assertEqual(self.calc.subtract(-5,-3), -8)
        self.assertEqual(self.calc.subtract(5,-3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6,3), 18)
        self.assertEqual(self.calc.multiply(6,6), 36)
        self.assertEqual(self.calc.multiply(6,0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(15,3), 5)
        self.assertEqual(self.calc.divide(3,0), "Cannot divide by 0")
        self.assertEqual(self.calc.divide(0,3), 0)