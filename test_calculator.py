"""
Unit tests for the Calculator class.
These tests will be run by Jenkins to verify our code works correctly.
"""

import unittest
import math
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test calculator instance before each test."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)
    
    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(-12, 3), -4)
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(10, 2), 100)
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2)
    
    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(self.calc.square_root(16), 4)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertEqual(self.calc.square_root(1), 1)
        self.assertAlmostEqual(self.calc.square_root(2), math.sqrt(2))
    
    def test_square_root_negative(self):
        """Test square root of negative number raises exception."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)
    
    def test_history(self):
        """Test calculation history functionality."""
        # Initially empty
        self.assertEqual(len(self.calc.get_history()), 0)
        
        # Add some calculations
        self.calc.add(5, 3)
        self.calc.multiply(2, 4)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("5 + 3 = 8", history)
        self.assertIn("2 × 4 = 8", history)
        
        # Clear history
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_history_limit(self):
        """Test that history is limited to 10 entries."""
        # Add 15 calculations
        for i in range(15):
            self.calc.add(i, 1)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 10)  # Should only keep last 10
    
    def test_version(self):
        """Test version information."""
        version = self.calc.get_version()
        self.assertIsInstance(version, str)
        self.assertTrue(len(version) > 0)

if __name__ == '__main__':
    # Run tests with detailed output
    unittest.main(verbosity=2)
