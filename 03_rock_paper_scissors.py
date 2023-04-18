# a simple Rock, Paper, and Scissors Game
# Instrunctions:
# The program should do the following:
# Ask the user to select a number which represents the choice of rock, paper, or scissors.
# The computer should randomly select a number which represents the choice of rock, paper, or scissors.
# The program should compare the user's choice and the computer's choice and determine the winner.
# The program should print the results using Ascii art.
# The program should ask the user if they want to play again otherwise the program should end.


import random
import os

def object_to_shape(object):
    if object == 1:
        print(
            """
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)

            """
        )

    elif object == 2:
        print (

            """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
           
            """
        )
    elif object == 3:
        print (
            """           
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

            """
        )
    else:
        print("Invalid choice!")



def main():
    # 1. Ask the user to select a number which represents the choice of rock, paper, or scissors.
    print("Welcome to Rock, Paper, Scissors!")
    print("Please select a number from the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = int(input("Your choice: "))

    # 2. The computer should randomly select a number which represents the choice of rock, paper, or scissors.
    computer_choice = random.randint(1, 3)
    object_to_shape(user_choice)
    
    # 3. The program should print the selection of the user and the computer.
    # print("You chose: " + str(user_choice))
    print("The computer chose: " + str(computer_choice))
    object_to_shape(computer_choice)

    # 4. The program should compare the user's choice and the computer's choice and determine the winner.
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif user_choice == 1 and computer_choice == 3:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 2 and computer_choice == 3:
        print("You lose!")
    elif user_choice == 3 and computer_choice == 1:
        print("You lose!")
    elif user_choice == 3 and computer_choice == 2:
        print("You win!")
    else:
        print("Invalid choice!")
        
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == "y":
        # clear the screen and start the game again
        os.system("cls")
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

