# main.py
# Day 03  exercise 11 - Pizza Order Practice.
"""
    Congratulations, you've got a job at Python Pizza!
    Your first job is to build an automatic pizza order program.

    Based on a user's order, work out their final bill.

    Small pizza (S): $15

    Medium pizza (M): $20

    Large pizza (L): $25

    Add pepperoni for small pizza (Y or N): +$2

    Add pepperoni for medium or large pizza (Y or N): +$3

    Add extra cheese for any size pizza (Y or N): +$1
"""
print("Thank you for choosing Python Pizza Deliveries:")
print("What size pizza do you want? S, M, or L")
size = input()
print("Do you want pepperoni? Y or N")
add_pepperoni = input()
print("Do you want extra cheese? Y or N")
extra_cheese = input()
# Don't change the code above.
# #######################################################
# Write your code below.
total = 0
if size == 'S':
    total += 15
elif size == 'M':
    total += 20
elif size == 'L':
    total += 25
# Ignore incorrect input
# Not going to implement input validation in this exercise.
if add_pepperoni == 'Y':
    if size == 'S':
        total += 2
    else:
        total += 3
elif add_pepperoni == 'N':
    pass

if extra_cheese == 'Y':
    total += 1
elif extra_cheese == 'N':
    pass

print(f"Your final bill is: ${total}.")
