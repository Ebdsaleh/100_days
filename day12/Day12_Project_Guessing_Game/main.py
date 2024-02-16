# main.py
# Day 12 Project - Guessing Game
"""
In this program the user will pick difficulty level between 'easy' and 'hard'.
'easy' will give the user 10 guesses, 'hard' will give the user 10 guesses.
The computer will pick a number between 1 and 100.
The user will input their guess and it will be compared against the number
chosen by the computer.
The progam will inform the user if their guess was 'too high' or 'too low'.
The remaining guesses will be subtracted each time the player makes a guess.

"""

import os
import sys
import random


EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def clear_screen():
    OS = sys.platform
    if OS.startswith('linux') or OS == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def check_answer(guess, answer):
    if guess > answer:
        print("Too High.")
        return False
    elif guess < answer:
        print("Too Low.")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_DIFFICULTY
    elif difficulty == 'hard':
        return HARD_DIFFICULTY


# Program start
def game():
    clear_screen()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    attempts = set_difficulty()
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if check_answer(guess, answer):
            break
        else:
            print("Guess again.")
            attempts -= 1
    if attempts == 0:
        print("You used up all your guesses, you lose.")


def main():
    game()


if __name__ == '__main__':
    main()
