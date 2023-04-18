import turtle
import random

CAR_COLORS = ["red", "yellow", "green", "orange"]
SPEED_INCREMENT = 2

class Car:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color(random.choice(CAR_COLORS))
        self.turtle.shapesize(stretch_wid=1, stretch_len=2)
        self.turtle.penup()
        self.turtle.goto(random.randint(-300, 300), random.randint(-100, 100))
        self.speed = random.randint(1, 5)

    def move(self):
        self.turtle.goto(self.turtle.xcor() - self.speed, self.turtle.ycor())

        # Check if the car has gone off the screen
        if self.turtle.xcor() < -300:
            self.turtle.goto(300, self.turtle.ycor())


    def speed_up(self):
        self.speed += SPEED_INCREMENT
