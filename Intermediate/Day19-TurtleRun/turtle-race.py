import random, turtle
from turtle import Turtle, Screen

turtles = []
width = 800
height = 700
turtle_count = 5
turtle.colormode(255)
race_on = False


def generate_y_coordinate(y_pos, total):
    if total <= 1:
        return [0]
    y_pos -= 150
    step = y_pos / (total - 1)
    return [int(-y_pos / 2 + i * step) for i in range(total)]


y = generate_y_coordinate(height, turtle_count)
colors = ["sandy brown", "brown", "orchid", "violet", "olive drab", "teal", "blue", "lime", "gold", "black", "red",
          "pink"]
turtle_colors = []


def create_turtles(total):
    while total > 0:
        name = "turtle" + str(total)
        name = Turtle()
        turtles.append(name)
        total -= 1


def turtles_position(turtles_list):
    for i in range(len(turtles_list)):
        turtles_list[i].shape("turtle")
        turtle_colors.append(random.choice(colors))
        turtles_list[i].color(turtle_colors[i])
        turtles_list[i].penup()
        turtles_list[i].goto((width / -2) + 20, y[i])


screen = Screen()
screen.setup(width, height)
create_turtles(turtle_count)
turtles_position(turtles)
user_bet = screen.textinput("Make your bet", f"Which turtle color will win the race?{turtle_colors}")

if user_bet:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > (width / 2) - 20:
            winner = t.pencolor()
            if user_bet == winner:
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You loose! The {winner} turtle is the winner!")
            race_on = False
        rand_move = random.randint(0, 10)
        t.forward(rand_move)

screen.exitonclick()
