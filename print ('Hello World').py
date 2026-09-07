again = "yes"

while again == "yes":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = float(num1)
    num2 = float(num2)

    operation = input("Enter an operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation"

    print(f"Result: {result}")

    again = input("Do you want to calculate again? (yes/no): ")
