import turtle
import pandas as pd
import os

# get the name of the current directory
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "blank_states_img.gif")
data_path = os.path.join(current_dir, "50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
image = image_path
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv(data_path)
states_list = states_data["state"].to_list()

score = 0
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 270)
scoreboard.write(f"Score: {score}/{len(states_list)}", align="center", font=("Arial", 24, "normal"))

while score < len(states_list):
    answer_state = screen.textinput(title=f"{score}/{len(states_list)} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:
        state_data = states_data[states_data["state"] == answer_state]
        x = int(state_data["x"])
        y = int(state_data["y"])
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(x, y)
        state_name.write(answer_state, align="center", font=("Arial", 12, "normal"))
        score += 1
        scoreboard.clear()
        scoreboard.write(f"Score: {score}/{len(states_list)}", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()