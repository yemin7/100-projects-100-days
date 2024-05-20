import os


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    end_it = False
    # continue_num = False
    number1 = float(input("Enter first number: "))

    while not end_it:
        # total = 0.0
        # if not continue_num:
        print("+\n-\n*\n/")
        operator = input("Pick an operation: ")
        number2 = float(input("Enter second number:"))

        cal_function = operations[operator]
        print(type(cal_function))
        total = cal_function(number1, number2)

        # if operator == "+":
        #     total = add(number1, number2)
        # elif operator == "-":
        #     total = subtract(number1, number2)
        # elif operator == "*":
        #     total = multiply(number1, number2)
        # elif operator == "/":
        #     total = divide(number1, number2)

        print(f"{number1} {operator} {number2} = {total}")

        result = input(f"Type 'y' to continue calculating with {total} or 'n' to start a new calculation"
                       " or 'e' to exit: ")
        if result == 'y':
            number1 = total
        elif result == 'n':
            os.system('clear')
            calculator()
        else:
            # end_it = True
            exit()


calculator()
