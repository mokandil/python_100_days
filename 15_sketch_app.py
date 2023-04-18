# create a sketch app using turtle module
import turtle
from turtle import Turtle, Screen

# create a turtle object
t = Turtle()

# create a screen object
s = Screen()

# set speed of the turtle object
t.speed("fastest")


# create a function to move the turtle forward
def move_forward():
    t.forward(10)


# create a function to move the turtle backward
def move_backward():
    t.backward(10)


# create a function to turn the turtle left
def turn_left():
    t.left(10)


# create a function to turn the turtle right
def turn_right():
    t.right(10)


# create a function to clear the screen
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


# create a function to draw a curve
def draw_curve():
    for i in range(20):
        t.right(1)
        t.forward(1)


# create a key binding
s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=turn_left)
s.onkey(key="d", fun=turn_right)
s.onkey(key="q", fun=draw_curve)
s.onkey(key="c", fun=clear_screen)

# exit on click
s.exitonclick()

s.exitonclick()
