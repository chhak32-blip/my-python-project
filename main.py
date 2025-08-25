import sys

def run_demo():
    print("🧮 Welcome to the Simple Calculator!")
    # your demo functions here...

def run_interactive():
    print("🔢 Interactive Calculator Mode")
    while True:
        try:
            user_input = input("Enter calculation (e.g., '5 + 3') or 'quit': ")
            if user_input.lower() == 'quit':
                break
            print("Result:", eval(user_input))  # just example, use safe parsing
        except EOFError:
            print("❌ No input available, exiting.")
            break
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    if "--ci" in sys.argv:
        run_demo()
    else:
        run_demo()
        run_interactive()
