from create_turtle import CreateTurtle
import random
tur = CreateTurtle()
t = tur.get_turtle()
s = tur.get_screen()
s.colormode(255)
# faster turtle
t.speed(6)
# thicker lines
t.pensize(20)
for i in range(100):
    # todo random color
    t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # todo random direction
    t.setheading(random.randint(0,3) * 90)
    t.forward(30)
s.exitonclick()