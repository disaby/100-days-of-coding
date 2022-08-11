import turtle
from types import NoneType
import pandas, numpy

IMG = "us-states-game-start/blank_states_img.gif"

screen = turtle.Screen()
screen.title("US states")
screen.addshape(IMG)

turtle.shape(IMG)

# get mouse coordingate on screen:
"""
def get_mouse_coor(x, y):
    print(x, y)

screen.onscreenclick(get_mouse_coor)
"""

# Importing from csv
data = pandas.read_csv("us-states-game-start/50_states.csv")

all_states = data["state"].to_list()
found_states = []

user_input = screen.textinput(title="Guess the State",
                              prompt="What is the State's name?")

game_is_on = True
while game_is_on:
    if type(user_input) == NoneType:
        break
    else:
        if user_input.lower() == "exit":
            break
        if user_input != "":
            for state in all_states:
                if user_input.lower() == state.lower():
                    found_states.append(state)

                    series = data[data["state"] == state]
                    t = turtle.Turtle()
                    t.penup()
                    t.hideturtle()
                    t.goto(int(series["x"]), int(series["y"]))
                    t.write(series["state"].item())

                    all_states.remove(state)

            if len(found_states) == 50:
                game_is_on = False
        user_input = screen.textinput(title=f"{len(found_states)}/50 State",
                                      prompt="What is the State's name?")

# States to learn.csv
export = pandas.Series(all_states, numpy.arange(1, len(all_states) + 1))
export.to_csv("states_to_learn.csv")

turtle.mainloop()