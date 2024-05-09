from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }


def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    restart = True
    while restart == True:

        for operation in operations:
            print(operation)
        choice = input("What kind of operation would ya like to use? ")
        num2 = float(input("What is the next number? "))

        calculation = operations[choice]
        answer = calculation(num1, num2)

        print(f"{num1} {choice} {num2} = {answer}")

        choice_restart = input(
            "Type 'y' to keep calculating with the previous result or type 'n' to exit, type restart to, well you know: ")
        if choice_restart == 'n':
            restart = False
            print("Goodbye!")
        elif choice_restart == 'y':
            num1 = answer

        elif choice_restart == 'restart':
            calculator()


calculator()