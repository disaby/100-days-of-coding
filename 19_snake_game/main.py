from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("The Snake game")

snake = Snake()
food = Food()
score = Score((screen.window_height() / 2 - 40))

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

    # Detecting collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        score.points += 1
        score.show_score()
        snake.grow()

    # Detecting collision with wall.
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor(
    ) > 280 or snake.head.ycor() < -280:
        game_mode_on = False
        score.game_over()

    # Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_mode_on = False
            score.game_over()

screen.exitonclick()