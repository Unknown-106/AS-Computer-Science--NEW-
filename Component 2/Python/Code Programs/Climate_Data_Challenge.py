# Climate Data Challenge
# Azhi Amin
# 29/09/2026
# OCR AS Computer Science


# User inputs their 3 temperature readings.
def temperatureInputs():
    try:
        first = int(input("Enter the first temperature reading (integer): "))
        second = int(input("Enter the second temperature reading (integer): "))
        third = int(input("Enter the third temperature reading (integer): "))
        return [first, second, third]
    except Exception as e:
        print("Error occurred:", e)


# Compares the first, second and third temperature readings exhaustively and outputs the largest reading/s.
def comparison(first, second, third):
    try:
        if first > second and first > third:
            print(f"The first temperature reading is the largest, at {first}*C.")
        elif second > first and second > third:
            print(f"The second temperature reading is the largest, at {second}*C.")
        elif third > first and third > second:
            print(f"The third temperature reading is the largest, at {third}*C.")
        elif first == second:
            print(
                f"Both the first and second temperature readings are the largest, at {first}*C."
            )
        elif first == third:
            print(
                f"Both the first and third temperature readings are the largest, at {first}*C."
            )
        elif second == third:
            print(
                f"Both the second and third temperature readings are the largest, at {second}*C."
            )
    except Exception as e:
        print("Error occurred:", e)


# Execute
def main():
    try:
        array_Temperature = temperatureInputs()
        first = array_Temperature[0]
        second = array_Temperature[1]
        third = array_Temperature[2]
        comparison(first, second, third)
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
