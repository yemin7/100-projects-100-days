from turtle import Turtle


class Snake:

    def __init__(self):
        self.start_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        self.direction = "Right"

    def createSnake(self):
        for pos in self.start_position:
            self.addSegment(pos)

    def addSegment(self, pos):
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def eatFood(self):
        self.addSegment(self.segments[-1].pos())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.direction != "Down":
            self.head.setheading(90)
            self.direction = "Up"

    def down(self):
        if self.direction != "Up":
            self.head.setheading(270)
            self.direction = "Down"

    def left(self):
        if self.direction != "Right":
            self.head.setheading(180)
            self.direction = "Left"

    def right(self):
        if self.direction != "Left":
            self.head.setheading(0)
            self.direction = "Right"
