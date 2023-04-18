# write a python code to create a caesar cipher program
# the program should ask the user to enter a message
# the program should ask the user to enter a key
# the program should encrypt the message using the key
# the program should decrypt the message using the key

# let's organize the code in functions; namely the encode, decode, and main functions

def encode(message, key):
    encrypted_message = ""
    for letter in message:
        encrypted_message += chr(ord(letter) + key)
    return encrypted_message

def decode(message, key):
    decrypted_message = ""
    for letter in message:
        decrypted_message += chr(ord(letter) - key)
    return decrypted_message

def main():
    # step 1: ask the user to enter a message
    message = input("Enter a message: ").lower()

    # step 2: ask the user to enter a key
    key = int(input("Enter a key: "))

    # step 3: encrypt the message using the key
    encrypted_message = encode(message, key)

    # step 4: print the encrypted message
    print("Encrypted message: ", encrypted_message)

    # step 5: print the decrypted message
    # ask the user to enter a key, and then decrypt the message using the key
    inp_key = int(input("Enter a key to decrypt the message: "))
    decrypted_message = decode(encrypted_message, inp_key)

    # step 6: print the decrypted message
    print("Decrypted message: ", decrypted_message)

# call the main function   
if __name__ == "__main__":
    main()

