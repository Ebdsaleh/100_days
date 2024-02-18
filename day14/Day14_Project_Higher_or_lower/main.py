# main.py
# Day 14 Project - Higher or lower
import random
import art
import game_data
import os
import sys


def clear_screen():
    OS = sys.platform
    if OS.startswith('linux') or OS == 'darwin':
        os.system('clear')
    else:
        os.system('cls')


def select_option(_data):
    option = random.randint(0, len(_data) - 1)
    return _data[option]


def check_for_duplicates(opt_a, opt_b):
    if opt_a == opt_b:
        return True
    else:
        return False


def check_answer(choice, opt_a, opt_b, most_followers):
    if choice[0] == 'A':
        # check the data
        if compare(opt_a, opt_b):
            most_followers.append(opt_a)
            return True
        else:
            return False
    elif choice[0] == 'B':
        if not compare(opt_a, opt_b):
            most_followers.append(opt_b)
            return True
        else:
            return False


def compare(opt_a, opt_b):
    """
        returns True if a is higher and b
    """
    if opt_a["follower_count"] > opt_b["follower_count"]:
        return True
    else:
        return False


def form_question(option):
    question = str(
            f"{option['name']}, a {option['description']}" +
            f" from {option['country']}."
            )
    return question


# Game loop
def game():
    data = game_data.data
    logo = art.logo
    vs = art.vs
    game_end = False
    score = 0
    most_followers = []
    opt_a = {}
    opt_b = {}
    while not game_end:
        clear_screen()
        if most_followers == []:
            opt_a = select_option(data)
        else:
            opt_a = most_followers[-1]
        opt_b = select_option(data)
        if check_for_duplicates(opt_a, opt_b):
            continue

        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {form_question(opt_a)}")
        print(vs)
        print(f"Against B: {form_question(opt_b)}")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        # check input
        if not check_answer(choice, opt_a, opt_b, most_followers):

            game_end = True
        else:
            score += 1
    print(f"Sorry, that's wrong. Final score: {score}")


def main():
    game()


if __name__ == '__main__':
    main()
