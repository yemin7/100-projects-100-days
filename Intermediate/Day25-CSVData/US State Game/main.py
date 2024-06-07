import turtle
from turtle import Screen
from states import States

screen = Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guess_states = []
states = States()


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guess_states) < 50:
    text = screen.textinput(title=f"{states.score}/50 States Correct", prompt="What is state name?").title()
    if text == "Exit":
        missing_states = []
        for state in states.data_list:
            if state not in guess_states:
                missing_states.append(state)
        states.save_to_csv(missing_states)
        break
    if text not in guess_states:
        guess_states.append(states.user_import(text))
