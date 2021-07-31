from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.showturtle()
t.color("red","dark green")
t.shape("turtle")
t.pencolor("dark blue")
t.resizemode('user')
t.turtlesize(4,4,2)
t.pendown()
t.pensize(5)

for _ in range(4):
    t.forward(200)
    t.left(90)
s.exitonclick()