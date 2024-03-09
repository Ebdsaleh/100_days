# snake.py
# Day 20 Project - Snake Game
"""
This is the class for the snake (player) for the snake game.

"""

from turtle import Turtle
import random
import time


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.body = []
        self.segments = 3
        self.segment_size = 20
        self.move_distance = 20
        self.directions = {"east": 0, "north": 90, "west": 180, "south": 270}
        self.create_body()
        self.head = self.body[0]
        self.tail = self.body[-1]

    def create_body(self):
        for i in range(0, self.segments):
            t: Turtle = Turtle(shape="square")
            t.penup()
            t.color(self.pick_random_color())
            t.setheading(self.directions["east"])
            t.goto((-self.segment_size * 1), 0)
            self.body.append(t)

    def add_segment(self, color):
        x_offset: float = self.body[-1].xcor()
        y_offset: float = self.body[-1].ycor()
        heading = self.head.heading()
        if heading == self.directions["east"]:
            x_offset -= self.segment_size
        elif heading == self.directions["north"]:
            y_offset -= self.segment_size
        elif heading == self.directions["west"]:
            x_offset += self.segment_size
        elif heading == self.directions["south"]:
            y_offset += self.segment_size
        t: Turtle = Turtle(shape="square")
        t.penup()
        t.color(color)
        t.setheading(heading)
        t.goto(x_offset, y_offset)
        self.body.append(t)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.forward(self.move_distance)

    def head_north(self):
        if self.head.heading() == self.directions["south"]:
            return
        else:
            self.head.setheading(self.directions["north"])

    def head_south(self):
        if self.head.heading() == self.directions["north"]:
            return
        else:
            self.head.setheading(self.directions["south"])

    def head_west(self):
        if self.head.heading() == self.directions["east"]:
            return
        else:
            self.head.setheading(self.directions["west"])

    def head_east(self):
        if self.head.heading() == self.directions["west"]:
            return
        else:
            self.head.setheading(self.directions["east"])

    def pick_random_color(self):
        color_range = 255
        random.seed(time.time())
        r = random.randint(0, color_range)
        g = random.randint(0, color_range)
        b = random.randint(0, color_range)
        color: tuple = (r, g, b)
        return color
