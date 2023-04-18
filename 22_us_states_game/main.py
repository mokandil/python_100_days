import turtle
import pandas as pd
import os

# get the name of the current directory
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "blank_states_img.gif")
data_path = os.path.join(current_dir, "50_states.csv")


class Screen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("US States Game")
        self.image = image_path
        self.screen.addshape(self.image)
        turtle.shape(self.image)


class StateMap:
    def __init__(self):
        self.states_data = pd.read_csv(data_path)
        self.states_list = self.states_data["state"].to_list()

    def get_state_data(self, state_name):
        state_data = self.states_data[self.states_data["state"] == state_name]
        x = int(state_data["x"])
        y = int(state_data["y"])
        return (x, y)


class Scoreboard:
    def __init__(self, total_states):
        self.score = 0
        self.total_states = total_states
        self.scoreboard = turtle.Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}/{self.total_states}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


class Game:
    def __init__(self):
        self.screen = Screen()
        self.state_map = StateMap()
        self.scoreboard = Scoreboard(len(self.state_map.states_list))
        self.play_game()

    def play_game(self):
        while self.scoreboard.score < len(self.state_map.states_list):
            answer_state = self.screen.screen.textinput(
                title=f"{self.scoreboard.score}/{len(self.state_map.states_list)} States Correct",
                prompt="What's another state's name?").title()

            if answer_state == "Exit":
                break

            if answer_state in self.state_map.states_list:
                x, y = self.state_map.get_state_data(answer_state)
                state_name = turtle.Turtle()
                state_name.hideturtle()
                state_name.penup()
                state_name.goto(x, y)
                state_name.write(answer_state, align="center", font=("Arial", 12, "normal"))
                self.scoreboard.increase_score()

        self.screen.screen.exitonclick()


if __name__ == "__main__":
    game = Game()
    game.play_game()
