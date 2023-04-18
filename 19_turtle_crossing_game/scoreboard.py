import turtle

FONT = ("Courier", 24, "normal")
SCORE_POSITION = (0, 200)
SCORE_INCREMENT = 10

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(SCORE_POSITION)
        self.update_score()

    def update_score(self):
        self.turtle.clear()
        self.turtle.write("Score: {}".format(self.score), align="center", font=FONT)

    def increase_score(self):
        self.score += SCORE_INCREMENT
        self.update_score()

    def game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.write("Game Over", align="center", font=FONT)
