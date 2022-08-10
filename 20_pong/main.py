from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# The screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
#Paddle
paddle_l = Paddle((-360, 0))
paddle_r = Paddle((360, 0))
ball = Ball()
score = Scoreboard()
screen.update()

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
screen.tracer(1)

game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    ball.move()

    # Collide with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_dir_y()
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        if ball.xcor() >= 380:
            score.change_score(1, 0)
            time.sleep(1)
            ball.refresh(0, 1)
        elif ball.xcor() <= -380:
            score.change_score(0, 1)
            time.sleep(1)
            ball.refresh(1, 0)

    # Collision with paddles
    if (ball.distance(paddle_r) < 50
            and ball.xcor() > 340) or (ball.distance(paddle_l) < 50
                                       and ball.xcor() < -340):
        ball.change_dir_x()

# Freeze
screen.exitonclick()