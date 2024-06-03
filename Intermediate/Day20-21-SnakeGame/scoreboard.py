from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, (height / 2) - 40)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(arg=f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)
