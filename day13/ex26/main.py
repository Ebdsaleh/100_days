# main.py
# day 13 exercise 26 - Debugging Leap Year
"""

    Read this the code in main.py
    Spot the problems 🐞.
    Modify the code to fix the program.
    No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# ############################# Buggy Code ##############################

# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
"""

# ########################## Fixed Code #################################
year = int(input("Which Year do you want to check?: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


"""
# Bug:
    This code is assigning the 'year' variable as a string and trying to do
    numerical comparisons on it. This will cause a Type Error and the program
    will crash once the input has been submitted.
# Solution:
     To fix the code, cast the input() as an 'int' to allow the numerical
     comparisons.
"""
