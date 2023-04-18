# create a turtle crossing game using the turtle module
# Use OOP to create a player, cars, and scoreboard

import turtle
import random
import time
from scoreboard import Scoreboard
from car import Car
from player import Player

# Set up the screen
screen = turtle.Screen()
screen.title("Crossing Street Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Define the CrossingStreetGame class
class CrossingStreetGame:
    def __init__(self):
        self.player = Player()
        self.cars = [Car() for _ in range(10)]
        self.scoreboard = Scoreboard()
        self.is_game_over = False

        # Set up the key bindings
        screen.listen()
        screen.onkeypress(self.player.move_up, "Up")
        screen.onkeypress(self.player.move_down, "Down")
        screen.onkeypress(self.player.move_left, "Left")
        screen.onkeypress(self.player.move_right, "Right")
        screen.onkeypress(screen.bye, "q")   # Quit the game
        screen.onkeypress(self.start_new_game, "r")  # Start a new game


        # Draw the street's borders
        street_border = turtle.Turtle()
        street_border.speed(0)
        street_border.color("white")
        street_border.penup()
        street_border.goto(-320, -150)
        street_border.pendown()
        street_border.pensize(3)
        street_border.forward(640)
        street_border.penup()
        street_border.goto(-320, 150)
        street_border.pendown()
        street_border.forward(640)

        # Set up the game loop
        self.game_loop()

    def game_loop(self):
        while not self.is_game_over:

            # Wait for 0.1 seconds
            time.sleep(0.1)
            screen.update()

            # Move the cars
            for car in self.cars:
                car.move()

                # Check for collisions with the player
                if self.player.is_collision(car):
                    self.player.turtle.color("red")
                    self.scoreboard.game_over()
                    self.is_game_over = True
                    break

            # Check if the game is over
            if self.is_game_over:
                break

            # Check if the player has reached the other side
            if self.player.turtle.ycor() > 150:
                self.player.turtle.color("royal blue")
                self.player.turtle.goto(0, -200)
                self.scoreboard.increase_score()
                for car in self.cars:
                    car.speed_up()

            # Update the screen
            self.scoreboard.update_score()
            screen.update()

        # Keep the window open when the game is over
        screen.mainloop()

    def start_new_game(self):
        # Reset the game
        self.is_game_over = False

        # Reset the player
        self.player.turtle.clear()
        self.player.turtle.color("royal blue")
        self.player.turtle.goto(0, -200)
        
        # Reset the cars
        for car in self.cars:
            car.turtle.hideturtle()
        self.cars = [Car() for _ in range(10)]

        # Reset the score
        self.scoreboard.turtle.goto(0, 200)
        self.scoreboard.score = 0
        self.scoreboard.update_score()
        self.game_loop()


# Start the game
game = CrossingStreetGame()

