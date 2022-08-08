from turtle import Turtle, Screen, width
import random

screen = Screen()
game_mode_on = False
screen.setup(width=500, height=400)
user_choice = screen.textinput("Your choice", "Type in your winner: ")
turtles_list = []
colors = ["blue", "red", "orange", "purple", "yellow", "brown"]
y_positions = [-75, -45, -15, 15, 45, 75]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    turtles_list.append(new_turtle)

if user_choice:
    game_mode_on = True

while game_mode_on:
    for turtle in turtles_list:
        if turtle.xcor() > 220:
            if user_choice == turtle.color():
                print(f"You won! Turtle {turtle.color()[0]} is winner.")
            else:
                print(f"You lost! Turtle {turtle.color()[0]} is winner.")
            game_mode_on = False
        distance = random.randint(2, 10)
        turtle.forward(distance)

screen.exitonclick()