# main.py
# day 19 Challenge: Etch-A-Sketch App
"""
In this challenge we are making an Etch-A-Sketch application using the Turtle
Graphics library. 
USER CONTROLS:
    KEY:    ACTION:
         'W'        Move the turtle forward.
         'S'        Move the turtle backward.
         'A'        Rotate the turtle counter-clockwise
         'D'        Rotate the turtle clockwise
         'C'        Clear the drawing and reset the turtle's position.
    Use mouse-left-click to exit program.
"""

from turtle import Turtle, Screen
# constants
MOVEMENT = 10
ROTATION = 10
t: Turtle = Turtle()
screen: Screen = Screen()


def clear_and_reset():
    t.penup()
    t.home()
    t.reset()
    t.pendown()


def move_forwards():
    t.forward(MOVEMENT)


def move_backwards():
    t.back(MOVEMENT)


def rotate_clockwise():
    t.right(ROTATION)


def rotate_counter_clockwise():
    t.left(ROTATION)


def handle_input(screen):
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=rotate_counter_clockwise)
    screen.onkey(key="d", fun=rotate_clockwise)
    screen.onkey(key="c", fun=clear_and_reset)


def main():
    screen.listen()
    handle_input(screen)
    screen.exitonclick()





if __name__ == '__main__':
    main()
