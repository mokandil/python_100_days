# write a program that generates a random number between 1 and 100 and lets the user guess what number was generated. 
# The computer calculates the error and gives the user a hint.
# the programe should end when the user guesses the correct number or hits the maximum number of guesses.

import random
import os

# generate a random number between 1 and 100
def generate_number():
    return random.randint(1, 100)

# get the user's guess
def get_guess():
    return int(input("Enter your guess: "))

# check guess and calculate error
def check_guess(guess, number):

    error = (guess - number) / number * 100
    return error

# create the main function
def main():
    
    # clear the screen
    os.system("cls")

    # generate a random number
    number = generate_number()

    # set the maximum number of guesses
    max_guesses = 5

    # set the number of guesses to 0
    nr_guesses = 0

    # set the game over flag to false
    game_over = False

    # while the game is not over
    while not game_over:

        # get the user's guess
        guess = get_guess()

        # check the guess
        error = check_guess(guess, number)

        # increment the number of guesses
        nr_guesses += 1

        # check if the user guessed the number
        if error == 0:
            print("You guessed the number!")
            game_over = True

        # check if the user has reached the maximum number of guesses
        elif nr_guesses == max_guesses:
            print("You have reached the maximum number of guesses.")
            game_over = True

        # give the user a hint
        else:
            if error > 0:
                print("You are too high.", f"You have {max_guesses - nr_guesses} attempts left.")
            else:
                print("You are too low.", f"You have {max_guesses - nr_guesses} attempts left.")

    # print the correct number
    print("The correct number was: ", number)

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        main()

# call the main function
if __name__ == "__main__":
    main()
