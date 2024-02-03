# main.py
# Day 02 Exercise 5 - Datatypes
# This program takes a two digit number and sums them together.
print("Enter a two digit number:")
two_digit_number = input()
# Don't change the code above...
# ###################################
# Write your code below.
if len(two_digit_number) == 2:
    a = int(two_digit_number[0])
    b = int(two_digit_number[1])
    sum = a + b
    print(sum)
else:
    print("You must enter and two digit number.")
