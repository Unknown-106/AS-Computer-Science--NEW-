# Guessing Game
# Azhi Amin
# 04/9/2026
# OCR AS Computer Science

import random

#generate random number to try and guess
number = random.randint(1,20)

#Executes the procedures in sequence
def Guessing_Game():
    print("Welcome to the Guessing Game!\n")
    guess = -1
    attempts = 0
    while guess != number and attempts < 6:
        attempts += 1
        guess = int(input("Guess my number (between 1-20): "))
        HigherOrLower(guess,attempts)

#The core logic that gives the user feedback on their guess, whether their guess was higher or lower than the target number
def HigherOrLower(guess,attempts):
    try:
        if attempts >= 6:
            result(guess)
        elif guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
    except Exception as e:
        print("Error occurred:",e)

#Determines whether the user won or lost the game and outputs their result.
def result(guess):
    try:
        if guess == number:
            print("You Win!")
        else:
            print("You Lose!")
        print(f"My number was {number}.")
    except Exception as e:
        print("Error occured:",e)

#Execute
def main():
    try:
        Guessing_Game()
    except Exception as e:
        print("Error occurred:",e)

#program starts here
if (__name__ == "__main__"):
    main()

