# main.py
# Day 13 exercise 27 - Debugging FizzBuzz

"""

    Read this the code in main.py
    Spot the problems 🐞.
    Modify the code to fix the program.
    No shortcuts - don't copy-paste to replace the code entirely with
    a working solution.

The code needs to print the solution to the FizzBuzz game.

Your program should print each number from 1 to x where x is the input number.

However when the number is divisible by 3 then instead of printing the
number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number
it should print "Buzz".

And if the number is divisible by both 3 and 5 e.g. 15 then instead of
the number it should print "FizzBuzz".

# ###################################### Buggy Code ###########################

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
"""
# #################################### Fixed Code ##########################

target = int(input())
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

"""
# Bug:
    This code has 3 bugs in it.
    1. The FizzBuzz is being printed every time a number divisible by 3 or 5
        is reached.
    2. Every number is being outputted including the Fizz, Buzz and FizzBuzz
        numbers.
    3. The ouput of the numbers are decorated by [] e.g '[3]'
# Solution:
    1. Change the 'or' keyword to 'and' in the first 'if' statement.
    2. Change the second and third 'if' statements to 'elif' statements.
        This will ensure that the number will be replaced by the
        appropiate word 'Fizz', 'Buzz', or 'FizzBuzz'.
    3. Remove the square brackets '[]' from the print statement in the
        'else' clause e.g  print(number)
"""
