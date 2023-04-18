# create scoreboard class
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_paddle_score} - {self.right_paddle_score}", align=ALIGNMENT, font=FONT)

    def left_paddle_scored(self):
        self.left_paddle_score += 1
        self.update_scoreboard()

    def right_paddle_scored(self):
        self.right_paddle_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

