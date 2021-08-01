from turtle import Turtle, Screen
t = Turtle()
s = Screen()
s.listen()
def move_forward():
    t.forward(5)
def turn_right():
    # t.right(5)
    t.setheading((t.heading() - 10))
def turn_left():
    # t.left(5)
    t.setheading(t.heading() + 10)
def move_backward():
    t.backward(5)
def clear():
    t.reset()
s.onkey(key='w', fun=move_forward)
s.onkey(key='a', fun=turn_left)
s.onkey(key='s', fun=move_backward)
s.onkey(key='d', fun=turn_right)
s.onkey(key='c', fun=clear)

s.exitonclick()