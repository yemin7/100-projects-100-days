from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

width = 600
height = 600
game_on = True

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=width, height=height)
screen.tracer(0)

snake = Snake()
food = Food(width, height)
scoreboard = ScoreBoard(height)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.updateScore()
        snake.eatFood()

    if (snake.head.xcor() > (width // 2) - 20 or snake.head.xcor() < (-width // 2) + 20 or
            snake.head.ycor() > (height // 2) - 20 or snake.head.ycor() < (-height // 2) + 20):
        scoreboard.gameOver()
        game_on = False

    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.gameOver()

screen.exitonclick()
