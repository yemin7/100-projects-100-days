import math

h = int(input("Height: "))
w = int(input("Width: "))

coverage = 5


def paint_calc(height, width, cover):
    cans = (height * width) / cover

    print(f"You'll need {math.ceil(cans)} cans of paint.")


paint_calc(height=h, cover=coverage, width=w)
