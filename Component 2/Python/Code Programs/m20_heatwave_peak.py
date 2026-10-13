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


# Makes a list of heatwave runs.
def makeList():
    try:
        runs = []
        for i in range(0, len(temperatures)):
            start_day = 0
            run_length = 0
            if temperatures[i] >= threshold:
                start_day = i+1
                while temperatures[i] >= threshold:
                    run_length += 1
                    if i == len(temperatures) - 1:
                        break
                    i += 1
                runs.append(start_day,run_length)
    except Exception as e:
        print("Error occurred:", e)


# Bubble Sort for the list of runs, ranked in ascending order by run_length.
def bubble_sort():
    try:
        Swapped = True
        while Swapped == True:
            for i in range(len(runs)):
                Swapped = False
                if i > len(runs):
                    if runs[i][1] > runs[i+1][1]:
                        runs[i], runs[i+1] = runs[i+1], runs[i]
                        Swapped = True
    except Exception as e:
        print("Error occurred:", e)


# Checks for equal longest runs and updates start_day to be the earliest possible longest run.
def checkEqual():
    try:
        Earlier = True
        i = len(runs) - 1
        while Earlier == True:
            Earlier = False
            if runs[i-1][0] == runs[i][0]:
                i -= 1
                Earlier = True
        return runs[i]
    except Exception as e:
        print("Error occurred:", e)


#
def longest_heatwave(temperatures,threshold,min_days):
    try:
        # Makes a list of heatwave runs
        runs = []
        for i in range(0, len(temperatures)):
            start_day = 0
            run_length = 0
            if temperatures[i] >= threshold:
                start_day = i+1
                while temperatures[i] >= threshold:
                    run_length += 1
                    if i == len(temperatures) - 1:
                        break
                    i += 1
                if run_length + 1 == min_days:
                    runs.append(start_day,run_length)
                else:
                    runs.append(0,0)
        # Bubble Sort
        Swapped = True
        while Swapped == True:
            for i in range(len(runs)):
                Swapped = False
                if i > len(runs):
                    if runs[i][1] > runs[i+1][1]:
                        runs[i], runs[i+1] = runs[i+1], runs[i]
                        Swapped = True
        # Checks for equal longest runs and updates start_day to be the earliest possible longest run.
        Earlier = True
        i = len(runs) - 1
        while Earlier == True:
            Earlier = False
            if runs[i-1][0] == runs[i][0]:
                i -= 1
                Earlier = True
        return runs[i]
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
