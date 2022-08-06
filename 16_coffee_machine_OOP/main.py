from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine=CoffeeMaker()
menu=Menu()
money=MoneyMachine()

def process():
    options=menu.get_items()
    order=input(f"What would you like? ({options}):").lower()
    match order:
        case "espresso"|"latte"|"cappuccino":
                drink=menu.find_drink(order)
                if machine.is_resource_sufficient(drink):
                    if money.make_payment(drink.cost):
                        machine.make_coffee(drink)
                    
                process()
        case "report":
            machine.report()
            money.report()
            process()
        case "off":
            pass
        case _:
            process()
    

process()

