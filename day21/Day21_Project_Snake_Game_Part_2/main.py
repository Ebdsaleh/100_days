# main.py
# Day 21 Project - Snake Game - part 2

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
from scoreboard import Scoreboard
from food import Food
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
screen._root.resizable(False, False)  # prevent screen resizing.
screen.colormode(COLOR_MODE)
screen.bgcolor((0, 0, 0))
screen.title("Snake Game")
game_is_on: bool = True


def is_wall_collision(snake: Snake):
    x_border = (SCREEN_WIDTH / 2) - (snake.segment_size / 2)
    y_border = (SCREEN_HEIGHT / 2) - (snake.segment_size / 2)
    if snake.head.xcor() > x_border or snake.head.xcor() < -x_border:
        return True
    elif snake.head.ycor() > y_border or snake.head.ycor() < -y_border:
        return True
    else:
        return False


def is_tail_collision(snake: Snake):
    for segment in snake.body[3:]:
        if snake.head.distance(segment) < 10:
            return True


def quit_game():
    screen.bye()


def main():
    global game_is_on
    screen.tracer(0)
    scoreboard: Scoreboard = Scoreboard()
    snake = Snake()
    food = Food()
    screen.listen()
    screen.onkey(key="w", fun=snake.head_north)
    screen.onkey(key="Up", fun=snake.head_north)
    screen.onkey(key="s", fun=snake.head_south)
    screen.onkey(key="Down", fun=snake.head_south)
    screen.onkey(key="a", fun=snake.head_west)
    screen.onkey(key="Left", fun=snake.head_west)
    screen.onkey(key="d", fun=snake.head_east)
    screen.onkey(key="Right", fun=snake.head_east)
    screen.onkey(key="Escape", fun=quit_game)
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            scoreboard.color(food.get_color())
            scoreboard.increase_score()
            snake.add_segment(food.get_color())
            food.spawn()

        # Detect collision with the wall
        if is_wall_collision(snake):
            game_is_on = False
            scoreboard.game_over()
        if is_tail_collision(snake):
            game_is_on = False
            scoreboard.game_over()
    screen.exitonclick()


if __name__ == '__main__':
    main()
