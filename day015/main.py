from art import splash
from coffee import MENU, print_resources
OFF = 'off'
REPORT = 'report'
# print splashscreen
splash()
finished = False
while not finished:
    # Prompt Choice
    resp = input(f"What would you like? ({'/'.join(MENU.keys())}): ").lower()
    if resp in MENU.keys():
        print(f"{resp} it is!")
        # TODO start brewing coffee
    # Turn off if 'off' received
    elif resp == OFF:
        print("Turning the coffee maker off. Have a great day!")
        finished = True
        continue
    # Print report if 'report'
    elif resp == REPORT:
        print("Printing report... brrrrrrr")
        #TODO: store money in coin.py and grab amount and insert instead
        print_resources(0)
        # TODO: Print report if 'report'
