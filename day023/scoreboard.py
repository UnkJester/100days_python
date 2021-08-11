from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.speed('fastest')
        self.goto(-260, 260)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        go = Turtle()
        go.hideturtle()
        go.penup()
        self.speed('fastest')
        self.goto(-50, 0)
        self.color('red')
        self.write(arg=f"GAME OVER", font=("Courier", 24, "bold"))
