from art import logo
import random
from replit import clear


# logo, start
clear()
print(logo)
print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')

# generate random nuber
random_number = random.randint(1,100)

# for testing
print(f"Pssst, the correct answer is {random_number}")

# Choose a difficulty
while True:
    difficulty = input("Choose a difficulty.\nType 1: for easy\nType 2: hard\n")
    # easy
    if difficulty == "1":
        attempt = 10
        break
    # hard
    if difficulty == "2":
        attempt = 5
        break
    
while True:

    if attempt == 0:
        print("You've run out of guesses, you lose.")
        break
    
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        break
        
    elif guess > random_number:
        print("Too high.")
        attempt -= 1

    elif guess < random_number:
        print("Too low.")
        attempt -= 1

