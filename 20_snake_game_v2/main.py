import turtle
import time
import random
from snake2 import Snake
from food import Food
from scoreboard import Scoreboard

# Border parameters
BORDER_LENGTH = 500


# Game class
class SnakeGame:
    def __init__(self):
        # create the screen
        self.screen = turtle.Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)   # turn off the screen updates

        # create a snake
        self.snake = Snake()

        # create food
        self.food = Food()

        # create a scoreboard
        self.scoreboard = Scoreboard()

        # set the keyboard bindings
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.quit_game, "q")
        self.screen.onkey(self.restart_game, "r")

        # Draw borders
        self.border = turtle.Turtle()
        self.border.speed(0)
        self.border.penup()
        self.border.pensize(3)
        self.border.color("white")
        self.border.goto(-BORDER_LENGTH / 2, BORDER_LENGTH / 2)
        self.border.pendown()
        for i in range(4):
            self.border.forward(BORDER_LENGTH)
            self.border.right(90)
        self.border.hideturtle()

        # let the snake move while the game is running
        self.game_on = True
        self.play_game()

    def play_game(self):
        while self.game_on:
            self.screen.update()            # update the screen
            time.sleep(0.1)
            self.snake.move()

            # detect collision with food
            if self.snake.head.distance(self.food) < 20:
                self.food.refresh()
                self.scoreboard.increase_score()
                self.snake.extend()

            # detect collision with wall
            head_xpos = self.snake.head.xcor()
            head_ypos = self.snake.head.ycor()

            collide_top = head_ypos > BORDER_LENGTH / 2
            collide_bottom = head_ypos < -BORDER_LENGTH / 2
            collide_right = head_xpos > BORDER_LENGTH / 2
            collide_left = head_xpos < -BORDER_LENGTH / 2

            if collide_top or collide_bottom or collide_right or collide_left:
                self.game_on = False
                self.scoreboard.game_over()

            # detect collision with tail
            for segment in self.snake.segments[:-1]:
                if self.snake.head.distance(segment) < 10:
                    self.game_on = False
                    self.scoreboard.game_over()

    def quit_game(self):
        self.game_on = False
        self.screen.bye()

    def restart_game(self):
        self.game_on = False
        self.screen.clear()
        SnakeGame()


# create a new game instance
game = SnakeGame()

# exit the screen on click
game.screen.exitonclick()
