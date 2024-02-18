# main.py
# ###########DEBUGGING#####################
"""
I have left the bugs in the code and provided the solutions in the comments.
"""

# Describe Problem
# def my_function():
#    for i in range(1, 20):
#       if i == 20:
#            print("You got it")


# my_function()
"""
i is incremented starts at 1 and is incremented each iteration of the loop.
# BUG:
    i never reaches 20 because the range() function isn't inclusive of the
    upper limit. meaning that i will only go from 1 to 19.
# Solution:
    To fix the bug, add 1 to the upper limit of the range() but either changing
    it to 21 or range(1, 20 + 1).
    This will allow i to reach the value of 20 and meet the 'if' condition,
    which will print 'You got it'.
IndentationError: expected an indented block after 'if' statement on line 84
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
"""

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
"""
# Bug:
    The will sometimes produce and 'index out of range' exception error because
    the randint method is choosing between 1 and 6 but the dice_imgs list
    only has an idex value of 5 eventhough there are 6 elements.
    Indexing in Python begins at 0, not 1.
# Reproducing The Error:
    We can reproduce this error by trying to access the 6th index of the list.
    There are Two ways we can go about this:
        1. Change the dice_num value to 6. dice_num = 6
        2. Change the print statement to print(dice_imgs[6])
    This will cause the exception to trigger every time.
# Solution
    To fix the bug we need to change the range of the randint() method call.
    from 1, 6 to 0, 5. This will allow any element inside the dice_imgs list
    to be accessed and will execute the print() statement whithout error.

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
"""

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#    print("You are a millenial.")
# elif year > 1994:
#    print("You are a Gen Z.")
"""
# Bug:
    There are 2 errors in the code, the first (which I will ignore) is that
    Gen Z starts at 1997. The second (which I will fix) is:
    If the user enters 1994 neither print() statement is executed.
# Solution:
    To fix the code, change the 'elif' condition form '>' to '>=' so
    that the year 1994 is included in the condition.

year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")
"""

# Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
"""
# Bug:
    There are 3 bugs in the code:
        1. The print() statement is not indented which means the
        'if' condition is missing a following execution statement.
        This error will actually break the execution of our code.
        Due to an 'Indentation Error' this is the output I received when trying
        to run the code.
"IndentationError: expected an indented block after 'if' statement on line 84"
        2. The input() statement is going to assign the 'age' variable to
        a string which will cause a 'Type Error' when the 'if' statement is
        evaluated, because you cannot do numerical value comparisons with a
        string and a number.
        This kind of bug can be tricky to catch sometimes because the code
        will still run until that 'if' statement is evaluated.
        So be diligent.
        3. The print() statment needs to be an 'f string' to be able to use
        the age variable. f"{age}".
# Solution:
    To fix the code, indent the print() statement which will allow the code to
    execute. Then cast the input() statement as an 'int' or 'float'.
    (must be a number type) This will allow the 'if' statement to be evaluated
    and perform the comparison against to numerical values.
    Finally, make the string and 'f string' to print out the value of age.

age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
"""

# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
"""
# Bug:
    The 'total_words' variable is assigned to 0 because 'word_per_page' is
    never reassigned. An Equality operator '==' is being used instead of an
    assignment operator '='. This is causing 'pages' to be multiplied by 0
    each time the program is run, regardless of the integer value inputted by
    the user.
# Solution:
    To fix the code, change the equality operator '==' to an assignment
    operator '='. This will allow the 'total_words' variable to
    change in value.

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
"""

# Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
"""
Intended behaviour:
    The mutate function is meant to take in a_list and then create
    b_list then multiply each item of a_list by 2 and append the result
    to b_list. Finally print out b_list.

Bug:
    Only the last element in a_list is being mutated.
    This is due to an indentation issue, the line 'b_list.append(new_item)'
    is outdented from the 'for' loop, so only the last element is appended to
    b_list.
Solution:
    To fix the code, indent the 'b_list.append()' line to be inside of the
    'for' loop so that all the mutated items in a_list are added to b_list
    and will print out the mutated list as expected.

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
"""
