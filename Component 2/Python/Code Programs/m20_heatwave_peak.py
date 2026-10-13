# Longest Heatwave & Start Day
# Azhi Amin
# 12/10/2026
# OCR AS Computer Science


# Standard Libraries
pass

# Third Party Libraries
pass

# Local Modules
pass


# temperatures: list of consecutive daily maximum temperatures in °C.
# threshold: temperature at or above which a day is hot.
# min_days: positive whole number.
# Empty lists are allowed.
# Number days starting from 1.

# A list containing [start_day, run_length]. Return [0, 0] if there is no qualifying heatwave.


#
def longest_heatwave(temperatures, threshold, min_days):
    try:
        start_day = 0
        run_length = 0
        runs = []
        #Makes a list of heatwave runs
        for i in range(0, len(temperatures)):
            if temperatures[i] >= threshold:
                start_day = i+1
                while temperatures[i] >= threshold:
                    run_length += 1
                    if i == len(temperatures) - 1:
                        break
                    i += 1
                runs.append(start_day, run_length)
        #Bubble Sort
        for i in range(len(runs)):
            if runs[i][1] > runs[i+1][1]
                runs[i][1], runs[i+1][1] = runs[i+1][1], runs[i][1]
    except Exception as e:
        print("Error occurred:", e)


# ...
def main():
    try:
        longest_heatwave()
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
