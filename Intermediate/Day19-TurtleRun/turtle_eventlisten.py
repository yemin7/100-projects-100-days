from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def moveForward():
    tim.forward(10)


def moveBackward():
    tim.backward(10)


def moveLeft():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def moveRight():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clearScreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=moveForward)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="a", fun=moveLeft)
screen.onkey(key="d", fun=moveRight)
screen.onkey(key="c", fun=clearScreen)
screen.exitonclick()
