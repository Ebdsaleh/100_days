# scoreboard.py
# Day 21 Project - Snake Game scoreboard
"""
This class is responsible for keeping and displaying the player's score.

"""
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("green")
        self.score: int = 0
        self.score_text: str = "SCORE: "
        self.font_name: str = "Courier"
        self.font_size: int = 20
        self.font_style: str = "bold"
        self.pos_x: int = -10
        self.pos_y: int = 280 - self.font_size
        self.text_alignment: str = "center"
        self.style: tuple = (self.font_name, self.font_size, self.font_style)
        self.points: int = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(self.pos_x, self.pos_y)
        self.write(arg=f"{self.score_text}{self.score}",
                   font=self.style,
                   align=self.text_alignment)

    def set_points(self):
        if self.score < 100:
            self.points = 20
        elif 100 <= self.score < 500:
            self.points = 50
        elif 500 <= self.score < 1000:
            self.points = 100
        elif 1000 <= self.score < 2000:
            self.points = 200
        else:
            self.points = 500

    def increase_score(self):
        self.set_points()
        self.score += self.points
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(
                arg="GAME OVER!",
                font=self.style,
                align=self.text_alignment)
