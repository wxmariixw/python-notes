# Given an array of integers, return a new array with each value doubled.

def maps(a):
    new_array = []
    
    for i in a:
        i *= 2
        
        new_array.append(i)
    
    return new_array