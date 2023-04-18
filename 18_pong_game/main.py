# create the famous pong game
import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

# create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # turn off the animation of the screen

# create the left paddle
left_paddle = Paddle((-350, 0))

# create the right paddle
right_paddle = Paddle((350, 0))

# create the ball
ball = Ball()

# create the scoreboard
scoreboard = Scoreboard()

# listen to the key presses
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# test game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the top and bottom walls
    ball.check_wall_collision(scoreboard)

    # detect collision with the right and left paddles
    ball.check_collision_paddles(right_paddle, left_paddle)



# close the screen on click
screen.exitonclick()