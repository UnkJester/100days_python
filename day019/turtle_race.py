from turtle import Turtle, Screen
import random
COLORS = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
racers = []
s = Screen()
s.setup(width=600,height=500)
for i in range(6):
    t = Turtle(shape='turtle')
    t.fillcolor(COLORS[i])
    t.penup()
    t.goto((s.window_width()/-2)+10,(s.window_height()/-2)+s.window_height()/4 + (i*s.window_height()/12))
    racers.append(t)
user_bet = s.textinput(title='Choose your turtle', prompt='Which turtle wil win the race? Enter a color: ').lower()

def move_forward(turt):
    turt.forward(random.randint(0,15))
winner = None
while not winner and user_bet:
    for i in racers:
        move_forward(i)
        if i.xcor() >= s.window_width()/2 - 20:
            winner = i
            break
s.title(f"You {'won' if user_bet == winner.fillcolor() else 'lost'}! {winner.fillcolor().title()} was the winner today!")
s.exitonclick()


