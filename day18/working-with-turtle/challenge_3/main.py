# main.py
# Day 18 Challenge 3 - Drawing Different Shapes
"""
In this challenge we are going to be drawing the following shapes:
    Triangle, Square, Pentagon, Hexagon, Heptagon,
    Octogon, Nonagon and a Decagon.
Each shape will be drawn in a random colour and each side will be
100 in length.
divide 360 by the number of sides to get the angle of each shape.
"""
from turtle import Turtle, Screen
import random
from time import time

SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
# define turtle colours and max colour range.
COLOR_RANGE: int = 255
turtle_colors = [
        "red", "green", "blue", "yellow", "magenta", "black",
        "cyan", "orange", "pink", "chocolate"
        ]


# def functions for random selection.
def pick_random_number(limit: int):
    random.seed(time())
    number = random.randint(0, limit)
    return number


def pick_random_pen_color(t: Turtle):
    random.seed(time())
    r_value = pick_random_number(COLOR_RANGE)
    g_value = pick_random_number(COLOR_RANGE)
    b_value = pick_random_number(COLOR_RANGE)
    t.pencolor(r_value, g_value, b_value)


def pick_random_turtle_color(t: Turtle):
    random.seed(time())
    index = pick_random_number(len(turtle_colors) - 1)
    new_color = turtle_colors[index]
    t.color(new_color)


def pick_random_background_color(screen: Screen):
    random.seed(time())
    r_value = pick_random_number(COLOR_RANGE)
    g_value = pick_random_number(COLOR_RANGE)
    b_value = pick_random_number(COLOR_RANGE)
    screen.bgcolor(r_value, g_value, b_value)


# draw the shapes
def draw_shape(t: Turtle, sides: int, length: int, angle: float):
    for _ in range(sides):
        t.forward(length)
        t.right(angle)


def find_angle(sides: int):
    max_degrees = float(360)
    angle = max_degrees / sides
    return angle


def draw_triangle(t: Turtle, length: int):
    sides = 3
    angle = find_angle(sides)
    pick_random_pen_color(t)
    draw_shape(t, sides, length, angle)


def draw_square(t: Turtle, length):
    pick_random_pen_color(t)
    sides = 4
    angle = find_angle(sides)
    draw_shape(t, sides, length, angle)


def draw_pentagon(t: Turtle, length: int):
    pick_random_pen_color(t)
    sides = 5
    angle = find_angle(sides)
    draw_shape(t, sides, length, angle)


def draw_hexagon(t: Turtle, length: int):
    pick_random_pen_color(t)
    sides = 6
    angle = find_angle(sides)
    draw_shape(t, sides, length, angle)


def draw_heptagon(t: Turtle, length: int):
    pick_random_pen_color(t)
    sides = 7
    angle = find_angle(sides)
    draw_shape(t, sides, length, angle)


def draw_octogon(t: Turtle, length: int):
    pick_random_pen_color(t)
    sides = 8
    angle = find_angle(sides)
    draw_shape(t, sides, length, angle)


def draw_nonagon(t: Turtle, length: int):
    pick_random_pen_color(t)
    sides = 9
    angle = find_angle(sides)
    draw_shape(t, sides, length, angle)


def draw_decagon(t: Turtle, length: int):
    pick_random_pen_color(t)
    sides = 10
    angle = find_angle(sides)
    draw_shape(t, sides, length, angle)


def draw_shapes(t: Turtle, length: int):
    draw_triangle(t, length)
    draw_square(t, length)
    draw_pentagon(t, length)
    draw_hexagon(t, length)
    draw_heptagon(t, length)
    draw_octogon(t, length)
    draw_nonagon(t, length)
    draw_decagon(t, length)


def main():
    t: Turtle = Turtle()
    t.shape("turtle")
    t.pensize(5)
    screen: Screen = Screen()
    # set color mode to RGB
    screen.colormode(COLOR_RANGE)
    screen.screensize(SCREEN_HEIGHT, SCREEN_WIDTH)
    pick_random_turtle_color(t)
    length: int = 100
    pick_random_background_color(screen)
    draw_shapes(t, length)
    # handle program exit
    screen.exitonclick()


if __name__ == '__main__':
    main()
