import turtle
import time

tim = turtle.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
time.sleep(5)