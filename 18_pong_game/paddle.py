# create the paddle class and define its methods
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.step = 60
        self.speed(0)

    def go_up(self):
        new_y = self.ycor() + self.step
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - self.step
        self.sety(new_y)

