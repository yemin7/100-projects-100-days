from turtle import Turtle, Screen
import time
from snake import Snake

width = 600
height = 600
game_on = True

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=width, height=height)
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
