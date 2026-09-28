# Local & Global Variables
# Azhi Amin
# 18/09/2026
# OCR AS Computer Science

#example: local variables
def mySub():
    try:
        x = 10 #local variable, local to mySub
        print(x,"\n")
    except Exception as e:
        print("Error occurred:",e)

mySub() #procedure call. 'mySub' is the identifier
#print(x) #will not work as 'x is not defined', due to it not being a global variable

#example: how local variables interact
x = 200 #this actually have a global scope after definition
def mySub():
    try:
        x = 10 #defines x locally as 10, overriding the previous definition of 200
        print(x) #therefore, 10 is printed if mySub() is called
    except Exception as e:
        print("Error occurred:",e)

mySub()
print(x,"\n") #this, however prints 200 as x = 10 has a local scope to the procedure, whereas x = 200 has a local scope that works both within and outside of that procedure

#example: how local and global variables interact
x = 200
def mySub():
    try:
        global x
        x = 10
        print(x)
    except Exception as e:
        print("Error occurred:",e)

mySub()
print(x,"\n")

#1000 is printed twice
x = 1000
def mySub():
    try:
        x = 500
    except Exception as e:
        print("Error occurred:",e)
def mySub():
    try:
        print(x)
    except Exception as e:
        print("Error occurred:",e)

mySub()
print(x)


#Guessing Game

import random

number = random.randint(1,20)

def Guessing_Game():
    print("Welcome to the Guessing Game!\n")
    guess = -1
    attempts = 0
    while guess != number and attempts > 6:
        guess = int(input("Guess my number (between 1-20): ")
        HigherOrLower(guess)
        attempts += 1
    result(guess)

def HigherOrLower(guess):
    try:
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
    except Exception as e:
        print("Error occurred:",e)

def result(guess)
    try:
        if guess = number:
            print("Win")
        else:
            print("Loss")
    except Exception as e:
        print("Error occured:",e)


#...
def main():
    try:
        Guessing_Game()
    except Exception as e:
        print("Error occurred:",e)

#program starts here
if (__name__ == "__main__"):
    main()
