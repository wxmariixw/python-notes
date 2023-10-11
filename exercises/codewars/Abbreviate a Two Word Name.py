#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#The output should be two capital letters with a dot separating them

def abbrev_name(name):
    names = name.split()
    firstLetter = []
    
    for i in names:
        firstLetter.append(i[0])
        abbreviate = '.'.join(firstLetter)
    return abbreviate.upper()