# create a python program that simulates a coffee machine
# the program should ask the user what they would like to order from a menu
# the program should check if there is enough resources to make the drink
# the program should then ask the user to insert coins
# the program should check if the user has inserted enough coins
# the program should print a report of the resources left in the machine when the user types "report"
# the program should ask the user if they would like to order another drink
# the program should stop when the user types "off"

import os

# coins
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


# menue
menue = {"espresso": {"water": 50, "milk": 0, "coffee": 18, "sugar": 10,"cost": 1.5},
        "latte": {"water": 200, "milk": 150, "coffee": 24, "sugar": 30,"cost": 2.5},
        "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "sugar": 20, "cost": 3.0},
        "americano": {"water": 200, "milk": 0, "coffee": 24, "sugar": 30, "cost": 2.5},
        "mocha": {"water": 200, "milk": 100, "coffee": 24, "sugar": 20, "cost": 3.0},
        "macchiato": {"water": 200, "milk": 100, "coffee": 24, "sugar": 25, "cost": 3.0}
}

# resources
resources = {"water": 600, 
             "milk": 600, 
             "coffee": 600, 
             "sugar": 300}


# dicttionary to map options to numbers
choices = {
    "1": "espresso",
    "2": "latte",
    "3": "cappuccino",
    "4": "americano",
    "5": "mocha",
    "6": "macchiato",
    "7": "report",
    "8": "off"
}


# function to check if there is enough resources to make the drink
def check_resources(drink):

    if resources["water"] < menue[drink]["water"]:
        print("Sorry there is not enough water.")
        return False
    
    elif resources["milk"] < menue[drink]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    
    elif resources["coffee"] < menue[drink]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    
    elif resources["sugar"] < menue[drink]["sugar"]:
        print("Sorry there is not enough sugar.")
        return False
    
    else:
        return True


# function to check if the user has inserted enough coins
def check_coins(drink):
    print("Please insert coins.")
    quarters_inserted = int(input("How many quarters?: "))
    dimes_inserted = int(input("How many dimes?: "))
    nickles_inserted = int(input("How many nickles?: "))
    pennies_inserted = int(input("How many pennies?: "))

    total_coins = quarters_inserted * quarters + dimes_inserted * dimes + nickles_inserted * nickles + pennies_inserted * pennies

    if total_coins >= menue[drink]["cost"]:
        change = round(total_coins - menue[drink]["cost"], 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# function to make the drink
def make_drink(drink):
    global resources

    res = resources
    res["water"] -= menue[drink]["water"]
    res["milk"] -= menue[drink]["milk"]
    res["coffee"] -= menue[drink]["coffee"]
    res["sugar"] -= menue[drink]["sugar"]

    print(f"Here is your {drink}. Enjoy!")


# function to print a report of the resources left in the machine
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Sugar: {resources['sugar']}g")


# function to ask the user if they would like to order another drink
def order_again():
    order_again = input("Would you like to order another drink? (y/n): ")
    if order_again == "y":
        return True
    else:
        return False
    

# function to process the order
def order_drink(drink):
    if check_resources(drink):
        if check_coins(drink):
            make_drink(drink)
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
        

# create a function to diplay the menue with prices
def print_menue():
    print("Welcome to the Coffee Machine!")
    print("What would you like to order from the menue?")
    for i, drink in enumerate(menue, start=1):
        print(f"{i}. {drink} - ${menue[drink]['cost']}")
    print("7. Report")
    print("8. Off")


# main function
def main():
    os. system("cls")

    # print menue
    print_menue()

    # ask user for input
    choice = input("Please enter your choice: ")

    # check if the user wants to order a drink
    if choice in choices:
        if choice == "7":
            print_report()
            if order_again():
                main()
            else:
                return
        elif choice == "8":
            return
        else:
            order_drink(choices[choice])
            if order_again():
                main()
            else:
                return

# call main function
if __name__ == "__main__":
    main()

# end of program