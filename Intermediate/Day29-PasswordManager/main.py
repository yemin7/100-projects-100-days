from random import choice, randint, shuffle
from tkinter import messagebox
from tkinter import *
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    entry_password.delete(0, END)
    password = []
    letters_range = randint(8,10)
    numbers_range = randint(2, 4)
    symbols_range = randint(2, 4)
    password += ([choice(letters) for _ in range(letters_range)])
    password += ([choice(numbers) for _ in range(numbers_range)])
    password += ([choice(symbols) for _ in range(symbols_range)])

    shuffle(password)
    result = "".join(password)

    entry_password.insert(0, result)
    pyperclip.copy(result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP  ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=80, pady=80)

# Canvas
canvas = Canvas(width=200, height=200)
pw_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_image)
canvas.grid(row=0, column=1)

# Label
label_website = Label(text="Website:", font=(FONT_NAME, 14, "normal"))
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:", font=(FONT_NAME, 14, "normal"))
label_email.grid(row=2, column=0)

label_password = Label(text="Password:", font=(FONT_NAME, 14, "normal"))
label_password.grid(row=3, column=0)

# Entry
entry_website = Entry(width=42)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

entry_email = Entry(width=42)
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=24)
entry_password.grid(row=3, column=1)

# Button
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=40, command=save)
button_add.grid(row=4, column=1, columnspan=2)

screen.mainloop()
