# calculator.py
# A simple calculator that performs basic arithmetic operations.

# ----- CALCULATOR FUNCTIONS -----

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the result of a divided by b.
    Raises a ValueError if b is zero (division by zero is undefined).
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# ----- MAIN PROGRAM (runs when you execute this file directly) -----

def main():
    """Display a menu, take user input, and perform the chosen operation."""
    print("===========================")
    print("   SIMPLE CALCULATOR")
    print("===========================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("===========================")

    choice = input("Enter your choice (1/2/3/4): ")

    # Validate the menu choice
    if choice not in ("1", "2", "3", "4"):
        print("Error: Invalid choice. Please enter 1, 2, 3, or 4.")
        return  # exit the function early

    # Get numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    # Perform the chosen operation
    if choice == "1":
        result = add(num1, num2)
        operation = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operation = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operation = "*"
    elif choice == "4":
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(f"Error: {e}")
            return
        operation = "/"

    print(f"\nResult: {num1} {operation} {num2} = {result}")


# This block runs only when you execute 'python calculator.py' directly.
# It does NOT run when another file imports this file.
if __name__ == "__main__":
    main()
