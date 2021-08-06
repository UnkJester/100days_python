from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=800, height=600)
s.title('PING')
s.bgcolor('black')
p1 = Paddle(1)
p2 = Paddle(2)
b = Ball()
score = Scoreboard()

s.listen()
s.onkeypress(p1.move_up, 'Up')
s.onkeypress(p1.move_down, 'Down')
s.onkeypress(p2.move_up, 'w')
s.onkeypress(p2.move_down, 's')

playing = True

while playing:
    time.sleep(b.move_speed)
    if -350 < b.xcor() < -320 and p2.distance(b) < 50:
        b.bounce_right()
    elif 320 < b.xcor() < 350 and p1.distance(b) < 50:
        b.bounce_left()
    b.move()

    if b.xcor() > 380:
        print('p2 scores')
        score.left_score()
        b.center()
    elif b.xcor() < -380:
        print('p1 scores')
        score.right_score()
        b.center()


    s.update()
s.exitonclick()
