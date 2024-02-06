# main.py
# Day 04 exercise 15 - Treasure map
"""
You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is
what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this
line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists
to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Now it looks a bit more like the coordinates of a real map:
Your job is to write a program that allows you to mark a
square on the map using a letter-number system.

So an input of A3 should place an X at the position shown below:
    A     B     C
1 ['⬜️', '⬜️', '⬜️']

2 ['⬜️', '⬜️', '⬜️']

3 ['X', '⬜️', '⬜️']

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X".
Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

Example Input 1

B3

Example Output 1

Hiding your treasure! X marks the spot.
['⬜️', '⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']


"""

line1 = ['⬜️', '⬜️', '⬜️']
line2 = ['⬜️', '⬜️', '⬜️']
line3 = ['⬜️', '⬜️', '⬜️']
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position[0] == "A":
    if position[1] == "1":
        line1[0] = 'X'
    elif position[1] == "2":
        line2[0] = 'X'
    else:
        line3[0] = 'X'

elif position[0] == "B":
    if position[1] == "1":
        line1[1] = 'X'
    elif position[1] == "2":
        line2[1] = 'X'
    else:
        line3[1] = 'X'

elif position[0] == "C":
    if position[1] == "1":
        line1[2] = 'X'
    elif position[1] == "2":
        line2[2] = 'X'
    else:
        line3[2] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

"""
This will give the exact same result.
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

"""
