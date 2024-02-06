# main.py
# Day 03 exercise 12 - Love Calculator

"""
    You are going to write a program that tests the compatibility between
    two people. To work out the love score between two people:

    Take both people's names and check for the number of times
    the letters in the word TRUE occurs.

    Then check for the number of times the letters in the word LOVE occurs.

    Then combine these numbers to make a 2 digit number.

    For Love Scores less than 10 or greater than 90, the message should be:

    "Your score is *x*, you go together like coke and mentos."

    For Love Scores between 40 and 50, the message should be:

    "Your score is *y*, you are alright together."

    Otherwise, the message will just be their score. e.g.:

    "Your score is *z*."
    e.g.

    name1 = "Angela Yu"
    name2 = "Jack Bauer"

    T occurs 0 times

    R occurs 1 time

    U occurs 2 times

    E occurs 2 times

    Total = 5

    L occurs 1 time

    O occurs 0 times

    V occurs 0 times

    E occurs 2 times

    Total = 3

    Love Score = 53

    Print: "Your score is 53."
"""

# print("The Love Calculator is calculating your score...")

name1 = input("What is your name? ")
name2 = input("What is their name? ")
# Don't change the code above
# ##############################################
# Write your code below this line
names = name1 + name2
lowered_names = names.lower()


# This is one method to achieve the same result
def non_loop(names):
    t = names.count("t")
    r = names.count("r")
    u = names.count("u")
    e = names.count("e")
    first_digit = t + r + u + e

    l = names.count("l")
    o = names.count("o")
    v = names.count("v")
    e = names.count("e")
    second_digit = l + o + v + e

    score = str(first_digit) + str(second_digit)
    return int(score)


def check_names(names):
    count1 = 0
    count2 = 0
    check1 = "true"
    check2 = "love"
    for char in names:
        if char in check1:
            count1 += 1
        if char in check2:
            count2 += 1
    score = f"{count1}{count2}"
    return int(score)


def process_score(score):
    print("The Love Calculator is calculating your score...")
    message = ""
    if score < 10 or score > 90:
        message = ", you go together like coke and mentos."
    elif score >= 40 and score <= 50:
        message = ", you are alright together."
    else:
        message = "."
    print(f"your score is {score}{message}")


score = check_names(lowered_names)
process_score(score)
