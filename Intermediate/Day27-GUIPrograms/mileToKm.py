from tkinter import *

FONT = ("Arial", 20, "normal")

screen = Tk()
width = 400
height = 100
screen.title("Mile to Km Converter")
screen.minsize(width=width, height=height)
screen.config(padx=20, pady=20)


def calculate():
    miles = input_miles.get()
    miles_to_km = round(1.609 * float(miles), 2)
    label_result.config(text=miles_to_km)


# Entry
input_miles = Entry(width=15)
input_miles.grid(row=0, column=1)

# Label
label_miles = Label(text="Miles", font=FONT)
label_miles.grid(row=0, column=2)

label_eq = Label(text="is equal to", font=FONT)
label_eq.grid(row=1, column=0)

label_result = Label(font=FONT)
label_result.grid(row=1, column=1)

label_km = Label(text="Km", font=FONT)
label_km.grid(row=1, column=2)

# Button
button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(row=2, column=1)

screen.mainloop()
