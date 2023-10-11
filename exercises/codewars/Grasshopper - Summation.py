# Description

# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

#resolution

def summation(num):
    sum = 0
    while num > 0:
        sum = sum + num
        num -= 1
    return sum

def summation(num):
    sum = 0
    for i in range(0, num):
        i += 1
        sum += i
    return sum