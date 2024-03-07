# main.py
# Day 18 Project - The Hirst Painting
"""
Day 18 Project - The Hirst Painting:
    This program is going to paint a bunch of dots on the screen in a similar
    fashion to a painting by artist Damien Hirst.
    Using the Turtle Graphics library and a package called 'Colorgram'.
    install with pip: ( pip install colorgram.py )
    Colorgram allows is a package that can extract colours from an image,
    which will be used to for the color palette.
    The painting will be 10 x 10 rows of dots
    extract the colors from the image
    removed the background color from the list of colors extracted.
    Each dot should be around 20 in size and 50 spaces apart
NOTE:
    I have commented out code that is no longer in use once the colours are
    extracted. The 'colors.py' file has the extracted colour values from the 
    'image.png' file used for creating the 'color_list' variable.
"""

from time import time
from turtle import Turtle, Screen
from random import seed, randint, choice
# import colorgram  #  No longer need, step completed.
import colors
# constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
COLOR_MODE = 255
ROWS = 10
SPACING = 50
DOTS = 10


"""
No longer required, step already done.
image_colors = colorgram.extract('image.png', 90)
"""
color_list = colors.rbg_colors


def pick_random_number(num_range: int):
    seed(time())
    r_num = randint(0, num_range)
    return r_num


def pick_random_color(palette):
    seed(time())
    color = choice(palette)
    return color


def draw_row(t: Turtle, dots: int, spacing: int, palette: list):
    for i in range(dots):
        size = 20
        color = pick_random_color(palette)
        t.pendown()
        t.dot(size, color)
        t.penup()
        t.forward(spacing)


def reset_position(t: Turtle):
    position = t.position()
    start_x = -500
    move_up = 50
    position += (start_x, move_up)
    t.setposition(position)


def draw_painting(t: Turtle, rows: int, dots: int, spacing, palette: list):
    start_position: tuple = (0, -350)
    position: tuple = start_position
    t.setposition(position)
    for _ in range(0, rows):
        draw_row(t, dots, spacing, palette)
        reset_position(t)


"""
No longer needed as I've already extracted the colors and manually put them in
their own list. Which can be found in 'colors.py'
def create_color_palette(color_palette):
    palette = []
    item_range = len(color_palette) - 1
    for i in range(item_range):
        cg: colorgram.Color = color_palette[i].rgb
        r = cg.r
        g = cg.g
        b = cg.b
        c: tuple = (r, g, b)
        palette.append(c)
    return palette
"""


def main():
    screen: Screen = Screen()
    screen.screensize(canvwidth=SCREEN_WIDTH, canvheight=SCREEN_HEIGHT)
    screen.colormode(COLOR_MODE)
    t: Turtle = Turtle()
    t.pensize(20)
    t.penup()
    t.hideturtle()

    """
    Colours already extracted, step no longer needed.
    colors = create_color_palette(image_colors)
    print(colors)   # <- used to manually create and filter the 'rbg_colors'
                    # found inside the 'colors.py' file.
    """
    draw_painting(t, DOTS, ROWS, SPACING, color_list)
    screen.exitonclick()


if __name__ == '__main__':
    main()
