def duplicate_count(text):
    text_lower = text.lower()
    sum = 0

    for i in text_lower:
        counter = text_lower.count(i)
        text_lower = text_lower.replace(i, '')
        
        if counter >= 2:
            sum += 1

    return sum