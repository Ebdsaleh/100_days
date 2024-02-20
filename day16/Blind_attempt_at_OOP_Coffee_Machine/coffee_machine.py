# coffee_machine.py


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
    notes: This is my own OOP implementation. I did this as an attempt before
    I read the requirements at the end of the section.


"""

import os
import sys


class CoffeeMachine():
    def __init__(self):
        self.OS = sys.platform
        self.MENU = {
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
        self.resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
                }
        self.coins = {
                "penny": 0.01,
                "nickel": 0.05,
                "dime": 0.10,
                "quarter": 0.25,
                }
        self.money = 0

    def power_on(self):
        self.clear_screen()
        print("Welcome to the Coffee Machine 3000!")
        print("Checking available resources:")
        self.print_report()
        print("OK!")
        input("Machine ready for use. Press 'Enter' to continue")
        self.run()

    def clear_screen(self):
        if self.OS.startswith('linux') or self.OS.startswith('darwin'):
            os.system('clear')
        else:
            os.system('cls')

    def print_report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money:.2f}")

    def process_coins(self):
        amount_processed = 0
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        amount_processed += self.coins["quarter"] * quarters
        amount_processed += self.coins["dime"] * dimes
        amount_processed += self.coins["nickel"] * nickels
        amount_processed += self.coins["penny"] * pennies
        return amount_processed

    def process_payment(self, drink):
        payment_received = 0
        cost = self.MENU[drink]['cost']
        print(f"Please insert ${cost:.2f} in coins.")
        payment_received = self.process_coins()
        amount_received_text = str(f"Received: ${payment_received:.2f}, ")
        change_text = str()
        if payment_received >= cost:
            change = payment_received - cost
            self.money += cost
            if change > 0:
                change_text = str(
                        f"here is your ${change:.2f} change in coins.")
            else:
                change_text = str("No change given.")
            payment_accepted_text = str(
                    f"{amount_received_text}" +
                    f"{change_text}")
            print(f"{payment_accepted_text}")
            return True
        else:
            payment_declined_text = str(
                    f"Sorry, you inserted only: ${payment_received:.2f} " +
                    f"That's not enough money. ${cost:.2f} was required. " +
                    "Money refunded.")
            print(f"{payment_declined_text}")
            return False

    def can_make_drink(self, drink):
        has_enough_resources = True
        ingredients = self.MENU[drink]["ingredients"]
        for item in ingredients:
            if self.resources[item] < ingredients.get(item):
                has_enough_resources = False
                print(f"Sorry, there isn't enough {item}.")
        return has_enough_resources

    def make_drink(self, drink):
        print(f"Brewing your {drink}, please wait...")
        resource_cost = 0
        ingredients = self.MENU[drink]['ingredients']
        for item in ingredients:
            resource_cost = ingredients[item]
            self.resources[item] -= resource_cost
        print(f"Done, enjoy your {drink}.")

    def process_order(self, order):
        if order in self.MENU:
            print(f"Beginning transaction for {order}...")
            if self.can_make_drink(order):
                if self.process_payment(order):
                    self.make_drink(order)
        else:
            if order == "report":
                self.print_report()
            elif order == "quit":
                exit()
            else:
                print("Drink not available or invalid command.")

    def run(self):
        self.clear_screen()
        main_screen_text = str(
                "What would you like? " +
                "espresso/latte/cappuccino"
                )
        while True:
            user_input = input(f"{main_screen_text}: ").lower()
            self.process_order(user_input)
