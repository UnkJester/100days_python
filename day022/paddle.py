from turtle import Turtle

POSITIONS = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.score = 0

        if player == 1:
            self.goto(POSITIONS[0])
        else:
            self.goto(POSITIONS[1])
        self.speed('normal')

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)

    def score_point(self):
        self.score += 1
