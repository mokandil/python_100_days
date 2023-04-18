# create a simple blackjack game with a single player.py and a dealer
# the player.py can choose to hit or stand
# instrunctions:
# the player.py is dealt two cards
# the dealer is dealt two cards
# the player.py can see one of the dealer's cards
# the player.py can choose to hit or stand
# if the player.py hits, they are dealt another card
# if the player.py stands, the dealer's turn begins
# the dealer must hit until their cards add up to 17
# if the dealer goes over 21, the player.py wins
# if the dealer gets 21, the dealer wins
# if the player.py gets 21, the player.py wins
# if the player.py gets more than the dealer without going over 21, the player.py wins


# import libraries
import random
import os
from logo import logo
import time

# create a deck of cards
def create_deck():
    # create a list of cards
    cards_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # duplicate the list 4 times
    cards_deck = cards_deck * 4
    # return the deck
    return cards_deck


# create a function to deal cards
def deal_cards(cards_deck):
    # shuffle the deck
    random.shuffle(cards_deck)
    # deal the first two cards to the player.py
    player_cards = [cards_deck.pop(), cards_deck.pop()]
    # deal the first two cards to the dealer
    dealer_cards = [cards_deck.pop(), cards_deck.pop()]
    # return both hands
    return player_cards, dealer_cards


# create a function to calculate the score of a hand
def calculate_score(cards):
    # create a temporary list of cards to filter out the Aces
    temp_cards = [card for card in cards if card != 'A']

    # calculate the score of the hand before the Aces
    score = sum([10 if card in ['J', 'Q', 'K'] else int(card) for card in temp_cards])

    # calculate the score of the hand after the Aces
    if cards.count('A') >= 2:
        if score <= 9:
            score += 12
        else:
            score += 2

    elif cards.count('A') == 1:
        if score <= 10:
            score += 11
        else:
            score += 1
    
    return score


# create a function to check for a blackjack
def is_blackjack(cards):
    if len(cards) == 2:
        if 'A' in cards and (True if 'Q' in cards or 'J' in cards or 'K' in cards or '10' in cards else False):
            return True
        
        return False
          
    else:
        return False


# create a function to handle the hit action
def hit(cards_deck, cards):
    random.shuffle(cards_deck)
    cards.append(cards_deck.pop())
    return cards

# create a function to handle the stand action
def stand(cards):
    return cards


# create a function to handle the player.py's turn
def player_turn(cards_deck, player_cards, action):
    # hit == h and stand == s
    
    if action == "h":
        player_cards = hit(cards_deck, player_cards)

    elif action == "s":
        player_cards = stand(player_cards)

    else:
        print("Invalid action")
    
    return player_cards



# create a function to handle the dealer's turn
def dealer_turn(cards_deck, dealer_cards):
    
    score = calculate_score(dealer_cards)

    while score < 17:
        dealer_cards = hit(cards_deck, dealer_cards)
        score = calculate_score(dealer_cards)
    
    return dealer_cards



# create a function to check the end of the game
def is_gameover(player_cards, dealer_cards, first_turn = False):

    """the functions returns a tuple with three values:
    is_gameover, is_blackjack, winner
    winner can be "Player", "Dealer", "Tie, or None
    """
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    if is_blackjack(player_cards):
        return True, True, "Player"

    elif is_blackjack(dealer_cards):
        return True, True, "Dealer"
    
    elif player_score > 21:
        return True, False, "Dealer"

    elif dealer_score > 21:
        return True, False, "Player"
    
    elif first_turn:
        return False, False, None

    elif dealer_score >= 17:
        if player_score > dealer_score:
            return True, False, "Player"
        
        elif player_score < dealer_score:
            return True, False, "Dealer"
        
        else:
            return True, False, "Tie"

    else:
        return False, False, None


# create a function to display the cards and the score of the player.py and the dealer
def display_cards(player_cards, dealer_cards, *args):
    os.system('cls')
    # format the displayed cards and the score to be printed
    print(f"Player's cards: {str(player_cards):>25} \t- Score: {calculate_score(player_cards)}")
    print(f"Dealer's cards: {str(dealer_cards):>25} \t- Score: {calculate_score(dealer_cards)}")

    if args:
        is_gameover, is_blackjack, winner = args

        if is_gameover:

            if is_blackjack:
                print("Blackjack! {} wins!".format(winner))

            elif winner == "Tie":
                print("It's a tie!")

            else:
                print("{} wins!".format(winner))



# create the main function
def main():
    
    # clear the terminal
    os.system('cls')

    # print the logo
    print(logo)
    time.sleep(2)

    # create a deck of cards
    cards_deck = create_deck()

    # deal the cards
    player_cards, dealer_cards = deal_cards(cards_deck)

    # flag to check if it's the first turn
    first_turn = True

    # display the cards and the score of the player.py and the dealer
    display_cards(player_cards, dealer_cards[:-1])

    # check if the game is over
    gameover, is_blackjack, winner = is_gameover(player_cards, dealer_cards[:-1], first_turn)

    # if the game is not over, continue the game
    while not gameover:

        # ask the player.py to hit or stand, h = hit, s = stand
        action = input("Do you want to hit or stand? (h/s) ")
        
        # handle the player.py's turn
        player_cards = player_turn(cards_deck, player_cards, action)
        first_turn = False

        # check if the game is over
        gameover, is_blackjack, winner = is_gameover(player_cards, dealer_cards[:-1])

        # handle the dealer's turn
        if not gameover and action == "s":
            dealer_cards = dealer_turn(cards_deck, dealer_cards)

            # check if the game is over
            gameover, is_blackjack, winner = is_gameover(player_cards, dealer_cards)

        # display the cards and the score of the player.py and the dealer
        args = (gameover, is_blackjack, winner)
        display_cards(player_cards, dealer_cards[:-1], *args)


    # display the cards and the score of the player.py and the dealer
    args = (gameover, is_blackjack, winner)
    display_cards(player_cards, dealer_cards, *args)

    # ask the player.py if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == 'y':
        main()



# call the main function
if __name__ == '__main__':
    main()

