def get_grade(s1, s2, s3):
    sum = s1 + s2 + s3
    average = sum/3
    
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average :
        return "B"
    elif 70 <= average :
        return "C"
    elif 60 <= average :
        return "D"
    else:
        return "F"