# main.py
# Day 13 exercise - Debugging Odd or Even
"""
    Read this the code in main.py
    Spot the problems 🐞.
    Modify the code to fix the program.

Fix the code so that it works and passes the tests when you submit.
# ######################## Buggy Code #########################
number = int(input()) # Which number do you want to check?

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
"""
# ####################### Fixed Code ###########################
number = int(input("Which number do you want to check?: "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

"""
# Bug:
    The 'if' statement has an assignment operator '=' instead of an
    equality operator '==' causing the program to crash, resulting in a
    'Sytax Error'
# Solution:
    To fix the code, change the assignemnt operator to and equality comparison
    operator.

"""
