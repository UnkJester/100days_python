from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600,height=600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)
s.getshapes()
snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up, 'Up')
s.onkey(snake.down, 'Down')
s.onkey(snake.left, 'Left')
s.onkey(snake.right, 'Right')

alive = True
while alive:
    s.update()
    time.sleep(0.1)
    # move
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        score.update_score()
        snake.extend()
    # Detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        alive = False
        score.game_over()
    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            alive = False
            score.game_over()


s.exitonclick()