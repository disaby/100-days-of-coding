import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    webs = website_entry.get().strip()
    usern = username_entry.get().strip()
    passw = password_entry.get().strip()
    tosave = f"{webs} | {usern} | {passw}\n"

    if len(webs) == 0 or len(usern) == 0 or len(passw) == 0:
        missing = ""
        if len(webs) == 0:
            missing += f"Website"
        if len(usern) == 0:
            if len(missing) != 0:
                missing += f"\nEmail/Username"
            else:
                missing += f"Email/Username"
        if len(passw) == 0:
            if len(missing) != 0:
                missing += f"\nPassword"
            else:
                missing += f"Password"
        messagebox.showerror(
            title="Error",
            message=
            f"All spaces need to be filled.\nStill need to enter:\n{missing}")

    else:
        is_ok = messagebox.askokcancel(
            title=webs,
            message=
            f"You have entered:\nEmail: {usern}\nPassword: {passw}\n\nConfirm to save"
        )
        if is_ok:
            # .TXT file
            with open("data.txt", "a") as file:
                file.write(tosave)

            # .JSON file
            new_data = {webs: {"email": usern, "password": passw}}
            try:
                with open("data.json", "r") as file:
                    data_dic = json.load(file)
                    data_dic.update(new_data)
            except FileNotFoundError:
                print("file not found")
                data_dic = new_data

            with open("data.json", "w") as file:
                json.dump(data_dic, file, indent=4)

            website_entry.delete(0, END)
            website_entry.focus()
            # username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH DATA ------------------------------- #


def search():
    website = website_entry.get().strip()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="No data", message="No data was saved yet")
    else:
        isfound = False
        for data_web in data:
            if data_web.lower() == website.lower():
                isfound = True
                toprint = f"Email: {data[data_web]['email']}\nPassword: {data[data_web]['password']}"
                messagebox.showinfo(title=data_web, message=toprint)
                break
        if isfound == False:
            messagebox.showerror(
                title="No data",
                message=f"No saved data for <{website}> website")
    finally:
        website_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ---- Labels-----#
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, pady=4)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2, pady=4, padx=10)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=4)

# ---- Inputs-----#

website_entry = Entry(width=23)
website_entry.grid(column=1, row=1, sticky=W + E)
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W + E)
username_entry.insert(0, "disaby@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3, sticky=W + E)

# ---- Buttons-----#
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky=W + E)

gener_pass_button = Button(text="Generate password", command=generate)
gener_pass_button.grid(column=2, row=3, sticky=W + E)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=E)

window.mainloop()