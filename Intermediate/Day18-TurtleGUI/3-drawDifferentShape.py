import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("black", "yellow")

colors = ["blue", "gold2", "cyan", "azure", "coral", "DeepPink", "DarkViolet", "DarkGrey", "DarkOrange"]


def drawSquare(sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)


for shape in range(3, 10):
    turtle.pencolor(random.choice(colors))
    drawSquare(shape)

screen.exitonclick()
