#Assume both the given number and the number of times to count will be positive numbers greater than 0.
#Return the results as an array or list ( depending on language ).
#Examples
#count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
#count_by(2,5) #should return [2,4,6,8,10]

def count_by(x, n):
    
    list = []
    mutiple = 1
    
    for i in range(n):
        
        i = x * mutiple
        list.append(i)
        
        mutiple += 1
        
    return list