COINS = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter':0.25
}
profit = 0

def receive_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * .1 + nickels * .05 + pennies * .01

def store_profit(income):
    global profit
    profit += income

def get_profit():
    return profit