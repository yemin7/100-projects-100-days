num = int(input("Give a number: "))


def prime_checker(number):
    prime = False
    for i in range(2, int(number / 2)):
        if number % i == 0:
            prime = False
            break
        else:
            prime = True
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(number=num)
