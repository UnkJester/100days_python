from turtle import Screen
from snake import Snake
import time

s = Screen()
s.setup(width=600,height=600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)
snake = Snake()

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






s.exitonclick()