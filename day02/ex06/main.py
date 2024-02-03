# main.py
# Day 02 Exercise 06 - BMI Calculator
"""
    This program takes the weight and height input from the user and
    calculates then outputs their BMI.
"""
print("Enter your height in meters e.g: 1.65")
height = input()
print("Enter your weight in kilograms e.g: 72")
weight = input()
# Don't change the code above:
# #####################################
# Write your code below.
weight = float(weight)
height = float(height)
bmi = weight / (height * height)
print(round(bmi))
