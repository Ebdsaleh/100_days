# main.py
"""
    This program takes two inputs the first variable is called a
    and the second variable called b.
    Write a program that switches the values stored in the variables a and b.
"""

a = input()
b = input()
# Don't change the code above.
#################################
# Write your program here.
temp = a
a = b
b = temp


# Write your code above this line.
print("a: " + a)
print("b: " + b)
