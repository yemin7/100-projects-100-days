import os
import random

EASY = 10
HARD = 5


def guess_num(level, number):
    count = 0
    if level == "easy":
        count = EASY
    elif level == "hard":
        count = HARD

    while count > 0:
        print(f"You have {count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            return
        elif guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        count -= 1

    if count == 0:
        print("You are run out of guesses, you loose.")

end_game = False
def play_game():

    global end_game
    while not end_game:
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
        number = random.randint(1, 100)

        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        guess_num(level, number)
        result = input("Do you wanna guess again? y/n: ")
        if result == 'y':
            os.system('clear')
            play_game()
        else:
            end_game = True


play_game()
