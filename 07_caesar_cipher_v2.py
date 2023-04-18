# write a python program that asks the user to enter a message
# and then asks him/her to enter a key
# finally, ask the user if he/she wants to encrypt or decrypt the message

"""
solution steps:
create two functions; 
one to encode or decode a message given a key and direction
the other function is the main function
"""

import os


def caeser_cipher(message, key, direction):
    """
    this function encodes or decodes a message given a key and direction
    """
    # first we need to handle the key limitations to avoid errors
    key = key % 10 + 1

    encoded_message = ""
    if direction == "encrypt":
        for letter in message:
            encoded_message += chr(ord(letter) + key)
    else:
        for letter in message:
            encoded_message += chr(ord(letter) - key)

    return encoded_message


def main():

    # step 1: ask the user to enter a message
    message = input("Enter a message: ").lower()

    # step 2: ask the user to enter a key
    key = int(input("Enter a key: "))

    # step 3: ask the user if he/she wants to encrypt or decrypt the message
    direction = input("Do you want to encrypt or decrypt the message? ").lower()

    # step 4: encode or decode the message
    encoded_message = caeser_cipher(message, key, direction)

    # step 5: print the encoded or decoded message
    print(f"The {direction}d message is: {encoded_message}")

    # step 6: ask the user if he/she wants to continue
    response = input("Do you want to continue? (y/n) ").lower()
    
    if response == "y":
        os.system("cls")
        main()
    else:
        print("Goodbye!")


# call the main function
if __name__ == "__main__":
    os.system("cls")
    main()