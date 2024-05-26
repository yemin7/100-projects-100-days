from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
# menuItem = MenuItem()
moneyMachine = MoneyMachine()
menu1 = Menu()

is_on = True
while is_on:
    coffee_type = input(f"What would you like? {menu1.get_items()}: ").lower()
    if coffee_type == "off":
        # return False
        is_on = False
    elif coffee_type == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu1.find_drink(coffee_type)

        if drink is None:
            continue
        else:
            if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
