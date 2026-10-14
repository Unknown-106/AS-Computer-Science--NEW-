# Longest Heatwave & Start Day
# Azhi Amin
# 12/10/2026
# OCR AS Computer Science


# Note: Tests are commented, starting from line 84


# Makes a list of heatwave runs.
def makeList(temperatures, threshold, min_days):
    try:
        runs = []
        for i in range(0, len(temperatures)):
            start_day = 0
            run_length = 0
            if temperatures[i] >= threshold:
                start_day = i + 1
                # print("Set start")
                while temperatures[i] >= threshold:
                    run_length += 1
                    if i == len(temperatures) - 1:
                        break
                    i += 1
                if run_length + 1 == min_days:
                    runs.append([start_day, run_length])
                    # print("Added run")
        return runs
    except Exception as e:
        print("Error occurred:", e)


# Bubble Sort for the list of runs, ranked in ascending order by run_length.
def bubble_sort(runs):
    try:
        Swapped = True
        while Swapped == True:
            Swapped = False
            for i in range(0, len(runs) - 1):
                if runs[i][1] > runs[i + 1][1]:
                    runs[i], runs[i + 1] = runs[i + 1], runs[i]
                    Swapped = True
        return runs
    except Exception as e:
        print("Error occurred:", e)


# Checks for equal longest runs and updates start_day to be the earliest possible longest run.
def checkEqual(runs):
    try:
        equal = []
        Tied = False
        for i in range(len(runs) - 1, 0, -1):
            if runs[i][0] == runs[len(runs) - 1][0]:
                equal.append(runs[i])
                Tied = True
            else:
                break
        Swapped = True
        while Swapped == True and Tied == True:
            Swapped = False
            for i in range(0, len(equal) - 1):
                if runs[i][1] > runs[i + 1][1]:
                    runs[i], runs[i + 1] = runs[i + 1], runs[i]
                    Swapped = True
        return equal[0]
    except Exception as e:
        print("Error occurred:", e)


# Main Sequence
def longest_heatwave(temperatures, threshold, min_days):
    try:
        runs = makeList(temperatures, threshold, min_days)
        runs_sorted = bubble_sort(runs)
        result = checkEqual(runs_sorted)
        return result
    except Exception as e:
        print("Error occurred:", e)


# print(makeList([16, 20, 32, 37, 39, 23, 35, 33, 36, 40, 18], 30, 2))

# Tests
"""
print("Testing Begins:")

print("Test 1: Normal Test. 2 runs with 1 longest run. No last day ending.")
assert longest_heatwave([16, 20, 32, 37, 39, 23, 35, 33, 36, 40, 18], 30, 2) == [
    7,
    3,
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
) == [2, 3]
print("PASS\n")


"""
