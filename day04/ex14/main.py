# main.py
# Day 04 - exercise 14 - Banker Roulette
from random import randint

"""
You are going to write a program that will select a random name from
a list of names. The person selected will have to pay for
everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 1 splits the string names_string into individual names
and puts them inside a List called names. For this to work,
you must enter all the names as names followed by comma then space.
e.g. name, name, name

HINT: Assume that names looks like this:
input: x, y, z, names = ["x", "y", "z"]

Example Output:
Michael is going to buy the meal today!
"""


names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# Don't change the code above
r_sel = randint(0, len(names) - 1)
print(f"{names[r_sel]} is going to buy the meal today!")
