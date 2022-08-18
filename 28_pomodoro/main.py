import tkinter as tk
import math
from tkinter.font import NORMAL

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    start_button.config(state=tk.NORMAL)
    checkp_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    start_button.config(state=tk.DISABLED)
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # countdown(long_break_sec)
        countdown(20)
        title_label.config(text="Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        # countdown(short_break_sec)
        countdown(5)
        title_label.config(text="Break", fg=PINK)
    else:
        # countdown(work_sec)
        countdown(25)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            print(marks)
            checkp_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
tomato_img = tk.PhotoImage(file="tomato.png")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer",
                       font=(FONT_NAME, 35, "bold"),
                       fg=GREEN,
                       bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,
                                130,
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start",
                         highlightthickness=0,
                         command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset",
                         highlightthickness=0,
                         command=reset_timer)
reset_button.grid(column=2, row=2)

checkp_label = tk.Label(bg=YELLOW)
checkp_label.grid(column=1, row=3)

window.mainloop()