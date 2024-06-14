from tkinter import *

window = Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.title("First GUI Program")
window.minsize(width=width // 2, height=height // 2)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

# my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    input_sentence = input.get()
    my_label.config(text=input_sentence)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

# Text
textbox = Text(height=5, width=30)
# Puts cursor in textbox
textbox.focus()
# Adds some text to begin wit.
textbox.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line1, character 0
textbox.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# ListBox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
