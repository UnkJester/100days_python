INGREDIENTS = 'ingredients'
MENU = {
    "espresso": {
        INGREDIENTS: {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        INGREDIENTS: {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        INGREDIENTS: {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def print_resources(money):
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money: ${'{:0,.2f}'.format(money)}")

def check_resources(choice):
    global INGREDIENTS
    drink = MENU.get(choice).get(INGREDIENTS)
    for key in drink:
        if resources[key] < drink[key]:
            return key
    return None
def get_price(choice):
    return MENU.get(choice).get('cost')

def make_drink(choice):
    global INGREDIENTS
    drink = MENU.get(choice).get(INGREDIENTS)
    for key in drink:
        resources[key] -= drink[key]
    print(f'Here is your {choice} ☕ Enjoy!')