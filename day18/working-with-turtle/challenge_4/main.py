# main.py
# Day 18 challenge - Turtle Graphics Random Walk
"""
In this challenge we are going to create a program that will make our turtle
walk in a randomized pattern.
"""
from turtle import Turtle, Screen
import random
from time import time
COLOR_RANGE = 255
DISTANCE = 20
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
direction_list = ["north", "south", "east", "west"]


def pick_random_number(num: int):
    random.seed(time())
    r_num: int = random.randint(0, num)
    return r_num


def pick_random_color(t: Turtle):
    r_value: int = pick_random_number(COLOR_RANGE)
    g_value: int = pick_random_number(COLOR_RANGE)
    b_value: int = pick_random_number(COLOR_RANGE)
    color: tuple = (r_value, g_value, b_value)
    t.pencolor(color)


def go_north(t: Turtle, distance: int):
    t.setheading(90)
    t.forward(distance)


def go_south(t: Turtle, distance: int):
    t.setheading(270)
    t.forward(distance)


def go_east(t: Turtle, distance: int):
    t.setheading(0)
    t.forward(distance)


def go_west(t: Turtle, distance: int):
    t.setheading(180)
    t.forward(distance)


def move(t: Turtle, direction):
    if direction == "north":
        go_north(t, DISTANCE)
    elif direction == "south":
        go_south(t, DISTANCE)
    elif direction == "east":
        go_east(t, DISTANCE)
    elif direction == "west":
        go_west(t, DISTANCE)
    return direction


def main():
    screen: Screen = Screen()
    screen.colormode(COLOR_RANGE)
    screen.screensize(canvwidth=SCREEN_WIDTH, canvheight=SCREEN_HEIGHT)
    t: Turtle = Turtle()
    t.shape("turtle")
    t.pensize(15)
    t.speed('fastest')
    moves = 1000
    steps = 0
    while steps < moves:
        pick_random_color(t)
        direction = random.choice(direction_list)
        move(t, direction)
        steps += 1

    screen.exitonclick()


if __name__ == '__main__':
    main()
