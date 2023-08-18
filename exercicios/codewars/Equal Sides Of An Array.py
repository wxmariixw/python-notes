# arr = [1,2,3,4,3,2,1]

# sumr = 0
# suml = 0

# for i in range(len(arr)):
#     for a in arr[0:i]:
#         sumr += a
#         # print(sumr)
#         # print("esse é o sumr")
            
#     for b in arr[i+1:]:
#         suml += b
#         print(suml)
#         print("esse é o suml")
    
#     i += 1

# if sumr == suml:
#     print(arr.index(i))
# else:
#     print(-1)

def find_even_index(arr):
    sumr = 0
    suml = 0
    
    for i in arr:     
        for a in range(arr[0], arr.index(i)):
            sumr += a
            
        for b in range(arr.index(i)+1, arr[-1]):
            suml += b
            
    if sumr == suml:
        return arr.index(i)
    else:
        return -1
    
print(find_even_index(1,2,3,4,3,2,1))
