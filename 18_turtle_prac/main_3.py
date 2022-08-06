import turtle
import time
import random

tim = turtle.Turtle()
turtle.colormode(255)

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.pensize(10)
tim.speed("fastest")
for _ in range(200):
    tim.setheading(random.choice(directions))
    tim.fd(30)
    tim.pencolor(random_color())

time.sleep(5)