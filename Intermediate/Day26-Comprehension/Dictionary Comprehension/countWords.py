sentence = input()

split_sentence = sentence.split(" ")

result = {word: len(word) for word in split_sentence}
print(result)
