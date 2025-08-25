#!/usr/bin/env python3
"""
Simple Python application for Jenkins pipeline demo
"""

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result"""
    return a * b

def main():
    """Main function"""
    print("🚀 Starting Python Application...")
    print("=" * 50)
    
    # Test addition
    result1 = add_numbers(10, 5)
    print(f"Addition: 10 + 5 = {result1}")
    
    # Test multiplication
    result2 = multiply_numbers(7, 3)
    print(f"Multiplication: 7 × 3 = {result2}")
    
    # Print environment info
    import sys
    print(f"Python version: {sys.version}")
    
    print("=" * 50)
    print("✅ Application completed successfully!")
    
    return result1, result2

if __name__ == "__main__":
    main()
