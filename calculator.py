# Simple command-line calculator
# Supports + - * / % ** // with input validation and a calculation history

print("SIMPLE CALCULATOR")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot be divided by 0."
    return x / y

def modulo(x, y):
    if y == 0:
        return "Error: Cannot take modulo by zero."
    return x % y

def floordivide(x, y):
    if y == 0:
        return "Error: Cannot be divided by 0."
    return x // y

def power(x, y):
    # A negative number to a fractional power gives a complex number in Python,
    # which a basic calculator shouldn't show
    if x < 0 and not y.is_integer():
        return "Error: Cannot raise a negative number to a fractional power."
    try:
        return x ** y
    except ZeroDivisionError:   # e.g. 0 ** -1
        return "Error: Zero cannot be raised to a negative power."
    except OverflowError:       # result too big for a float
        return "Error: Result is too large."

def format_result(result):
    # Show 8 instead of 8.0, but leave decimals (2.5) and error messages unchanged
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "**": power,
    "//": floordivide,
}

# Created once, outside the loop, so it keeps its entries between rounds
history = []


# Main loop

while True:
    print("\nChoose an operation from: (+ - * / % ** //), (h for history), (c for clearing history) or (q to quit)")
    op = input("Enter an operator: ")

    # Quit
    if op == "q":
        print("Program Ended")
        break

    # Show history
    if op == "h":
        if len(history) == 0:
            print("No history yet.")
        else:
            for entry in history:
                print(entry)
        continue

    # Clear history
    if op == "c":
        history.clear()
        print("History cleared.")
        continue

    # Validate the operator
    if op not in operations:
        print("Invalid operation, please try again.")
        continue

    # Validate the numbers
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid number, please enter digits only.\n")
      
    func = operations[op]
    result = format_result(func(x, y))
    print(result)

    # Save to history only if the calculation succeeded (errors are strings)
    if not isinstance(result, str):
        x = format_result(x)
        y = format_result(y)
        history.append(f"{x} {op} {y} = {result}")