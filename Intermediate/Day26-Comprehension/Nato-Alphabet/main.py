import pandas
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}
# print(nato_dict)

word = input("Enter a word: ")

nato_words = [nato_dict[character.upper()] for character in word]

print(nato_words)
