# main.py
# Day 19 Project - Turtle Race
"""
In this project we ask the user which colour turtle they think will win.
we then let the turtles race and will inform them of the result.
"""

from turtle import Turtle, Screen
import random
from time import time

# constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
NUMBER_OF_TURTLES = 6
MAX_SPEED = 10
screen: Screen = Screen()
screen.setup(
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
        startx=SCREEN_WIDTH / 2,
        starty=SCREEN_HEIGHT / 2)
user_bet = screen.textinput(
        "Place Your Bet.", "Which turtle will win the race?"
        )
print(f"Betting on: {user_bet}\n")
text_turtle: Turtle = Turtle()
text_turtle.hideturtle()
style = ("Courier", 14, "bold")
text_turtle.penup()
text_turtle.goto(-230, -140)
text_turtle.pencolor(user_bet)
text_turtle.pendown()
text_turtle.write(arg=f"Betting on: {user_bet}", font=style, align="left")
text_turtle.penup()
text_turtle.home()

turtles = []
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
start_positions = [
        (-230, 140), (-230, 100), (-230, 60),
        (-230, 20), (-230, -20), (-230, -60),
        ]
race_end: bool = True


def create_turtles():
    for i in range(0, NUMBER_OF_TURTLES):
        t: Turtle = Turtle(shape="turtle")
        t.penup()
        t.color(colors[i])
        screen.register_shape(colors[i], "turtle")
        position: tuple = start_positions[i]
        t.setposition(position)
        turtles.append(t)


def move(t: Turtle):
    random.seed(time())
    movement: int = random.randint(1, MAX_SPEED)
    t.forward(movement)


def check_race_end(t: Turtle):
    if t.xcor() > 230:
        winner: str = t.pencolor()
        result: str = ""
        if user_bet == winner:
            result = "You won."
        else:
            result = "You lost."
        result_string: str = str(
                f"{result} The winner was {winner}\n"
                )
        text_turtle.pencolor(winner)
        text_turtle.write(arg=result_string, font=style, align="center")
        screen.bgcolor("grey")
        print(f"{result_string}\n")
        return True
    else:
        return False


def race():
    global race_end
    race_end = False
    while not race_end:
        for i in range(0, NUMBER_OF_TURTLES):
            move(turtles[i])
            if check_race_end(turtles[i]):
                race_end = True
                break


def main():
    screen.listen()
    create_turtles()
    race()
    screen.exitonclick()


if __name__ == '__main__':
    main()
