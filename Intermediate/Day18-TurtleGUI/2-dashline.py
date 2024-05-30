import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("black", "yellow")


# turtle.pencolor("brown")

def drawDashLine():
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


for _ in range(15):
    drawDashLine()

screen.exitonclick()
