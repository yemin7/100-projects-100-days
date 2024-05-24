import os
import random
import logo

from game_data import data

score = 0
correct_guess = True


def get_data():
    return random.choice(data)


def guess_followers(compareA, compareB, guess):
    if guess == 'a' and compareA["follower_count"] > compareB["follower_count"]:
        return score + 1, True
    elif guess == 'b' and compareB["follower_count"] > compareA["follower_count"]:
        return score + 1, True
    else:
        return score, False


def print_data():
    print(f"Compare A: {compareA['name']}, {compareA['description']}, from {compareA['country']}")
    print(logo.vs)
    print(f"Against B: {compareB['name']}, {compareB['description']}, from {compareB['country']}")


print(logo.logo)

# random_num = random.sample(range(0, len(data)), 2)
# compareA = data[random_num[0]]
# compareB = data[random_num[1]]
compareA = get_data()
compareB = get_data()

while correct_guess:
    compareA = compareB
    compareB = get_data()

    while compareA == compareB:
        compareB = get_data()

    print_data()

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    score, correct_guess = guess_followers(compareA, compareB, guess)

    os.system('clear')
    print(logo.logo)
    if correct_guess:
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
