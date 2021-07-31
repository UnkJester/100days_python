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
t.pendown()

for i in range(3,11):
    for j in range(i):
        t.forward(100)
        t.right(360/i)
    print(str(i))

s.exitonclick()