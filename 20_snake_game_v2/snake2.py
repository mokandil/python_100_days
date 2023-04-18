from turtle import Turtle


# create Snake class
class Snake:
    def __init__(self):
        self.start_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[-1]

    def create_snake(self):
        for pos in self.start_pos:
            self.add_segment(pos)

    def add_segment(self, pos):
        segment = Turtle()
        segment.shape("square")
        segment.color("royal blue")
        segment.penup()
        segment.goto(pos)
        self.segments.insert(0, segment)

    def extend(self):
        self.add_segment(self.segments[0].position())

    def move(self):
        head_idx = len(self.segments) - 1
        tail_idx = 0
        for idx in range(tail_idx, head_idx, 1):
            x = self.segments[idx + 1].xcor()  # get the x coordinate of the next segment
            y = self.segments[idx + 1].ycor()  # get the y coordinate of the next segment
            self.segments[idx].goto(x, y)      # move the current segment to the next segment's position

        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
