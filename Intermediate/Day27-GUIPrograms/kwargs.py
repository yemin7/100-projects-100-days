def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


mycar = Car(make="Nissan", model="Skyline")
print(mycar.model)
