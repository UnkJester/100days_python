import colorgram
colors = colorgram.extract('images/image.jpg', 27)
list_colors = []
for i in colors:
    if i.proportion < 0.10:
        list_colors.append((i.rgb.r, i.rgb.g, i.rgb.b))

print(list_colors)

from create_turtle import CreateTurtle
import random
turtle = CreateTurtle()
t = turtle.get_turtle()
s = turtle.get_screen()
s.colormode(255)
t.penup()
t.speed('fastest')

circle_size = 10
distance_size = 30
for i in range(10):
    t.home()
    t.left(90)
    t.forward((circle_size + distance_size) * i)
    t.right(90)
    for j in range(10):
        t.fillcolor(list_colors[random.randint(0,len(list_colors)-1)])
        t.begin_fill()
        t.circle(circle_size)
        t.forward(circle_size + distance_size)
        t.end_fill()

s.exitonclick()
