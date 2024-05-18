def add (*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1,6,3,6,7,45,3,4,3,56))


def calculate(n, **kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    #
    # print(kwargs["add"])
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):

        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")

print(my_car.make)