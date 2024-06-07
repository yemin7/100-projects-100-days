import pandas
from turtle import Turtle

FONT = ("Arial", 10, "normal")

class States:
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.data_list = self.data["state"].to_list()
        self.score = 0

    def user_import(self, text):
        if text in self.data_list:
            self.increase_score()
            self.createState(text)
            return text

    def increase_score(self):
        self.score += 1

    def createState(self, text):
        t = Turtle()
        t.hideturtle()
        t.penup()
        coor = self.data[self.data["state"] == text]
        t.goto(int(coor.x.iloc[0]), int(coor.y.iloc[0]))
        t.write(coor.state.item(), font=FONT)

    def save_to_csv(self, data):
        new_data = pandas.DataFrame(data)
        new_data.to_csv("state_to_learn.csv")
