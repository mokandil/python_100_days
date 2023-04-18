# create food class
import random
from turtle import Turtle

# Food location parameters
FOOD_X = 200
FOOD_Y = 200

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-FOOD_X, FOOD_X)
        random_y = random.randint(-FOOD_Y, FOOD_Y)
        self.goto(random_x, random_y)
