#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / (height * height)

print(f"BMI is {round(bmi, 2)}")
