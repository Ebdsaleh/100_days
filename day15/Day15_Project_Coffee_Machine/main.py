# main.py
# Day 15 Project - Coffee Machine
"""
Coffee Machine:
    This programs simulates a basic coffee machine, the user will enter
    the name of the drink to order.
    The machine will check if the resources are sufficient before asking
    for payment.
    If the there are insufficient resources the user will be notified.
    If the payment received is insufficient, the money will be refunded
    to the user.
    Type 'report' to bring up the resources.
    Type 'quit' to exit the program.
    notes: This is a very minimal implimentation.


"""
import os
import sys
OS = sys.platform

MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
            },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
                },
            "cost": 2.5,
            },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
                },
            "cost": 3.0,
            }
        }

resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        }

coins = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
        }

money = 0


def clear_screen():
    if OS.startswith('linux') or OS == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def print_report():
    clear_screen()
    print(f"Water: {resources['water']}ml remaining.")
    print(f"Milk: {resources['milk']}ml remaining.")
    print(f"Coffee: {resources['coffee']}g remaining.")
    print(f"Money: ${money:.2f}")


def can_make_drink(drink):
    """
    Returns True or False depending on the resources available.
    """
    has_enough_resources = True
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients.get(item):
            print(f"Sorry there is not enough {item}.")
            has_enough_resources = False
    return has_enough_resources


def make_drink(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        deduct_from_resources = ingredients.get(item)
        resources[item] -= deduct_from_resources
    print(f"Done, enjoy your {drink}.")


def process_coins():
    amount_processed = 0
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    amount_processed += coins["quarter"] * quarters
    amount_processed += coins["dime"] * dimes
    amount_processed += coins["nickel"] * nickels
    amount_processed += coins["penny"] * pennies
    return amount_processed


def make_payment(drink):
    global money
    payment_received = 0
    cost = MENU[drink]["cost"]
    payment_received = process_coins()
    if payment_received >= cost:
        change = payment_received - cost
        print(f"Here is ${change:.2f} in change.")
        money += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def main():
    clear_screen()
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino):")
        if user_input == 'report':
            print_report()
        elif user_input == 'espresso':
            if can_make_drink(user_input):
                if make_payment(user_input):
                    make_drink(user_input)
        elif user_input == 'latte':
            if can_make_drink(user_input):
                if make_payment(user_input):
                    make_drink(user_input)
        elif user_input == 'cappuccino':
            if can_make_drink(user_input):
                if make_payment(user_input):
                    make_drink(user_input)
        elif user_input == 'quit':
            break
    exit()


if __name__ == '__main__':
    main()
