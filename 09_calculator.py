# write a simple python program that works as a calculator
# the program should ask the user to enter two numbers and an operator
# the program should print the result of the operation
# the program should ask the user if he/she wants to continue

import os

def main():

    # clear the screen
    os.system("cls")

    # step 1: ask the user to enter two numbers and an operator
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    # ask the user to enter an operator from the following list: +, -, *, /
    operator = input("Enter an operator from the following list: +, -, *, /: ")

    # step 2: perform the operation
    # create functions to perform the operations
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2

    # create a dictionary to store the functions
    operations = { "+": add, "-": subtract, "*": multiply, "/": divide }

    # call the function
    result = operations[operator](num1, num2)

    # step 3: print the result
    print(f"The result is: {result}")

    # step 4: ask the user if he/she wants to continue
    response = input("Do you want to continue? (y/n) ").lower()
    if response == "y":
        main()
    else:
        print("Goodbye!")

# call the main function
if __name__ == "__main__":

    main()


