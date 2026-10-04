# Modules
# Azhi Amin
# 02/10/2026
# OCR AS Computer Science

import random
import intComparison

# Imports module 'random' to generate a random list.
def randList():
    try:
        randomlist = []
        for i in range(0,5):
            randomlist.append(random.randint(1,30))
            print(randomlist)
    except Exception as e:
        print("Error occurred:", e)

randList()

# Imports module 'intComparison' to compare two integers.
def goCompare():
    try:
        x = int(input("Enter an integer for x: ")
        y = int(input("Enter an integer for y: ")
        intComparison.compare(x,y)
    except Exception as e:
        print("Error occurred:", e)


# ...
def three():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# ...
def main():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
