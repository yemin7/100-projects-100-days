from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


def readFile():
    with open("highscore.txt") as file:
        content = file.read()
        return int(content)


class ScoreBoard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.score = 0
        self.high_score = readFile()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, (height / 2) - 40)
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(arg=f"Score {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        # self.clear()
        self.updateScoreBoard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.updateScoreBoard()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)
