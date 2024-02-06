# main.py
# Day 04 Project - Rock Paper Scissors
from random import randint
import os
import sys


def clear_screen():
    OS = sys.platform
    if OS == "linux" or OS == "darwin":
        os.system('clear')
    else:
        os.system('cls')


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line

choice = [rock, paper, scissors]
score = 0
ai_score = 0
ai_visual = ""

while True:
    clear_screen()
    player_choice = input("Choose (r)ock, (p)aper or (s)cissors: ").lower()
    ch_ai = ""
    ai_choice = randint(0, len(choice) - 1)
    if ai_choice == 0:
        ch_ai = "r"
        ai_visual = choice[0]
    elif ai_choice == 1:
        ch_ai = "p"
        ai_visual = choice[1]
    else:
        ch_ai = "s"
        ai_visual = choice[2]

    if player_choice == "r":
        print(f"You played rock...\n{rock}")

    elif player_choice == "p":
        print(f"You played paper...\n{paper}")

    elif player_choice == "s":
        print(f"You played paper...\n{scissors}")

    else:
        print("invalid option!")
        continue

    print(f"AI played:\n{ai_visual}")
    if ch_ai == player_choice:
        print("Tie!")

    if player_choice == "r":
        if ch_ai == "s":
            print("You gain a point.")
            score += 1
        elif ch_ai == "p":
            print("AI gains a point.")
            ai_score += 1

    if player_choice == "p":
        if ch_ai == "r":
            print("You gain a point.")
            score += 1
        if ch_ai == "s":
            print("AI gains a point.")
            ai_score += 1

    if player_choice == "s":
        if ch_ai == "r":
            print("AI gains a point.")
            ai_score += 1
        elif ch_ai == "p":
            print("You gain a point.")
            score += 1

    print(f"You: {score} AI: {ai_score}")
    input("Press Enter to continue. ")
    if score == 3:
        print("You Win!")
        break
    elif ai_score == 3:
        print("You Lose!")
        break
exit()
