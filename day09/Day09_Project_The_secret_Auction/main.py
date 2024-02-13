# main.py
# Day 09 Project - The Secret Auction.

import sys
import os
import art

"""
The Secrect Auction Program.
This program take inputs from the user...
Name and bidding amount. The user with the highest bid wins.
Note: We are not checking for bids that are tied, the first user to enter the
highest bid wins.

"""
logo = art.logo
bidders = []


def clear_screen():
    OS = sys.platform
    if OS.startswith('linux') or OS == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def welcome():
    clear_screen()
    print(f"{logo}")
    print("Welcome to the secret auction program.")


def bid():
    name = input("What is your name? :")
    amount = int(input("What is your bid?: $"))
    bidder = {
            "name": name,
            "amount": amount,
              }
    bidders.append(bidder)


def calculate_bids():
    max_bid = 0
    name = ""
    for bid in bidders:

        if bid["amount"] > max_bid:
            max_bid = bid["amount"]
            name = bid["name"]

    print(f"The Winner is {name} with a bid of ${max_bid}")


def are_there_more_bids():
    more = False
    while True:
        clear_screen()
        more_bidders = input(
                "Are there anymore bidders? Type 'yes' or 'no'. ").lower()
        if more_bidders[0] == "y":
            more = True
            break
        elif more_bidders[0] == "n":
            more = False
            break
        else:
            print("Invalid input.")
            continue
    return more


while True:
    welcome()
    bid()
    if are_there_more_bids():
        continue
    else:
        break
print(f"{logo}")
calculate_bids()
