import tkinter

windows = tkinter.Tk()
windows.title("First GUI program")
windows.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label",
                         font=("Times New Roman", 20, "bold"))
my_label.grid(column=0, row=0)


def click_button():
    print("Button clicked")
    inputtext = my_input.get()
    my_label.config(text=inputtext)


def click_button2():
    my_input.config(textvariable="Button clicked")


my_button = tkinter.Button(text="I am a Button", command=click_button)
my_button.grid(column=1, row=1)

my_input = tkinter.Entry()
my_input.grid(column=3, row=2)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)

windows.mainloop()