import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("black", "yellow")


# turtle.pencolor("brown")

def drawSquare():
    turtle.forward(100)
    turtle.right(90)


for _ in range(4):
    drawSquare()

screen.exitonclick()
