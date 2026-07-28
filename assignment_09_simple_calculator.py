# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def add(numbers):
    return sum(numbers)


def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return None
        result /= num
    return round(result, 2)


def modulus(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return None
        result %= num
    return result


def exponentiate(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result **= num
    return result


# Main Program

while True:
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Error: Invalid choice. Please select a number from 1 to 7.")
        continue

    count = int(input("How many numbers do you want to enter? "))

    if count < 2:
        print("Error: Enter at least two numbers.")
        continue

    numbers = []
    for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    if choice == "1":
        result = add(numbers)
        print("Result =", result)

    elif choice == "2":
        result = subtract(numbers)
        print("Result =", result)

    elif choice == "3":
        result = multiply(numbers)
        print("Result =", result)

    elif choice == "4":
        result = divide(numbers)

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print("Result =", result)

    elif choice == "5":
        result = modulus(numbers)

        if result is None:
            print("Error: Cannot perform modulus by zero.")
        else:
            print("Result =", result)

    elif choice == "6":
        result = exponentiate(numbers)
        print("Result =", result)