# main.py
# Day 10 Project - Calculator
import art
import os
import sys

"""
This is a simple calculator program which takes input from the user.
input the number, then the operator then another number and will
output the answer, then prompt the user if they would like to continue
calculating with the current answer. If 'yes', then the user will select
another operator and then another number to calculate again.
If 'no', then the program will restart.
"""

logo = art.logo


def clear_screen():
    OS = sys.platform
    if OS.startswith('linux') or OS == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def show_operations():
    for symbol in operations:
        print(symbol)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
        }


def ask_to_continue(num):
    valid_input = False
    while not valid_input:
        ask = input(f"Type 'y' to continue calculating with {num}," +
                    " type 'n' to start a new calculation or type 'q'" +
                    " to quit: ")
        if ask[0] == 'y':
            valid_input = True
            return True
        elif ask[0] == 'n':
            valid_input = True
            return False
        elif ask[0] == 'q':
            valid_input = True
            clear_screen()
            print(f"{logo}")
            print("Goodbye.")
            exit()
        else:
            print("Invalid input.")
            valid_input = False


def calculator():
    clear_screen()
    print(f"{logo}")
    num_1 = float(input("What's the first number: "))
    show_operations()
    should_continue = True
    while should_continue:
        operator = input("Pick an operation: ")
        num_2 = float(input("What's the next number: "))
        calculation_function = operations[operator]
        answer = calculation_function(num_1, num_2)
        print(f"{num_1} {operator} {num_2} = {answer}")
        if ask_to_continue(answer):
            num_1 = answer
        else:
            should_continue = False
            calculator()


# program
def main():
    calculator()


if __name__ == '__main__':
    main()
