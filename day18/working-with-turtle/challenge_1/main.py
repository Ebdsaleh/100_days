# main.py
# Day 18 - Challenge 1 - Draw a Square
"""
In this challenge I we are drawing a 100 x 100 square using the Turtle graphics
library.
"""
from turtle import Turtle, Screen


# draw the square.
def draw_square(t: Turtle):
    sides = 4
    for _ in range(sides):
        t.forward(100)
        t.right(90)


def main():
    t = Turtle()
    t.shape("turtle")
    t.color("green")
    screen = Screen()
    draw_square(t)
    screen.exitonclick()


if __name__ == '__main__':
    main()
