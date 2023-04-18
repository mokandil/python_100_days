# create the famous snake game using turtle module

import turtle
import time
import random
from snake2 import Snake
from food import Food
from scoreboard import Scoreboard


# create the screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(width=600, height=600)
s.tracer(0)   # turn off the screen updates

# create a snake
snake = Snake()

# create food
food = Food()

# create a scoreboard
scoreboard = Scoreboard()


# set the keyboard bindings
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

# let the snake move while the game is running
game_on = True

while game_on:
    s.update()            # update the screen
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    head_xpos = snake.head.xcor()
    head_ypos = snake.head.ycor()

    collide_top = head_ypos > 280
    collide_bottom = head_ypos < -280
    collide_right = head_xpos > 280
    collide_left = head_xpos < -280

    if collide_top or collide_bottom or collide_right or collide_left:
        game_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[:-1]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()








# exit the screen on click
s.exitonclick()