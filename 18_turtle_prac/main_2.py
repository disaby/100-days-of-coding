import turtle
import time
import random

tim = turtle.Turtle()
colors = [
    "blue", "sea green", "orange", "medium violet red", "deep pink",
    "pale violet red", "olive drab", "steel blue", "light blue"
]


def draw(side_no):
    angle = 360 / side_no
    tim.pencolor(random.choice(colors))
    for _ in range(side_no):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    draw(i)

time.sleep(5)