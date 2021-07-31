from turtle import Turtle, Screen
class CreateTurtle:

    def __init__(self):
        self.turtle = Turtle()
        self.screen = Screen()
        self.turtle.showturtle()
        self.turtle.color("red", "dark green")
        self.turtle.shape("turtle")
        self.turtle.pencolor("dark blue")
        self.turtle.resizemode('user')
        self.turtle.turtlesize(2, 2, 2)
        self.turtle.pensize(5)
        self.turtle.pendown()

    def get_turtle(self):
        return self.turtle

    def get_screen(self):
        return self.screen
