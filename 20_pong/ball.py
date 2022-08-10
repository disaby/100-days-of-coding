from re import L
from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(-360, 360))

    def move(self):
        self.fd(2)

    def change_dir_y(self):
        new_h = -self.heading()
        self.setheading(new_h)

    def change_dir_x(self):
        self.setheading(180 - self.heading())

    def refresh(self, l, r):
        self.goto(0, 0)
        if l == 1:
            self.seth(random.randint(-90, 90))
        elif r == 1:
            self.seth(random.randint(90, 270))
