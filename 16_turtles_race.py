# create a simple betting game using turtles
# the idea is to create a game where the user can bet on a turtle
# from a set of 6 turtles with different colors
# that races to the finish line

import turtle
import random

# set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=400)


# create a list of colors
colors = ["red", "orange", "black", "green", "blue", "purple"]

# create a list of turtles' starting positions
start_positions = [-70, -40, -10, 20, 50, 80]

# let's shuffle the list of colors and the list of starting positions
random.shuffle(colors)
random.shuffle(start_positions)

# create a list of turtles
all_turtles = []

# create 6 turtles and add them to the list
for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=start_positions[turtle_index])
    all_turtles.append(new_turtle)

# create a user bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# a flag to check if the race has started
is_race_on = False

# let the turtles move forward until one of them reaches the finish line
if user_bet:
    is_race_on = True

# while the race is on, the turtles move forward until one of them reaches the finish line
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

if winning_color == user_bet:
    print(f"You've won! The {winning_color} turtle is the winner!")
else:
    print(f"You've lost! The {winning_color} turtle is the winner!")








# close the screen on click
screen.exitonclick()