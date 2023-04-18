# draw a piece of art using turtle
# random dots painting in a matrix with random colors

import turtle
from turtle import Turtle, Screen
import random

# create a turtle object
t = Turtle()

# set position
t.penup()             # pen up
t.setpos(-250, -250)  # set position
t.speed("fastest")    # set speed
t.hideturtle()        # hide the turtle

# create a function to generate random colors
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# create a function to draw a dot
def draw_dot():
    t.dot(20, random_color())



# create a function to draw a line of dots
def draw_line():
    for _ in range(10):
        draw_dot()
        t.forward(50)


# create a function to draw a matrix of dots
def draw_matrix():
    for _ in range(10):
        draw_line()
        t.backward(500)
        t.left(90)
        t.forward(50)
        t.right(90)


# draw a matrix of dots
draw_matrix()


# create screen object
s = Screen()
s.exitonclick()