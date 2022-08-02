from curses.ascii import isdigit


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0

#   Print report
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

#   Promt (Step 1)
def promt():
    str=input("What would you like? (espresso/latte/cappuccino): ").lower()
    match str.lower():
        case 'report':
            report()
            coffeemachine()
        case 'espresso' | 'latte' | 'cappuccino':
            if count(str):
                qu=di=ni=pe=""
                sum=change=0
                while not qu.isdigit() or not di.isdigit() or not ni.isdigit() or not pe.isdigit():
                    print("Please insert coins.")
                    qu=input("How many quarters?: ")
                    di=input("How many dimes?: ")
                    ni=input("How many nickels?: ")
                    pe=input("How many pennies?: ")
                    
                sum=int(qu)*0.25+int(di)*0.10+int(ni)*0.05+int(pe)*0.01
                cost=MENU[f"{str}"]["cost"]
                if sum>=cost:
                    change=sum-cost
                    change=round(change, 2)
                    make(str)
                    print(f"Here is ${change} dollars in change.")
                    coffeemachine()
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    coffeemachine()
            else: 
                coffeemachine()
        case 'off':
            return
        case _:
            print("Unclear input!")
            coffeemachine()


#   Deducting resources (making coffee)
def make(coffee):
    global money
    resources["water"]-=MENU[f"{coffee}"]["ingredients"]["water"]
    resources["coffee"]-=MENU[f"{coffee}"]["ingredients"]["coffee"]
    if coffee!="espresso":
        resources["milk"]-=MENU[f"{coffee}"]["ingredients"]["milk"]
    money+=MENU[f"{coffee}"]["cost"]
    print(f"Here is your {coffee}. Enjoy!")


#   Checking sufficiency of resources
def count(coffee):
    res_w=MENU[f"{coffee}"]["ingredients"]["water"]
    res_c=MENU[f"{coffee}"]["ingredients"]["coffee"]
    
    if coffee!="espresso":
        res_m=MENU[f"{coffee}"]["ingredients"]["milk"]
    else:
        res_m=0
    if resources['water']>=res_w and resources['milk']>=res_m and resources['coffee']>=res_c:
        return True
    else:
        no_res=""
        if res_w<=resources['water']: no_res = "water"
        if res_m<=resources['milk']: no_res = "milk"
        if res_c<=resources['coffee']: no_res = "coffee"
        print(f"Sorry there is not enough {no_res}.")
        return False

def coffeemachine():
    promt()
    
coffeemachine()











