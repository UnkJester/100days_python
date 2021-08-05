from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(0,270)
        self.write(arg=f"Score: {self.score}", move=False, align='center',font=('Arial', 18, 'bold'))
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write(arg=f"GAME OVER", move=False, align='center',font=('Arial', 18, 'bold'))