#Write a program that works out whether if a given number is an odd or even number.

number = int(input("Give a number: "))

if (number%2) == 0:
    print(f"{number} is Even number.")
else:
    print(f"{number} is Odd number.")
