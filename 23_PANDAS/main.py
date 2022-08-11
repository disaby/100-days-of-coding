import pandas

data = pandas.read_csv("squirrel_data.csv")

grey = 0
black = 0
red = 0

for color in data["Primary Fur Color"]:
    if color == "Gray":
        grey += 1
    elif color == "Cinnamon":
        red += 1
    elif color == "Black":
        black += 1

d_colors = ["grey", "red", "black"]
d_count = [grey, red, black]

d = {"color": d_colors, "count": d_count}

data_to_print = pandas.DataFrame(d)

print(data_to_print)

data_to_print.to_csv("squirrel_count.csv")