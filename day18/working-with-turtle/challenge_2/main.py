# main.py
# Day 18 - Challenge 2 - Draw a dashed line.
"""
In this challenge we are going to use the Turtle graphics library to draw a
dashed-line. e.g. _ _ _ _ _
"""
from turtle import Turtle, Screen


def draw_dashed_line(
        t: Turtle, length: int, size: int,
        color: str, paces: int
        ):
    t.pencolor(color)
    t.pensize(size)
    for i in range(length):
        if i % 2 == 0:
            t.penup()
        else:
            t.pendown()
        t.forward(paces)


def main():
    length = 50
    size = 5
    green = "green"
    paces = 10
    screen: Screen = Screen()
    t: Turtle = Turtle()
    t.color(green)
    t.shape("turtle")
    draw_dashed_line(t, length, size, green, paces)
    screen.exitonclick()


if __name__ == '__main__':
    main()
