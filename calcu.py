import math

PI = math.pi

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def custom_sqrt(x):
    return math.sqrt(x)

def exponentiation(x, y):
    return math.pow(x, y)

def sine(x, is_degrees=True):
    if is_degrees:
        x = math.radians(x)
    return math.sin(x)

def cosine(x, is_degrees=True):
    if is_degrees:
        x = math.radians(x)
    return math.cos(x)

def tangent(x, is_degrees=True):
    if is_degrees:
        x = math.radians(x)
    return math.tan(x)

def logarithm(x, base=10):
    return math.log(x, base)

def factorial(x):
    return math.factorial(x)

def evaluate_expression(expression, unit):
    is_degrees = unit.lower() in ["deg", "degrees"]
    try:
        # Add support for sqrt, logarithmic, and factorial operations
        expression = expression.replace("sqrt(", "custom_sqrt(")
        expression = expression.replace("log(", "logarithm(")
        expression = expression.replace("fact(", "factorial(")

        # Allow user to input "pi" for the mathematical constant π
        expression = expression.replace("pi", str(PI))

        # Use math module functions directly
        result = eval(expression, {"__builtins__": None, "custom_sqrt": custom_sqrt, "factorial": factorial},
                      {"sin": lambda x: sine(x, is_degrees),
                       "cos": lambda x: cosine(x, is_degrees),
                       "tan": lambda x: tangent(x, is_degrees),
                       "logarithm": logarithm})

        # Convert the result to float if it has a decimal point
        result = float(result) if "." in str(result) else int(result)

        # Return the result and unit
        return result, unit

    except Exception as e:
        # Print a helpful error message to the user
        print("Syntax Error:", e)
        return None, None

# Initialize result and unit
result = None
unit = None

while True:
    while True:
        # Prompt the user for the unit (degrees or radians)
        unit_choice = input("Enter unit (Degrees or Radians or Exit): ").lower()
        if unit_choice in ["deg", "degrees", "rad"]:
            break
        elif unit_choice == "exit":
            # Exit the program
            exit()
        else:
            print("Invalid unit. Please enter 'Deg' or 'Rad'.")

    while True:
        # Prompt the user to enter an expression
        expression = input(f"Enter an expression (The calculator is in {unit_choice}): (type 'exit' to exit) ")

        if expression.lower() == "exit":
            print("Exiting the calculator.")
            exit()

        # Evaluate the expression
        result, unit = evaluate_expression(expression, unit_choice)

        if result is not None:
            # Display the result in the chosen unit
            unit_display = "Degrees" if unit_choice in ["deg", "degrees"] else "Radians"
            print(f"= {result}")
        else:
            print("Result: Syntax Error")

        # Ask the user whether to continue, clear, or exit
        choice = input("Continue expression (yes), clear calculator (clr), or exit (exit): ")

        if choice == "clr":
            # Clear the calculator and prompt for the unit again
            result = None
            unit = None
            break
        elif choice == "exit":
            # Exit the program
            exit()
        elif choice != "yes":
            print("Invalid input. Please enter yes, clr, or exit.")
