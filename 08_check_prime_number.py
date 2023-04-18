# write a python code to check if a number is prime or not
"""
Note: A prime number is a number that is only divisible by 1 and itself.

Pseudocode: 
1. Ask the user to enter a number
2. Check if the number is divisible by any number between 2 and the number itself
3. If the number is divisible by any number between 2 and the number itself, then the number is not prime, 
otherwise the number is prime           
"""

# step 1: ask the user to enter a number
num = int(input("Enter a number: "))

# create a function to check if a number is prime or not
def is_prime(num):

    # check if the number is divisible by any number between 2 and the number itself
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # print the result
    if is_prime:
        print(f"The number {num} is prime")
    else:
        print(f"The number {num} is not prime")

# call the function
is_prime(num)