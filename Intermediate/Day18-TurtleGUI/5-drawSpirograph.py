import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

turtle.speed(20)
turtle.colormode(255)
radius = 100

directions = [0, 90, 180, 270]


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def drawCircle(circle_gap, radius):
    for _ in range(int(360/circle_gap)):
        turtle.color(randomColor())
        print(type(randomColor()))
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + circle_gap)


circle_gap = 5
drawCircle(circle_gap, radius)

screen.exitonclick()
