# main.py
# Day 02 Project - Tip Calculator
"""
    This program will take the input of bill amount and the amount of people
    to split it by. Then the percentage amount you want to tip.
    Example:
        if the bill was $150.00, split between 5 people, with a 12% tip.
        each person should pay (150.00 / 5) * 1.12
"""

print("Welcome to the Tip Calculator.")
bill_total = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give 10, 12, 15? "))
people = float(input("How people to split the bill? "))
tip_percentage = 1 + (tip_percentage / 100)
tip_per_person = (bill_total / people) * tip_percentage

print(f"Each person should pay: ${tip_per_person:.2f}")
