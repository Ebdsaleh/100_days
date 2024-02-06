# main.py
# Day 03 Project - Treasure Island
import os
import sys


def clear_screen():
    platform = sys.platform
    if platform == "win32" or platform == "cygwin":
        os.system('cls')
    elif platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    else:
        return


clear_screen()
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
ch1 = input("Will you go left or right? ")
if ch1 == 'right':
    print("You fall into a hole and die")
    exit()
elif ch1 == "left":
    print("You come to the shore and see a boat approaching" +
          " from the distance...")
    ch2 = input("Will you swim or wait?")
    if ch2 == "swim":
        print("You jump in the water and swim toward the boat," +
              " you are attacked by a shark and die.")
        exit()
    elif ch2 == "wait":
        print("You wait for the boat and it takes you to an island.")
        print("You come across a building with three doors, one red, " +
              "one blue and one ")
        ch3 = input("Which door will you choose, red or blue?")
        if ch3 == "red":
            print("You set off a trap and are incinerated by fire.")
            print("You are dead.")
            exit()
        elif ch3 == "blue":
            print("A bear mauls you to death.")
            exit()
        elif ch3 == "green":
            print("You have found the treasure, congratulations!")
            exit()
