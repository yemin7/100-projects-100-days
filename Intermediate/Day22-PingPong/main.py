import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

WIDTH = 800
HEIGHT = 600
game_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((WIDTH // 2) - 50)
l_paddle = Paddle((WIDTH // -2) + 50)

r_score = ScoreBoard(-WIDTH, HEIGHT)
l_score = ScoreBoard(WIDTH, HEIGHT)

ball = Ball()

screen.listen()
screen.onkey(r_paddle.goUp, "Up")
screen.onkey(r_paddle.goDown, "Down")
screen.onkey(l_paddle.goUp, "w")
screen.onkey(l_paddle.goDown, "s")

while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > (HEIGHT // 2) - 20 or ball.ycor() < (HEIGHT // -2) + 20:
        ball.y_bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > (WIDTH // 2) - 80) or (
            ball.distance(l_paddle) < 50 and ball.xcor() < (WIDTH // -2) + 80):
        ball.x_bounce()

    if ball.xcor() > (WIDTH / 2) - 30:
        r_score.updateScore()
        ball.reset()
    elif ball.xcor() < (WIDTH / -2) + 30:
        l_score.updateScore()
        ball.reset()

screen.exitonclick()
