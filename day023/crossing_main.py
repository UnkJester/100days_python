import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
p = Player()
manager = CarManager()


screen.listen()
screen.onkeypress(p.run, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    manager.add_car()
    manager.drive(scoreboard.level)

    for car in manager.cars:
        if car.distance(p) < 20:
            p.squish()
            scoreboard.game_over()
            game_is_on = False
    if p.is_finished():
        p.next_level()
        scoreboard.update()

screen.exitonclick()
