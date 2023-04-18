# write a function to calculate the love score given the names of the two lovers
# Hints:
# 1. The first digit of love score is the number of times the letters in the word TRUE occurs in both strings.
# 2. The second digit of love score is the number of times the letters in the word LOVE occurs in both strings.
# 3. The love score is the concatenation of the first and the second digits.

def love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    
    true_count = 0
    love_count = 0
    
    for letter in "true":
        true_count += name1.count(letter) + name2.count(letter)
        
    for letter in "love":
        love_count += name1.count(letter) + name2.count(letter)
        
    love_score = int(str(true_count) + str(love_count))
    
    if love_score < 10 or love_score > 90:
        print(f"Your love score is {love_score}, you go together like coke and mentos.")
    elif love_score >= 40 and love_score <= 50:
        print(f"Your love score is {love_score}, you are alright together.")
    else:
        print(f"Your love score is {love_score}")

# test cases
love_score("Angela", "Jack")
love_score("Karl", "Anna")

