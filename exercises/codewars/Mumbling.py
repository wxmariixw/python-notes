#This time no story, no theory. The examples below show you how to write function accum

def accum(s):
    list = []
    index = 1
    accum = ''
    
    for i in s:
        lower = i.lower()
        item = lower * index
        cap = item.capitalize()
        list.append(cap) 
        
        index += 1
    
    accum = '-'.join(list)
    
    return accum