import pandas
from turtle import Turtle

FONT = ("Arial", 12, "normal")


class States:
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.data_list = self.data["state"].to_list()

    def import_state(self, text):
        if text in self.data_list:
            t = Turtle()
            t.penup()
            t.hideturtle()
            coordinates = self.data[self.data["state"] == text]
            t.goto(int(coordinates.x.iloc[0]), int(coordinates.y.iloc[0]))
            t.write(text, font=FONT)

    def save_to_csv(self, data):
        tocsv = pandas.DataFrame(data)
        tocsv.to_csv("state_to_learn.csv")
