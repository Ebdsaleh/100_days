# main.py
# Day 03 exercise 09 BMI 2.0
"""
    Write a program that interprets the Body Mass Index (BMI)
    based on a user's weight and height.

    It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Equal to or over 25 but below 30 they are slightly overweight
    Equal to or over 30 but below 35 they are obese
    Equal to or over 35 they are clinically obese.

"""
print("Enter your height in meters e.g., 1.55")
height = float(input())
print("Enter your weight in kilograms e.g, 72")
weight = int(input())
# Don't change the code above.
# ##################################
# Write your code below
bmi = weight / (height * height)
message = ""
if bmi < 18.5:
    message = "you are underweight."
elif bmi >= 18.5 and bmi < 25:
    message = "you have a normal weight."
elif bmi >= 25 and bmi < 30:
    message = "you are slightly overweight."
elif bmi >= 30 and bmi < 35:
    message = "you are obese."
else:
    message = "you are clinically obese."

print(f"Your BMI is {bmi}, {message}")
