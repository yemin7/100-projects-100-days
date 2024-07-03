import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
TEXT_FONT_SIZE = 40
WORD_FONT_SIZE = 60
to_learn = {}
current_card = {}

# ---------------------------- Functions ------------------------------- #

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/thai_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Random words
def random_cards():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    # current_card = data["Thai"].sample(1).iloc[0]
    canvas.itemconfig(text, text="Thai", fill="black")
    # canvas.itemconfig(word, text=current_card, fill="black")
    canvas.itemconfig(word, text=current_card["Thai"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)

    flip_timer = screen.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(text, text="English", fill="white")

    # word_thai = data[data["Thai"] == current_card]
    # word_english = word_thai["English"].iloc[0]
    # canvas.itemconfig(word, text=word_english, fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    random_cards()


# ---------------------------- UI SETUP  ------------------------------- #

screen = Tk()
screen.title("Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = screen.after(2000, flip_card)

# Canvas
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 300, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
text = canvas.create_text(400, 220, text="", fill="black", font=(FONT_NAME, TEXT_FONT_SIZE, "normal"))
word = canvas.create_text(400, 300, text="", fill="black", font=(FONT_NAME, WORD_FONT_SIZE, "bold"))
# english_word = canvas.create_text(400, 300, text="", fill="black", font=(FONT_NAME, WORD_FONT_SIZE, "bold"))

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image, width=100, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=random_cards)
button_wrong.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_image, width=100, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=is_known)
button_right.grid(row=1, column=1)

random_cards()

screen.mainloop()
