# main.py
"""
Using the Turtle Graphics API:
    make the turtle move 100 paces.
"""
from turtle import Turtle, Screen
turtle_chad = Turtle()
turtle_chad.shape("turtle")
turtle_chad.color("green")
screen = Screen()
max_paces = 101
pace = 1
for i in range(0, max_paces):
    turtle_chad.forward(pace)
screen.exitonclick()
