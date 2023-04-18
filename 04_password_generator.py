# create a simple password generator using python
# the programe will ask the user how many letters, symbols and numbers they want in their password
# then it will generate a password for them

import random

# create a list of letters, numbers and symbols
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()_+"

# ask the user how many letters, symbols and numbers they want in their password
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))

# create a list to store the password
password = []

# add the letters, symbols and numbers to the password list
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

# shuffle the password list
random.shuffle(password)

# create a string from the password list
password = "".join(password)

# print the password
print(f"Your password is: {password}")
print("\n\n\n")