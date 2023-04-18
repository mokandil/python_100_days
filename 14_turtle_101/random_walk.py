# create a simple random walk using turtle
# the turtle will move equal distance in a random direction
# with a random color
import turtle
from turtle import Turtle, Screen
import random

# create a turtle object
tim = Turtle()

# change the font width to 10
tim.width(10)

# create a list of directions
directions = [0, 90, 180, 270]

# create a function to generate a random color
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# create a function to move the turtle in a random direction given a distance
# but within the screen boundaries
def move_turtle(distance):
    tim.speed("fastest")
    tim.pencolor(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(distance)





# move the turtle 100 times
for _ in range(100):
    move_turtle(30)







# create screen object
screen = Screen()
screen.colormode(255)

# close the screen when you click on it
