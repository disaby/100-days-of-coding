from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'bold')


class Score(Turtle):

    def __init__(self, height):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, height)
        self.points = 0
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.points}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)
