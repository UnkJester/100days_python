from art import splash
from coffee import MENU, print_resources, check_resources, get_price, make_drink
from coin import receive_coins, store_profit, get_profit
OFF = 'off'
REPORT = 'report'
# print splashscreen
splash()
finished = False
while not finished:
    # Prompt Choice
    resp = input(f"What would you like? ({'/'.join(MENU.keys())}): ").lower()
    if resp in MENU.keys():
        print(f"{resp.title()} it is!")
        # Check if have enough resources
        not_enough = check_resources(resp)
        if check_resources(resp) is not None:
            print(f"Sorry there is not enough {not_enough}")
            continue
        # if there are enough resources. accept payment
        money_received = receive_coins()
        if money_received < get_price(resp):
            print(f"Sorry that's not enough money. Money refunded.")
            continue
        # insert into register
        store_profit(get_price(resp))
        # if there is enough money, give back change and make the drink
        make_drink(resp)
        print(f"Here is ${'{:0,.2f}'.format(money_received - get_price(resp))} in change.")
    elif resp == OFF:
        # Turn off if 'off' received
        print("Turning the coffee maker off. Have a great day!")
        finished = True
        continue
    elif resp == REPORT:
        # Print report if 'report'
        print("Printing report... brrrrrrr")
        print_resources(get_profit())
