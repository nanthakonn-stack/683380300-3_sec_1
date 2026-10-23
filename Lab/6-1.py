#0-7
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division result or an error message."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base, exponent=2):
    """Return the base raised to the exponent."""
    return base ** exponent


while True:
    print("\n===== Simple Calculator =====")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Exit")

    choice = input("Choose an operation (1-6): ")

    if choice == "6":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice. Please try again.")
        continue

    try:
        a = float(input("Enter the first number: "))

        if choice == "5":
            exponent_input = input(
                "Enter the exponent (press Enter for square): "
            )

            if exponent_input == "":
                result = power(a)
            else:
                result = power(a, float(exponent_input))

        else:
            b = float(input("Enter the second number: "))

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter a number.")

