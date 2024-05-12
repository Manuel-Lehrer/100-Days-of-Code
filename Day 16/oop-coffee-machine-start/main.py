from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drink = Menu()
functionality = CoffeeMaker()
payment = MoneyMachine()

turned_on = True

while turned_on is True:
    choice = input(f"What would you like? {drink.get_items()}")
    if choice == "off":
        turned_on = False
    elif choice == "report":
        print(functionality.report())
        print(payment.report())
    else:
        chosen_drink = drink.find_drink(choice)
        if functionality.is_resource_sufficient(chosen_drink):
            if payment.make_payment(chosen_drink.cost):
                functionality.make_coffee(chosen_drink)



