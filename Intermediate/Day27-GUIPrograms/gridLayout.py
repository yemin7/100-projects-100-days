from tkinter import *


screen = Tk()
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

screen.title("Grid Layout")
screen.minsize(width=screen_width//2, height=screen_height//2)
screen.config(padx=screen_width//8, pady=screen_height//4)

# Label
label1 = Label(font=("Arial", 24, "bold"))
label1.config(text="A new Text")
label1.grid(row=0, column=0)

# Button
button1 = Button(text="Button 1")
button1.grid(row=1, column=1)

button2 = Button(text="Button 2")
button2.grid(row=0, column=2)


# Entry
input1 = Entry(width=10)
input1.grid(row=2,column=3)


screen.mainloop()
