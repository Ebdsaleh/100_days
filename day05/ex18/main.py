# main.py
# Day 05 exercise 18 - Adding Even numbers
"""
You are going to write a program that calculates the sum of all the
even numbers from 1 to X. If X is 100 then the first even number would
be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output.
It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers
from 0 to a max of 1000.
Example Input

10

Example Output

30

Hint

There are quite a few ways of solving this problem,
but you will need to use the range() function in any of the solutions.
"""
print("Enter a number between 0 and 1000")
target = int(input())  # Enter a number between 0 and 1000
# Do not change the code above.
# Write your code here
if target > 1000:
    print("The input limit is 1000")
    exit()

added_evens = 0

for n in range(1, target + 1):
    if n % 2 == 0:
        added_evens += n

print(f"{added_evens}")
