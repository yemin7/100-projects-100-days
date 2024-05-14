name1 = input("Name1: ")
name2 = input("Name2: ")

names = name1+name2

true_count = 0
love_count = 0

true_count += names.lower().count("t")
true_count += names.lower().count("r")
true_count += names.lower().count("u")
true_count += names.lower().count("e")

love_count += names.lower().count("l")
love_count += names.lower().count("o")
love_count += names.lower().count("v")
love_count += names.lower().count("e")

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")
