"""
Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
"""


class Calculator:
    def __init__(self):
        operators = ["add", "subtract", "multiply", "divide"]
        while True:
            operator = input("Enter the operator (add, subtract, multiply, divide): ").strip().lower()
            if operator in operators:
                break
            else:
                print("Invalid operator, Please enter one of: add, subtract, multiply, divide")

        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input, Please enter a valid number.")

        while True:
            try:
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input, Please enter a valid number.")

        if operator == "divide" and num2 == 0:
            print("Cannot divide by zero")
            return

        if operator.lower() == "add":
            print(num1, "+", num2, "=", num1 + num2)
        elif operator.lower() == "subtract":
            print(num1, "-", num2, "=", num1 - num2)
        elif operator.lower() == "multiply":
            print(num1, "*", num2, "=", num1 * num2)
        elif operator.lower() == "divide":
            print(num1, "/", num2, "=", num1 / num2)


Calculator()
