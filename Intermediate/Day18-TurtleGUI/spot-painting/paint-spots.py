import random
import turtle
from turtle import Turtle, Screen

colors = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5),
          (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),
          (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8),
          (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62),
          (5, 38, 33), (68, 219, 155)]

screen = Screen()
spot = Turtle()

turtle.colormode(255)
spot.penup()
spot.hideturtle()
spot.speed("fastest")
x = -300
y = -300
row = 10
column = 10
spot.setpos(x, y)

for i in range(column):
    for j in range(row):
        # spot.color(random.choice(colors))
        spot.dot(20, random.choice(colors))
        spot.setpos(x + (50*j), y + (50*i))

screen.exitonclick()
