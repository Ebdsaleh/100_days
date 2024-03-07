# main.py
# Day 18 challenge 5 - Draw a Spirograph
"""
In this challenge we are going to draw a spriograph using the Turtle Graphics
library.
The Turtle object will draw circles with a radius of 100 and 5 in distance
between each circle.
Each circle will have a randomly assigned colour.
"""

from turtle import Turtle, Screen
from time import time
from random import randint, seed

# constants
SCREEN_HEIGHT: int = 1080
SCREEN_WIDTH: int = 1920
DISTANCE: int = 5
COLOR_RANGE: int = 255
RADIUS:int = 100


def pick_random_number(num: int):
    seed(time())
    r_num = randint(0, num)
    return r_num


def pick_random_color(t: Turtle):
    seed(time())
    r_hue: int = pick_random_number(COLOR_RANGE)
    g_hue: int = pick_random_number(COLOR_RANGE)
    b_hue: int = pick_random_number(COLOR_RANGE)
    color: tuple = (r_hue, g_hue, b_hue)
    t.pencolor(color)


def draw_spirograph(t: Turtle, radius: int, distance):
    step: int = 0
    heading: int = 0
    steps: int = int(360 / distance)
    while step < steps:
        pick_random_color(t)
        t.circle(radius)
        t.setheading(heading)
        step += 1
        heading += DISTANCE


def main():
    screen: Screen = Screen()
    screen.screensize(canvheight=SCREEN_HEIGHT, canvwidth=SCREEN_WIDTH)
    screen.colormode(COLOR_RANGE)
    t: Turtle = Turtle()
    t.speed('fastest')
    draw_spirograph(t, RADIUS, DISTANCE)
    screen.exitonclick()


if __name__ == '__main__':
    main()
