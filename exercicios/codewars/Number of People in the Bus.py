def number(bus_stops):
    get_on = 0
    get_off = 0
    
    for i in bus_stops:
        get_on += i[0]
        get_off += i[1]
        
    total = get_on - get_off
    
    return total