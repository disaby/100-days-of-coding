import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)


def main():
    screen.clear()
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(player.move, "Up")

    game_is_on = True
    i = 0
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()

        if player.ycor() > 280:
            player.refresh()
            scoreboard.levelup()
            car_manager.cars_faster()

        # Collision with cars
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.gameover()
                screen.onkey(main, "space")

        i += 1


main()

screen.exitonclick()
