#Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    sum = 0
    for i in numbers:
        i *= i
        sum = sum + i
    return sum