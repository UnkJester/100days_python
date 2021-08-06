from turtle import Turtle
BALL_SPEED = 9


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.speed(BALL_SPEED)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.bounce()
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        print('wall bounce')
        self.y_move *= -1

    def bounce_left(self):
        print('paddle bounce left')
        if self.x_move > 1:
            self.move_speed *= .9
            self.x_move *= -1

    def bounce_right(self):
        print('paddle bounce right')
        if self.x_move < 1:
            self.move_speed *= .9
            self.x_move *= -1

    def center(self):
        self.speed('fastest')
        self.goto(0, 0)
        self.speed(BALL_SPEED)
        self.x_move *= -1
        self.move_speed = 0.1

