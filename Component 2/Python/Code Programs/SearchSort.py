# SearchSort Module
# Azhi Amin
# 06/11/2026
# OCR AS Computer Science


# Standard Libraries
import random

# Third Party Libraries
pass

# Local Modules
pass


# ...
def linear(nlist, target):
    try:
        duplicates = 0
        for i in range(0, len(nlist)):
            if nlist[i] == target:
                # print(f"Target found at Index {i}.")
                duplicates += 1
        if duplicates > 1:
            return 0, 0
        else:
            return i, duplicates
    except Exception as e:
        print("Error occurred:", e)


# ...
def binary():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# ...
def bubble():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# ...
def insertion():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# Test Sequence
def main():
    try:
        nlist = [random.randint(0,100) for i in range(0,100)]
        target = int(input("Enter a number between 1 and 100: "))
        target_index, target_duplicates = linear(nlist, target)
        print(target_index, target_duplicates)
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
