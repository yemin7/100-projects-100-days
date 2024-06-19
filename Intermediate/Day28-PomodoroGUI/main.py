import math
from tkinter import *

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
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_work():
    count_down(WORK_MIN * 60)
    label_timer.config(text="Work", fg=GREEN)


def start_break():
    count_down(SHORT_BREAK_MIN * 60)
    label_timer.config(text="Break", fg=PINK)


def long_break():
    count_down(LONG_BREAK_MIN * 60)
    label_timer.config(text="Long Break", fg=RED)


def start_time():
    global reps
    reps += 1

    if reps % 8 == 0:
        long_break()
    elif reps % 2 == 0:
        start_break()
    else:
        start_work()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        start_time()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
            label_checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
# screen_width = screen.winfo_screenwidth()
# screen_height = screen.winfo_screenheight()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Label
label_timer = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=1, column=2)

label_checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_checkmark.grid(row=4, column=2)

# Button
button_start = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_time)
button_reset = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
button_start.grid(row=3, column=1)
button_reset.grid(row=3, column=3)

screen.mainloop()
