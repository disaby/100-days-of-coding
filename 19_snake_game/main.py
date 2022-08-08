from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("The Snake game")

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_mode_on = True
while game_mode_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()