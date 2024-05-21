import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []


def print_status(user_score, dealer_score):

    if user_score == dealer_score:
        print("Draw.")
    elif user_score > 21:
        print("You went over. You loose.")
    elif dealer_score > 21:
        print("Computer went over. You win.")
    elif user_score > dealer_score:
        print("You win.")
    else:
        print("You loose.")


def dealer_hit(user_score, dealer_score):
    while dealer_score < 17:
        dealer_cards.append(random.choice(cards))
        dealer_score = sum(dealer_cards)
    return dealer_score


def final_result(user_score, dealer_score):
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")


def blackjack():
    for _ in range(2):
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)

    user_hit = True
    high_score = False
    if (11 in dealer_cards) and (10 in dealer_cards):
        dealer_score = 0
        high_score = True
        user_hit = False
    elif (11 in user_cards) and (10 in user_cards):
        user_score = 0
        high_score = True
        user_hit = False

    while user_hit:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == 'n':
            user_hit = False
        elif hit == 'y':
            user_cards.append(random.choice(cards))
            user_score = sum(user_cards)
            if user_score > 21:
                user_hit = False

    if user_score <= 21 and user_score != 0 and dealer_score != 0:
        dealer_score = dealer_hit(user_score, dealer_score)

    if high_score:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {dealer_cards}, current score: {dealer_score}")
        if dealer_score == 0:
            print("Computer has blackjack. You loose.")
        elif user_score == 0:
            print("You has blackjack. You loose.")
    else:
        final_result(user_score, dealer_score)
        print_status(user_score, dealer_score)

    continue_game = input("Do you want to play it again? y/n: ")
    if continue_game == 'y':
        user_cards.clear()
        dealer_cards.clear()
        os.system('clear')
        blackjack()
    else:
        exit()


blackjack()
