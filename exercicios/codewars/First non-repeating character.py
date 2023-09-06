def first_non_repeating_letter(s):
    l = []
    
    for c in s:
        if s.lower().count(c.lower()) == 1:
            l.append(c)
            
    if len(l) > 0:
        return l[0]       
    else:
        return ''