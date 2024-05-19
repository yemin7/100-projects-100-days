import os

bidders = {}


def bidder(name, bid):
    bidders[name] = bid


def winner():
    max_bid = 0
    bidder_name = ""
    for name, bid in bidders.items():
        if bid > max_bid:
            max_bid = bid
            bidder_name = name

    print(f"The winner is {bidder_name} with a bid of ${max_bid}.")


end_bid = False

while not end_bid:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bidder(name, bid)

    result = input("Are there any other bidders? yes/no\n")

    if result == "yes":
        os.system('clear')
    elif result == "no":
        winner()
        end_bid = True
