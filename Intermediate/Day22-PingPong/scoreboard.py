from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")

class ScoreBoard(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((x_pos/8), (y_pos/2)-50)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()
