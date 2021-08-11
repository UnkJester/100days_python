STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.speed('fastest')
        self.penup()
        self.goto(STARTING_POSITION)
        self.speed('normal')
        self.is_alive = True

    def run(self):
        if self.is_alive:
            self.forward(MOVE_DISTANCE)

    def is_finished(self):
        return self.ycor() >= FINISH_LINE_Y

    def next_level(self):
        self.goto(STARTING_POSITION)

    def squish(self):
        self.shape('circle')
        self.color('red')
