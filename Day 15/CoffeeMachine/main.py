from menu import MENU, resources


money = [0]

water = [resources["water"]]
milk = [resources["milk"]]
coffee = [resources["coffee"]]


def format_report():
    print(f"Water: {water[0]}ml\nMilk: {milk[0]}ml\nCoffee: {coffee[0]}g\nMoney: ${money[0]}\n")


def check_resources_espresso(ingredients):
    if ingredients["ingredients"]["water"] < water[0]:
        if ingredients["ingredients"]["coffee"] < coffee[0]:
            water[0] -= ingredients["ingredients"]["water"]
            coffee[0] -= ingredients["ingredients"]["coffee"]
            return True, water, coffee
        else:
            print("Sorry there is not enough coffee.")
            return False

    else:
        print("Sorry there is not enough water.")
        return False


def check_resources(ingredients):
    if ingredients["ingredients"]["water"] <= water[0]:
        if ingredients["ingredients"]["coffee"] <= coffee[0]:
            if ingredients["ingredients"]["milk"] <= milk[0]:
                return True, water, milk, coffee
            else:
                print("Sorry there not enough milk")
                return False
        else:
            print("Sorry there is not enough coffee.")
            return False

    else:
        print("Sorry there is not enough water.")
        return False


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    return total


def process(choice_user):
    if choice_user == "espresso":
        if check_resources_espresso(MENU[choice_user]):
            total = round(process_coins(), 2)

            if total > MENU[choice_user]["cost"]:
                money[0] += MENU[choice_user]["cost"]
                money_back = total - MENU[choice_user]["cost"]
                print(f"Here is ${money_back} back in change.")
                make_coffee(MENU[choice_user])
                print(f"Here is your {choice_user} ☕. Enjoy!")

            else:
                print(f"You don't have enough money, here is your money back ${total}")
    else:
        if check_resources(MENU[choice_user]):
            total = round(process_coins(), 2)
            if total > MENU[choice_user]["cost"]:
                money[0] += MENU[choice_user]["cost"]
                money_back = total - MENU[choice_user]["cost"]
                print(f"Here is ${money_back} back in change.")
                make_coffee(MENU[choice_user])
                print(f"Here is your {choice_user} ☕. Enjoy!")
            else:
                print(f"You don't have enough money, here is your money back ${total}")


def make_coffee(ingredients):
    water[0] -= ingredients["ingredients"]["water"]
    milk[0] -= ingredients["ingredients"]["milk"]
    coffee[0] -= ingredients["ingredients"]["coffee"]


turn_off = False


while not turn_off:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        turn_off = True
    elif choice == "report":
        format_report()
    else:
        process(choice)
