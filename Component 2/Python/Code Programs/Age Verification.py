# Age Verification
# Azhi Amin
# 14/10/2026
# OCR AS Computer Science


# Standard Libraries
pass

# Third Party Libraries
pass

# Local Modules
pass


# Verifies if the user is an adult or minor based on whether the age is 18 or over, or under 18.
def verifyAge():
    try:
        while True:
            age = input("Enter your age: ")
            try:
                age = int(age)
                if not (0 < age < 120):
                    print("Error. Must enter a whole number between 0 and 120.")
                    continue
                else:
                    break
            except ValueError:
                print("Error. Must enter a whole number between 0 and 120.")
        if age >= 18:
            print(f"Your age is {age}. You are an adult.")
        else:
            print(f"Your age is {age}. You are an minor.")
        
    except Exception as e:
        print("Error occurred:", e)


# Main Sequence
def main():
    try:
        verifyAge()
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
