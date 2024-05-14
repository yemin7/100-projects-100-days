import random

name_string = input()
names = name_string.split(", ")

random_index= random.randint(0, len(names)-1)
print(f"{names[random_index]} is going to buy the meal today!")
