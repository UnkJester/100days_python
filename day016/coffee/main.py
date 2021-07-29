from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
off = False
while not off:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        off = True
    elif choice == 'report':
        maker.report()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                maker.make_coffee(drink)