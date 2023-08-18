import string

def top_3_words(text):
      
    punctuations = string.punctuation.replace("'", "")

    text = text.lower().translate(str.maketrans('', '', punctuations))
    text = " ".join(text.split())
    text = text.split()

    counts = []
    letters = []

    for word in text:
        text.count(word)
        counts = ([[l, text.count(l)] for l in set(text)])

    counts.sort(key=lambda x: x[-1], reverse=True)

    for i in counts[:3]:
        letters.append(i[0])
    
    for i in letters:
        if i in string.punctuation:
            letters = []

    return letters

#not finished