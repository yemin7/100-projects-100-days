import pandas

nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}


def generate_nato():
    word = input("Enter a word: ").upper()
    try:
        nato_words = [nato_dict[character] for character in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato()
    else:
        print(nato_words)


generate_nato()
