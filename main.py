MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO-1 : PRINT A REPORT
# TODO-2 : CHECK RESOURCES SUFFICIENT
# TODO-3 : PROCESS COINS
# TODO-4 : CHECK TRANSACTION SUCCESSFUL?
# TODO-5 : MAKE COFFEE
def is_resource_sufficient(order_ingredients):
    """Returns True when the resource is sufficient, False otherwise."""
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            return False
    return True
def is_transaction_sufficient(money_received, drink_cost):

    """Return drink if the money is sufficient and return false if the money is not sufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}$ in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry! That's not enough money !")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is you {drink_name} ")
def process_coins():
    """Returns the total amount of money"""
    print("Insert some coins: ")
    total = int(input("Number of Quarters? )"))* 0.25
    total += int(input("Number of dimes "))*0.1
    total += int(input("Number of Nickels? "))*0.05
    total += int(input("Number of Penny? "))*0.01
    return total
is_on = True

while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sufficient(payment, drink["cost"]):
                make_coffee(choice ,drink["ingredients"])
