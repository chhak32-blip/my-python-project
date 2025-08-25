"""
Calculator Module
Contains the Calculator class with basic mathematical operations.
"""

import math

class Calculator:
    """A simple calculator class with basic mathematical operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
        self.version = "1.0.0"
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract second number from first."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide first number by second."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """Raise base to the power of exponent."""
        result = math.pow(base, exponent)
        self._add_to_history(f"{base}^{exponent} = {result}")
        return result
    
    def square_root(self, number):
        """Calculate square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(number)
        self._add_to_history(f"√{number} = {result}")
        return result
    
    def get_history(self):
        """Return calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
    
    def _add_to_history(self, calculation):
        """Add calculation to history (private method)."""
        self.history.append(calculation)
        # Keep only last 10 calculations
        if len(self.history) > 10:
            self.history.pop(0)
    
    def get_version(self):
        """Return calculator version."""
        return self.version
