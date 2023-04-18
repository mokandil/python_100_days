# create the ball class and define its methods
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def check_wall_collision(self, scoreboard):
        # detect collision with the top and bottom walls
        collide_top = self.ycor() > 280
        collide_bottom = self.ycor() < -280
        if collide_top or collide_bottom:
            self.bounce_y()

        # detect collision with the right and left walls
        collide_right = self.xcor() > 380
        collide_left = self.xcor() < -380

        if collide_right:
            self.reset_position()
            scoreboard.left_paddle_scored()

        if collide_left:
            self.reset_position()
            scoreboard.right_paddle_scored()

    def check_collision_paddles(self, r_paddle, l_paddle):
        # detect collision with the right and left paddles
        collide_right_paddle = self.distance(r_paddle) < 50 and self.xcor() > 320
        collide_left_paddle = self.distance(l_paddle) < 50 and self.xcor() < -320

        if collide_right_paddle or collide_left_paddle:
            self.bounce_x()
