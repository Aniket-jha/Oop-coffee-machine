from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# menu_item=MenuItem()
menu_of_coffee=Menu()
making_coffee=CoffeeMaker()
machine_with_money=MoneyMachine()


is_on = True


while is_on :
    options = menu_of_coffee.get_items()
    name_of_coffee = input(f"Which type of coffee do you want ({options}): \n").lower()
    if name_of_coffee=="off":
        is_on=False
    elif name_of_coffee == "report":
        making_coffee.report()
        machine_with_money.report()
    else :
        drink=menu_of_coffee.find_drink(name_of_coffee)
        if making_coffee.is_resource_sufficient(drink) and machine_with_money.make_payment(drink.cost):
            making_coffee.make_coffee(drink)

