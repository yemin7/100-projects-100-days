import random
import os
import hangman_art as art
import hangman_word as hword

print(art.logo)

random_word = random.choice(hword.word_list)

blank_list = ["_"] * len(random_word)
result = ""

end_game = False

hangman_pos = len(art.stages) - 1

while not end_game:
    word = input("Guess word: ").lower()
    os.system('clear')

    if word in blank_list:
        print(f"You already guessed {word}")

    for i in range(len(random_word)):
        if word == random_word[i]:
            blank_list[i] = word

    if word not in random_word:
        hangman_pos -= 1
        print(art.stages[hangman_pos])

        if hangman_pos == 0:
            # print(stages[hangman_pos])
            end_game = True
            print("You lose.")
            break

    print(result.join(blank_list))

    if not "_" in blank_list:
        print("You win.")
        end_game = True
