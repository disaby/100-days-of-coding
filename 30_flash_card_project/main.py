import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
rand_card = {}

###     -------------------     Player answer    ----------------------  ###


def right():
    data_dic.remove(rand_card)
    df = pandas.DataFrame(data_dic)
    df.to_csv("data/french_words.csv", index=0)
    next_card()


###     -------------------     Random word    ----------------------  ###

#   --- Reading data from csv   --- #

data = pandas.read_csv("data/french_words.csv")
data_dic = data.to_dict(orient="records")
print(data_dic)


def next_card():
    global rand_card, flip_timer
    rand_card = random.choice(data_dic)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=rand_card["French"], fill="black")
    canvas.itemconfig(bg_img, image=card_img_fr)

    right_button.config(state=DISABLED)
    wrong_button.config(state=DISABLED)

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(bg_img, image=card_img_eng)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=rand_card["English"], fill="white")

    right_button.config(state=NORMAL)
    wrong_button.config(state=NORMAL)


###     -------------------     UI    ----------------------  ###

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_img_eng = PhotoImage(file="./images/card_back.png")
card_img_fr = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526)
bg_img = canvas.create_image(400, 263, image=card_img_fr)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400,
                                160,
                                text="Title",
                                font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400,
                               263,
                               text="word",
                               font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=right)
right_button.config(highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.config(highlightthickness=0)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()