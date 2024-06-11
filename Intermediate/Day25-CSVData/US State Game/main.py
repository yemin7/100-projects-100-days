import turtle
from turtle import Screen
from states import States

image = "blank_states_img.gif"
score = 0
guessStates = []

screen = Screen()
screen.addshape(image)
screen.title("US State Game")

states = States()
turtle.shape(image)

while len(guessStates) < 50:
    text = screen.textinput(title=f"{score}/50 States Correct", prompt="What is state name?").title()
    if text == "Exit":
        missingStates = [state for state in states.data_list if state not in guessStates] #List Comprehension
        states.save_to_csv(missingStates)
        break
    elif text not in guessStates:
        score += 1
        states.import_state(text)
        guessStates.append(text)
