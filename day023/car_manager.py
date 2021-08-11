from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.penup()
        self.speed('fastest')
        self.goto(320, randint(-260, 260))
        self.speed('normal')
        self.shape('square')
        self.shapesize(1, 2)
        self.setheading(180)


class CarManager:
    def __init__(self):
        self.cars = []
        for i in range(20):
            car = Car()
            car.speed('fastest')
            car.setx(randint(-300, 300))
            car.speed('normal')
            self.cars.append(car)

    def add_car(self):
        if randint(1, 5) == 5:
            self.cars.append(Car())

    def drive(self, level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE * level)
