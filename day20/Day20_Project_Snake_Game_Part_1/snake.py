# snake.py
# Day 20 Project - Snake Game
"""
This is the class for the snake (player) for the snake game.

"""

from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        self.body = []
        self.segments = 3
        self.segment_size = 20
        self.move_distance = 20
        self.directions = {"east": 0, "north": 90, "west": 180, "south": 270}
        self.create_body()

    def create_body(self):
        for i in range(0, self.segments):
            t: Turtle = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.setheading(self.directions["east"])
            t.goto((-self.segment_size * 1), 0)
            self.body.append(t)

    def add_segment(self):
        x_offset: float = self.body[-1].xcor()
        y_offset: float = self.body[-1].ycor()
        heading = self.body[0].heading()
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
        t.color("white")
        t.setheading(heading)
        t.goto(x_offset, y_offset)
        self.body.append(t)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].forward(self.move_distance)

    def head_north(self):
        if self.body[0].heading() == self.directions["south"]:
            return
        else:
            self.body[0].setheading(self.directions["north"])

    def head_south(self):
        if self.body[0].heading() == self.directions["north"]:
            return
        else:
            self.body[0].setheading(self.directions["south"])

    def head_west(self):
        if self.body[0].heading() == self.directions["east"]:
            return
        else:
            self.body[0].setheading(self.directions["west"])

    def head_east(self):
        if self.body[0].heading() == self.directions["west"]:
            return
        else:
            self.body[0].setheading(self.directions["east"])
