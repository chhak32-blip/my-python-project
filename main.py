import argparse
from calculator import Calculator

def run_interactive():
    calc = Calculator()
    while True:
        try:
            expr = input("Enter calculation (e.g., '5 + 3') or 'quit': ")
            if expr.lower() == "quit":
                break
            a, op, b = expr.split()
            a, b = float(a), float(b)

            if op == "+":
                print(calc.add(a, b))
            elif op == "-":
                print(calc.subtract(a, b))
            elif op == "*":
                print(calc.multiply(a, b))
            elif op == "/":
                print(calc.divide(a, b))
            else:
                print("Unknown operator")
        except Exception as e:
            print(f"❌ Error: {e}")

def run_ci():
    calc = Calculator()
    print("Running in CI mode...")
    print("2 + 3 =", calc.add(2, 3))
    print("10 - 4 =", calc.subtract(10, 4))
    print("6 * 7 =", calc.multiply(6, 7))
    print("8 / 2 =", calc.divide(8, 2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ci", action="store_true", help="Run in CI mode without input()")
    args = parser.parse_args()

    if args.ci:
        run_ci()
    else:
        run_interactive()
