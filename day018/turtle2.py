from turtle import Turtle, Screen
t = Turtle()
s = Screen()
t.showturtle()
t.color("red","dark green")
t.shape("turtle")
t.pencolor("dark blue")
t.resizemode('user')
t.turtlesize(4,4,2)
t.pensize(5)

for _ in range(50):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

s.exitonclick()