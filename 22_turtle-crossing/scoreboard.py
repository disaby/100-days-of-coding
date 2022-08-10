from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def levelup(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)