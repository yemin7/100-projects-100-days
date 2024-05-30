import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("black", "yellow")
turtle.pensize(10)
turtle.speed(5)
turtle.colormode(255)

directions = [0, 90, 180, 270]


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def randomWalk():
    turtle.pencolor(randomColor())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))


for _ in range(200):
    randomWalk()

screen.exitonclick()
