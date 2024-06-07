import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color("white")
        self.speed("fastest")
        self.width = (width//2) - 20
        self.height = (height//2) - 20
        self.refresh()

    def refresh(self):
        random_x = random.randint(-self.width, self.width)
        random_y = random.randint(-self.height, self.height)
        self.goto(random_x, random_y)
