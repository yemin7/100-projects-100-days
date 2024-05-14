print("Thank you for choosing Python Pizza Deliveries!")
size = input("What pizza size do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? (Y or N): ")
extra_cheese = input("Do you want extra cheese? (Y or N) ")

price = 0

if size == "S":
    if add_pepperoni == "Y":
        price = 15 + 2
    else:
        price += 15

elif size == "M":
    if add_pepperoni == "Y":
        price = 20 + 3
    else:
        price += 20

elif size == "L":
    if add_pepperoni == "Y":
        price = 25 + 3
    else:
        price += 25

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")
