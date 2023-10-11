# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(numbers):
    sum = 0
    if len(numbers) != 0:
        for i in numbers:
            sum = sum + i
            length = len(numbers)
            average = sum / length
    else:
        return 0
    return average