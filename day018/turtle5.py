from create_turtle import CreateTurtle
import random
tur = CreateTurtle()
t = tur.get_turtle()
s = tur.get_screen()
s.colormode(255)
# faster turtle
t.speed('fastest')
# thicker lines
t.pensize(5)
num_circles = 100
for i in range(num_circles):
    # todo random color
    t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    t.forward(1)
    t.circle(radius=100)
    t.home()
    t.left(360/num_circles*i)
s.exitonclick()

#circles, random colors, size of 100