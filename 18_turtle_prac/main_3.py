import turtle
import time
import random

colors = [
    "blue", "sea green", "orange", "medium violet red", "deep pink",
    "pale violet red", "olive drab", "steel blue", "light blue"
]
directions = [0, 90, 180, 270]

tim = turtle.Turtle()
tim.pensize(10)
tim.speed("fastest")
for _ in range(200):
    tim.setheading(random.choice(directions))
    tim.fd(30)
    tim.pencolor(random.choice(colors))

time.sleep(5)