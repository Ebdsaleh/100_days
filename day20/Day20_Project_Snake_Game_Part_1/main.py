# main.py
# Day 20 Project - Snake Game - part 1

"""
Snake game Project part 1:
    Setup the screen.
    Create the snake body.
    Animate the snake segments.
    Create the Snake class and move to OOP.
    Control the snake with key presses.
"""
from turtle import Screen
from snake import Snake
import time
# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
COLOR_MODE = 255
# To offset the screen to display on my 2nd monitor on the right ->>>
# If you are not using an extended monitor configuration set the
# X_OFFSET and Y_OFFSET to 0.
X_OFFSET = 2600
Y_OFFSET = 199
# Setup the screen.
screen: Screen = Screen()
screen.setup(
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
        startx=X_OFFSET, starty=Y_OFFSET
        )
screen.colormode(COLOR_MODE)
screen.bgcolor("black")
screen.title("Snake Game")

game_is_on: bool = True


def main():
    screen.tracer(0)
    snake = Snake()
    screen.listen()
    screen.onkey(key="w", fun=snake.head_north)
    screen.onkey(key="s", fun=snake.head_south)
    screen.onkey(key="a", fun=snake.head_west)
    screen.onkey(key="d", fun=snake.head_east)
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
    screen.exitonclick()


if __name__ == '__main__':
    main()
