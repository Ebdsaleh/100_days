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
player_code = 0


while True:
    clear_screen()
    player_choice = input("Choose (r)ock, (p)aper or (s)cissors: ").lower()
    ai_choice = randint(0, len(choice) - 1)
    ai_visual = choice[ai_choice]

    if player_choice == "r":
        print(f"You played rock...\n{rock}")
        player_code = 0
    elif player_choice == "p":
        print(f"You played paper...\n{paper}")
        player_code = 1
    elif player_choice == "s":
        print(f"You played paper...\n{scissors}")
        player_code = 2
    else:
        print("invalid option!")
        continue
    print(f"AI:\n{ai_visual}")
    if player_code == 0 and ai_choice == 2:
        print("You gain a point.")
        score += 1
    elif ai_choice == 0 and player_code == 2:
        print("AI gains a point.")
        ai_score += 1
    elif ai_choice > player_code:
        print("AI gains a point.")
        ai_score += 1
    elif player_code > ai_choice:
        print("You gain a point.")
        score += 1
    elif ai_choice == player_code:
        print("Tie.")

    print(f"You: {score} AI: {ai_score}")
    input("Press Enter to continue. ")
    if score == 3:
        print("You Win!")
        break
    elif ai_score == 3:
        print("You Lose!")
        break
exit()
