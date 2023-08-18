import string

def alphabet_position(text):
    text = text.lower().replace(' ', '')
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.translate(str.maketrans('', '', string.digits))

    num = []

    for l in text:
        n = ord(l) - 96
        num.append(str(n))
    num = ' '.join(num)
    return num