#!/usr/bin/env python3
"""
Simple Python Application - Calculator Demo
This is the main entry point of our application.
"""

from calculator import Calculator

def main():
    """Main function to demonstrate our calculator"""
    print("🧮 Welcome to the Simple Calculator!")
    print("=" * 40)
    
    # Create calculator instance
    calc = Calculator()
    
    # Demonstrate basic operations
    print("Demonstrating calculator functions:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 × 7 = {calc.multiply(6, 7)}")
    print(f"15 ÷ 3 = {calc.divide(15, 3)}")
    print(f"2³ = {calc.power(2, 3)}")
    print(f"√16 = {calc.square_root(16)}")
    
    # Interactive mode
    print("\n🔢 Interactive Calculator Mode")
    print("Enter two numbers and an operation (+, -, *, /, ^, sqrt)")
    print("Type 'quit' to exit")
    
    while True:
        try:
            user_input = input("\nEnter calculation (e.g., '5 + 3') or 'quit': ").strip()
            
            if user_input.lower() == 'quit':
                print("👋 Thanks for using the calculator!")
                break
            
            # Handle square root (special case)
            if 'sqrt' in user_input:
                number = float(user_input.replace('sqrt', '').strip())
                result = calc.square_root(number)
                print(f"√{number} = {result}")
                continue
            
            # Parse regular operations
            parts = user_input.split()
            if len(parts) != 3:
                print("❌ Please enter in format: number operator number")
                continue
            
            num1, operator, num2 = float(parts[0]), parts[1], float(parts[2])
            
            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                result = calc.divide(num1, num2)
            elif operator == '^':
                result = calc.power(num1, num2)
            else:
                print("❌ Unknown operator. Use +, -, *, /, ^, or sqrt")
                continue
            
            print(f"✅ {num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("❌ Please enter valid numbers")
        except ZeroDivisionError:
            print("❌ Cannot divide by zero!")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
