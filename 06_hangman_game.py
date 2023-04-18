# write a python code to create a hangman game
# Description of the game:
# 1. The computer will randomly choose a word from a list of words
# 2. The player will have to guess the word
# 3. The player will have 6 chances to guess the word
# 4. If the player guesses the word correctly, the player wins
# 5. If the player does not guess the word correctly, the player loses
# 6. The player can only guess one letter at a time

# import the random module
import random
import os
import time

def hangman_game():
        
    # create a list of words
    list_of_words = ["apple", "banana", "orange", "grapes", "mango", "watermelon", "pineapple", "strawberry", 
                    "blueberry", "kiwi", "pear", "peach", "cherry", "lemon", "lime", "coconut", "avocado", "papaya", "melon", "plum", "apricot", 
                    "fig", "pomegranate", "guava", "jackfruit", "tomato", "potato", "onion", "garlic", "ginger", "cucumber", "carrot", "broccoli", 
                    "cauliflower", "spinach", "cabbage", "peas", "beans", "corn", "rice", "wheat", "barley", "oats", "sugar", "salt", "pepper", "chilli", 
                    "turmeric", "cumin", "coriander", "mustard", "saffron", "vanilla", "cinnamon", "nutmeg", "cloves", "ginger", "chocolate", "coffee", "tea", 
                    "milk", "butter", "cheese", "yogurt", "cream", "egg", "meat", "fish", "pork", "beef", "chicken", "turkey", "duck", "goose", "lamb", "salmon", 
                    "tuna", "shrimp", "lobster", "crab", "oyster", "clam", "snail", "rabbit", "deer", "horse", "cow", "sheep", "goat", "pig", "elephant", "lion", 
                    "tiger", "leopard", "cheetah", "jaguar", "panther", "bear", "wolf", "fox", "dog", "cat", "mouse", "rat", "rabbit", "hamster", "squirrel", 
                    "chipmunk", "beaver", "kangaroo", "koala", "panda", "penguin", "seal", "whale", "dolphin", "shark", "crocodile", "snake", "lizard", "frog", 
                    "toad", "turtle", "ant", "bee", "butterfly", 
                    "dragonfly", "grasshopper", "ladybug", "mosquito", "spider", "worm", "cricket", "dove", "duck", "eagle", 
                    "owl", "parrot", "pigeon", "robin", "sparrow", "swan", "bat", "camel", "cat", "chimpanzee", "cow", "dog",
                    "dolphin", "elephant", "frog", "giraffe", "goat", "hamster", "horse", "kangaroo", "leopard", "lion", 
                    "monkey", "octopus", "owl", "panda", "pig", "rabbit", "rat", "scorpion", "seal", "shark", "sheep", 
                    "snail", "snake", "spider", "squirrel", "tiger", "turtle", "wolf", "zebra", "airplane", "ambulance", 
                    "bicycle", "bus", "car", "helicopter", "motorcycle", "ship", "submarine", "train", "truck", "aircraft", 
                    "balloon", "canoe", "cruise ship", "ferry", "hot air balloon", "jet", "lifeboat", "raft", "rocket", 
                    "sailboat", "schooner", "scooter", "sled", "space shuttle", "submarine", "tank", "tugboat", "yacht", 
                    "air", "earth", "fire", "water", "wind", "cloud", "fog", "rain", "snow", "storm", "sun", "thunder", 
                    "tornado", "volcano", "wave", "bridge", "castle", "cave", "church", "city", "house", "lighthouse", 
                    "palace", "pyramid", "school", "skyscraper", "temple", "treehouse", "waterfall", "windmill", "bed", 
                    "chair", "couch", "desk", "lamp", "mirror", "nightstand", "pillow", "sofa", "table", "toilet", "window", 
                    "alarm clock", "camera", "computer", "game console", "headphones", "laptop", "microphone", "mobile phone",
                    "mouse", "printer", "remote control", "television", "video camera", "book", "envelope", "map", 
                    "newspaper", "paint", "paper", "pencil", "picture", "poster", "scissors", "stamps", "stapler", "tape"]


    # create a function to check if the guessed character is in the word
    def check_char_in_word(hidden_word, guessed_word, guessed_char):
        for i in range(len(hidden_word)):
            if hidden_word[i] == guessed_char:
                guessed_word[i] = guessed_char
        return guessed_word

    # randomly choose a word from the list of words
    hidden_word = random.choice(list_of_words)
    # create a list of underscores to represent the word to be guessed
    guessed_word = ["_"] * len(hidden_word)

    # create a variable to keep track of the number of guesses
    nr_of_guesses = 6
    game_over = False

    # create a loop to keep the game running
    while nr_of_guesses > 0:
        os.system("cls")
        print(" ".join(guessed_word))
        print("\n\nYou have {} guesses left\n\n".format(nr_of_guesses))

        # ask the user to guess a character
        guessed_char = input("Guess a character: ")
        if guessed_char in hidden_word:
            guessed_word = check_char_in_word(hidden_word, guessed_word, guessed_char)

        else:
            nr_of_guesses -= 1

            # Alaram the user that they have guessed the wrong character 
            os.system("cls")
            print("Wrong guess!!! You have {} guesses left".format(nr_of_guesses))
            time.sleep(1)

        # check if the user has guessed the word
        if "_" not in guessed_word:
            print(f"You won. The word was {hidden_word}")
            game_over = True

        # check if the user has run out of guesses
        if nr_of_guesses == 0:
            print(f"You lost. The word was {hidden_word}")
            game_over = True

        # check if the game is over
        if game_over:
            # ask the user if they want to play again
            play_again = input("Do you want to play again? (y/n): ")
            # if the user wants to play again, call the hangman game function
            if play_again == "y":
                hangman_game()
            # if the user doesn't want to play again, break out of the while loop
            else:
                print("Thank you for playing the game")
                break



# create a main function to run the program
def main():
    # clear the screen
    os.system("cls")
    # call the hangman game function
    hangman_game()

# call the main function
if __name__ == "__main__":
    main()