from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(randint(-380, 380), randint(-280, 280))
