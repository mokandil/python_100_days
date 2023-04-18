# re-writing the coffee machine program using OOP

import os

# coffee machine class
class CoffeeMachine:

    def __init__(self):
        self.quarters = 0.25
        self.dimes = 0.10
        self.nickles = 0.05
        self.pennies = 0.01

        self.menue = {"espresso": {"water": 50, "milk": 0, "coffee": 18, "sugar": 10,"cost": 1.5},
                    "latte": {"water": 200, "milk": 150, "coffee": 24, "sugar": 30,"cost": 2.5},
                    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "sugar": 20, "cost": 3.0},
                    "americano": {"water": 200, "milk": 0, "coffee": 24, "sugar": 30, "cost": 2.5},
                    "mocha": {"water": 200, "milk": 100, "coffee": 24, "sugar": 20, "cost": 3.0},
                    "macchiato": {"water": 200, "milk": 100, "coffee": 24, "sugar": 25, "cost": 3.0}
        }

        self.resources = {"water": 600,
                        "milk": 600,
                        "coffee": 600,
                        "sugar": 300}
        
        self.choices = {
            "1": "espresso",
            "2": "latte",
            "3": "cappuccino",
            "4": "americano",
            "5": "mocha",
            "6": "macchiato",
            "7": "report",
            "8": "off"
        }

    def check_resources(self, drink):
        """checks if there is enough resources to make the drink"""
        for item in self.resources:
            if self.resources[item] < self.menue[drink][item]:
                print(f"Sorry there is not enough {item} to make {drink}")
                return False
        return True
    

    def check_coins(self, drink):
        """checks if there is enough money to make the drink"""
        print("Please insert coins.")
        quarters = int(input("how many quarters?: ")) * self.quarters
        dimes = int(input("how many dimes?: ")) * self.dimes
        nickles = int(input("how many nickles?: ")) * self.nickles
        pennies = int(input("how many pennies?: ")) * self.pennies
        total = quarters + dimes + nickles + pennies

        if total >= self.menue[drink]["cost"]:
            change = round(total - self.menue[drink]["cost"], 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
    
    
    def make_coffee(self, drink):
        """makes the coffee"""
        for item in self.resources:
            self.resources[item] -= self.menue[drink][item]
        print(f"Here is your {drink} ☕ Enjoy!")

    
    def report(self):
        """prints the report"""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Sugar: {self.resources['sugar']}g")

    
    def off(self):
        """turns off the machine"""
        print("Machine is now off.")
        exit()
    

    def order_again(self):
        """asks the user if they want to order another drink"""
        choice = input("Would you like to order another drink? (y/n): ")
        if choice == "y":
            return True
        else:
            return False
    

    def display_menue(self):
        """displays the menue"""
        print("What would you like? (espresso/latte/cappuccino/americano/mocha/macchiato): ")
        for i, drink in self.choices.items():
            print(f"{i}. {drink}")
    

    def run(self):
        """runs the coffee machine"""
        os.system("cls")

        while True:
            self.display_menue()
            choice = input("Enter your choice: ")
            
            if choice in self.choices:
                drink = self.choices[choice]

                if choice == "7":
                    self.report()
                    if self.order_again():
                        continue
                    else:
                        break

                elif choice == "8":
                    self.off()

                else:
                    if self.check_resources(drink):
                        if self.check_coins(drink):
                            self.make_coffee(drink)
                            if self.order_again():
                                continue
                            else:
                                break
            else:
                print("Invalid choice. Try again.")
                continue


# main
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()