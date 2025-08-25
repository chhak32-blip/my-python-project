import sys
from calculator import Calculator

def run_demo():
    """Run a non-interactive demo for CI/CD pipelines."""
    calc = Calculator()
    print("🧮 Welcome to the Simple Calculator!")
    print("========================================")
    print("Demonstrating calculator functions:")

    print("5 + 3 =", calc.add(5, 3))
    print("10 - 4 =", calc.subtract(10, 4))
    print("6 × 7 =", calc.multiply(6, 7))
    print("15 ÷ 3 =", calc.divide(15, 3))
    print("2³ =", calc.power(2, 3))
    print("√16 =", calc.square_root(16))

def run_interactive():
    """Run the calculator in interactive mode (local only)."""
    calc = Calculator()
    print("\n🔢 Interactive Calculator Mode")
    print("Enter two numbers and an operation (+, -, *, /, ^, sqrt)")
    print("Type 'quit' to exit")

    while True:
        try:
            user_input = input("Enter calculation (e.g., '5 + 3') or 'quit': ")
            if user_input.lower() == "quit":
                break
            parts = user_input.split()
            
            if len(parts) == 2 and parts[0].lower() == "sqrt":
                num = float(parts[1])
                print("Result:", calc.square_root(num))
            elif len(parts) == 3:
                a = float(parts[0])
                op = parts[1]
                b = float(parts[2])
                if op == "+":
                    print("Result:", calc.add(a, b))
                elif op == "-":
                    print("Result:", calc.subtract(a, b))
                elif op == "*":
                    print("Result:", calc.multiply(a, b))
                elif op == "/":
                    print("Result:", calc.divide(a, b))
                elif op == "^":
                    print("Result:", calc.power(a, b))
                else:
                    print("❌ Unknown operator")
            else:
                print("❌ Invalid input format")
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    if "--ci" in sys.argv:   # Jenkins mode
        run_demo()
    else:                   # Local mode
        run_demo()
        run_interactive()
