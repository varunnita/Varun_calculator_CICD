# test_calculator.py
# Automated tests for the calculator functions.
# These tests run automatically to verify our calculator works correctly.

import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """A collection of tests for each calculator function."""

    # ----- ADDITION TESTS -----

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        """Test adding zero to a number."""
        self.assertEqual(add(5, 0), 5)

    # ----- SUBTRACTION TESTS -----

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        """Test subtraction that results in a negative number."""
        self.assertEqual(subtract(3, 7), -4)

    # ----- MULTIPLICATION TESTS -----

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        """Test multiplying by zero (result should always be 0)."""
        self.assertEqual(multiply(100, 0), 0)

    # ----- DIVISION TESTS -----

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        self.assertEqual(divide(10, 2), 5)

    def test_divide_returns_float(self):
        """Test that division returns a decimal result when needed."""
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)


# This allows running the tests by executing: python test_calculator.py
if __name__ == "__main__":
    unittest.main()
