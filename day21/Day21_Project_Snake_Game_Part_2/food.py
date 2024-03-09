# food.py
# Day 21 - Project Snake Game food.py
"""
This class is an item that is collected by the snake
which will allow the snake to grow its body.
"""

from turtle import Turtle
import random
import time


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.scale = 0.5
        self.shapesize(stretch_len=self.scale, stretch_wid=self.scale)
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        self.pick_random_color()
        random.seed(time.time())
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

    def pick_random_color(self):
        random.seed(time.time())
        color_range = 255
        r = random.randint(0, color_range)
        g = random.randint(0, color_range)
        b = random.randint(0, color_range)
        color: tuple = (r, g, b)
        self.color(color)

    def get_color(self):
        return self.convert_to_hex_string(self.color()[0])

    def convert_to_hex_string(self, color):
        r, g, b = color
        return "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
