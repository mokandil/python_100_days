from turtle import Turtle
import os

# get the current directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# scoreboard settings
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_FILE = os.path.join(dir_path, "high_score.txt")


# scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

        # update the high score if necessary
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                high_score = int(file.read())
        except FileNotFoundError:
            high_score = 0

        return high_score

    def save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))
