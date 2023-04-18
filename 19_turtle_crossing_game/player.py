import turtle

PLAYER_COLOR = "royal blue"
PLAYER_POSITION = (0, -200)
MOVE_INCREMENT = 20

class Player:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("turtle")
        self.turtle.color(PLAYER_COLOR)
        self.turtle.penup()
        self.turtle.goto(PLAYER_POSITION)
        self.turtle.setheading(90)

    def move_up(self):
        y = self.turtle.ycor()
        self.turtle.sety(y + MOVE_INCREMENT)
                         
    def move_down(self):
        y = self.turtle.ycor()
        self.turtle.sety(y - MOVE_INCREMENT)

    def move_left(self):
        x = self.turtle.xcor()
        self.turtle.setx(x - MOVE_INCREMENT)

    def move_right(self):
        x = self.turtle.xcor()
        self.turtle.setx(x + MOVE_INCREMENT)

    def is_collision(self, other):
        if self.turtle.distance(other.turtle) < 20:
            return True
        else:
            return False
