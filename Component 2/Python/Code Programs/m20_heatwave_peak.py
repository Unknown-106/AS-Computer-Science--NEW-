# Longest Heatwave & Start Day
# Azhi Amin
# 12/10/2026
# OCR AS Computer Science

# Credit to Eliot Bennett for helping me debug makeList()
# Eliot's comments are marked with 'Eliot:', my replies to his comments are within {}

# Note: Tests are commented, starting from line __.


# Makes a list of valid heatwave runs.
def makeList(temperatures, threshold, min_days):
    try:
        runs = []
        start_day = 0 # Eliot: are there enough comments {no, MORE COMMENTS}
        run_length = 0
        for i in range(0, len(temperatures)):
            if temperatures[i] >= threshold and i > start_day + run_length - 1: # Eliot: check if the day is hot enough; and if it hasn't been counted yet (by a previous run), -1 because startday is 1 indexed
                start_day = i + 1 # since days start at 1 (why?? {because we are outputting the actual days?})
                j = i # Eliot: i mean really should be i + 1 to be more efficient but oh well ive already uploaded it [to GitHub], barely any more ops anyway
                run_length = 0
                while temperatures[j] >= threshold:
                    run_length += 1
                    if j == len(temperatures) - 1:
                        break
                    j += 1
                if run_length >= min_days: # Eliot: you said if the run_length is == to the min days you silly fool, oh and you also said run_length + 1 in this if but then not +1 in the line after
                    runs.append([start_day, run_length])
        return runs
    except Exception as e:
        print("Error occurred:", e)


# Bubble sorts the list of runs in ascending order by run_length.
def bubble_sort(runs):
    try:
        swapped = True
        while swapped == True:
            swapped = False
            for i in range(0, len(runs) - 1):
                if runs[i][1] > runs[i + 1][1]:
                    runs[i], runs[i + 1] = runs[i + 1], runs[i]
                    swapped = True
        return runs
    except Exception as e:
        print("Error occurred:", e)


# Checks for the longest runs with equal run_length.
def checkEquals(runs):
    try:
        equals = []
        for i in range(len(runs) - 1, -1, -1):
            if runs[i][1] == runs[len(runs) - 1][1]:
                equals.append(runs[i])
            else:
                break
        return equals
    except Exception as e:
        print("Error occurred:", e)
        
# Linear search for the earliest start_day.
def searchEarliest(equals):
    try:
        index = 0
        earliest = equals[index][0]
        for i in range(0, len(equals)):
            if equals[i][0] <= earliest:
                earliest = equals[i][0]
                index = i
        return equals[index]
    except Exception as e:
        print("Error occurred:", e)


# Main Sequence
def longest_heatwave(temperatures, threshold, min_days):
    try:
        runs = makeList(temperatures, threshold, min_days)
        runs_sorted = bubble_sort(runs)
        equals_list = checkEquals(runs_sorted)
        result = searchEarliest(equals_list)
        return result
    except Exception as e:
        print("Error occurred:", e)


# Tests
# """
print("Testing Begins:\n")

print("Test 1: Normal Test. 2 runs with 1 longest run. No last day ending.")
assert longest_heatwave([16, 20, 32, 37, 39, 23, 35, 33, 36, 40, 18], 30, 2) == [
    7,
    4,
]
print("PASS\n")

print("Test 2: Boundary Test. 2 boundary runs with 1 longest run. No last day ending.")
assert longest_heatwave([40, 39, 39, 40, 40, 39, 39, 40, 40, 40, 39], 40, 2) == [
    8,
    3,
]
print("PASS\n")

print(
    "Test 3: Boundary Test. 2 boundary runs with 1 longest run. Includes last day ending."
)
assert longest_heatwave([20, 19, 20, 20, 20, 19, 19, 20, 20, 20, 20], 20, 3) == [
    8,
    4,
]
print("PASS\n")

print(
    "Test 4: Normal Test. 4 runs with 1 longest run. No last day ending, requires sorting."
)
assert longest_heatwave(
    [
        34,
        31,
        39,
        35,
        21,
        23,
        35,
        36,
        39,
        32,
        31,
        19,
        32,
        26,
        21,
        31,
        33,
        27,
        28,
        34,
        36,
        37,
        18,
    ],
    30,
    2,
) == [7, 5]
print("PASS\n")


print(
    "Test 5: Normal Test. 4 runs with 2 tied for longest run. No last day ending, requires sorting."
)
assert longest_heatwave(
    [16, 20, 32, 37, 39, 23, 27, 31, 33, 28, 35, 33, 38, 26, 32, 34], 30, 2
) == [3, 3]
print("PASS\n")


# """
