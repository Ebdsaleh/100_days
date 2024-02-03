# main.py

"""
Band name generator:
    This is a simple program that takes two inputs from the user and
    generates a band name with them.
"""

print("Welcome to the Band Name Generator.")
word_1 = input("What is the name of the city you grew up in?\n")
word_2 = input("What is the name of your favourite pet?\n")
band_name = f"{word_1} {word_2}"
print(f"Your band name could be {band_name}")
