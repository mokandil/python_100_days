from turtle import Turtle, Screen
from numpy import random

# create a turtle object
tim = Turtle()

# change its shape to turtle and color to red
tim.shape("turtle")
tim.color("red")


# # draw a square but with dashed lines style using for loop
# for _ in range(4):
#     for _ in range(15):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.right(90)

# create a dictionary of shapes and their number of sides
shapes = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8, "nonagon": 9}

# create a function to draw a shape with a given size and color
def draw_shape(size, color, shape):
    tim.color(color)
    for _ in range(shapes[shape]):
        tim.forward(size)
        tim.right(360/shapes[shape])


# create a list of colors to use with  size of 10 colors. ignore yellow and white
colors = ["red", "orange", "green", "blue", "purple", "pink", "brown", "black", "grey", "light blue"]

# draw a triangle inside a square inside a pentagon inside a hexagon inside a heptagon inside a octagon inside a nonagon
# but with different colors

for shape in shapes:
    color = random.choice(colors, replace=False)
    draw_shape(100, color, shape)









# create a screen object
screen = Screen()
# close the screen when you click on it
screen.exitonclick()