# HeadsOrTails
# Azhi Amin
# 28/09/2026
# OCR AS Computer Science

import random


# Calculates the result of the coin flip and returns as string: "Heads" or "Tails".
def coinFlip():
    try:
        answer = random.randint(0, 1)
        match answer:
            case 0:
                return "Heads"
            case 1:
                return "Tails"
    except Exception as e:
        print("Error occurred:", e)


# User guesses "Heads" or "Tails".
def userGuess():
    try:
        return input("Heads or Tails? ")
    except Exception as e:
        print("Error occurred:", e)


# Determines whether or not the guess matches the answer and outputs if the user was right or wrong, including the actual answer.
def WinOrLose(guess, answer):
    try:
        if guess == answer:
            print(f"You were right, it is {answer}!")
        else:
            print(f"Unfortunately, you were wrong by saying {guess}. It was {answer}.")
    except Exception as e:
        print("Error occurred:", e)


# Executes WinOrLose(guess, answer) function with functions userGuess() and coinFlip() embedded as arguments. Their returns are the arguments passed into WinOrLose(guess, answer).
def main():
    try:
        WinOrLose(userGuess(), coinFlip())
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
