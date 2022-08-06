import turtle
import random

# import colorgram

# colors = colorgram.extract('hirst-spot/index.jpeg', 25)
# color_list = []
# for item in colors:
#     color_list.append((item.rgb[0], item.rgb[1], item.rgb[2]))

# print(color_list)

rgb_colors = [(195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52),
              (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85),
              (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67),
              (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82),
              (207, 202, 146), (144, 176, 161), (178, 150, 156),
              (176, 202, 188), (217, 179, 172), (22, 77, 93)]

tim = turtle.Turtle()
tim.hideturtle()
turtle.colormode(255)


def draw_hirst():
    tim.penup()
    tim.goto(-250, -250)

    for line_no in range(10):
        tim.goto(-250, -250 + line_no * 50)
        for _ in range(10):
            tim.pendown()
            tim.dot(30, random.choice(rgb_colors))
            tim.penup()
            tim.forward(50)


draw_hirst()

screen = turtle.Screen()
screen.exitonclick()
