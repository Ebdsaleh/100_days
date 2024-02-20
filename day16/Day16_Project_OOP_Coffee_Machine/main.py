from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
import sys


def clear_screen():
    OS = sys.platform
    if OS.startswith('linux') or OS.startswith('darwin'):
        os.system('clear')
    else:
        os.system('cls')


def main():
    clear_screen()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    drinks = menu.get_items()
    power_on = True
    while power_on:
        user_input = input(f"What would you like? {drinks}: ")
        if user_input == "report":
            coffee_machine.report()
            money_machine.report()
        elif user_input == "quit":
            power_on = False
        else:
            drink = menu.find_drink(user_input)
            if (coffee_machine.is_resource_sufficient(drink) and
               money_machine.make_payment(drink.cost)):
                coffee_machine.make_coffee(drink)

    exit()


if __name__ == '__main__':
    main()
