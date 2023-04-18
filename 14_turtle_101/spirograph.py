# create a spirograph using turtle
import turtle
from turtle import Turtle, Screen
import random

# create a turtle object
t = Turtle()


# create a function to generate random colors
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# create a function to draw a circle
def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.speed("fastest")
        t.pencolor(random_color())
        t.circle(100)
        current_heading = t.heading()
        new_heading = current_heading + size_of_gap
        t.setheading(new_heading)


# draw a spirograph
draw_circle(10)











# create a screen object
s = Screen()
s.exitonclick()