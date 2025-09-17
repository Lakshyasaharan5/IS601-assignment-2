"""
Calculator REPL for performing add, sub, mul and div
"""

import operations

def repl():
    print("Welcome to Lakshya's Calculator")
    print("Available commands: add, sub, mul, div, exit")

    while True:
        command = input("calc> ").strip().split()

        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "exit":
            print("Goodbye!")
            break

        if cmd in ("add", "sub", "mul", "div"):
            if len(command) != 3:
                print("Usage: <command> num1 num2")
                continue

            try:
                x = float(command[1])
                y = float(command[2])
            except ValueError:
                print("Error: Please provide two numbers")
                continue

            if cmd == "add":
                result = operations.add(x, y)
            elif cmd == "sub":
                result = operations.sub(x, y)
            elif cmd == "mul":
                result = operations.mul(x, y)
            elif cmd == "div":
                result = operations.div(x, y)

            print(result)
        else:
            print("Unknown command. Type add, sub, mul, div, or exit.")
