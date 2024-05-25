from menu import MENU
from menu import resources

money = 0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there isn't enough {items}.")
            return False
    return True


def process_coin():
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)


def check_transaction(coins, cost):
    global money
    # cost = MENU[coffee]["cost"]
    if coins < cost:
        print("Sorry that isn't enough money. Money refunded!")
        return False
    elif coins >= cost:
        money += cost
        print(f"Here is ${round(coins - cost, 2)} in change.")
        return True


def make_coffee(coffee, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {coffee} ☕️")


def coffee_machine():
    while True:
        check_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if check_input == "off":
            return False
        elif check_input == "report":
            print_report()
        else:
            drink = MENU[check_input]

            is_enough = check_resources(drink["ingredients"])
            if is_enough:
                print(f"The coffee costs {MENU[check_input]['cost']}")

                coins = process_coin()
                print(f"You pay: {round(coins, 2)}")

                if check_transaction(coins, drink["cost"]):
                    make_coffee(check_input, drink["ingredients"])


coffee_machine()
