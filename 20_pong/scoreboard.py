from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 240)
        self.score_r = 0
        self.score_l = 0
        self.write(f"{self.score_l}     {self.score_r}",
                   align=ALLIGNMENT,
                   font=FONT)

    def change_score(self, left, right):
        self.clear()
        self.score_l += left
        self.score_r += right
        self.write(f"{self.score_l}         {self.score_r}",
                   align=ALLIGNMENT,
                   font=FONT)
