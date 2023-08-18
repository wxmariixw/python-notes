def pig_it(text):
    words = text.split(' ')
    new_words = []
    
    for word in words:
        if word.isalpha() == True:
            first_letter = word[0]
        
            word = word.replace(first_letter, '', 1)
            word = word + first_letter + 'ay'
            new_words.append(word)
        else:
            new_words.append(word)
            
        text = ' '.join(new_words)
        
    return text

# def pig_it(text):
#     lst = text.split() # o .split vai separar as palavras e coloca-las num array chamado lst
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

    # foi usado o split string pra separar a string string[indice da primeira letra:indice depois da ultima letra]
    # [word[1:] vai pegar a partir da segunda letra  
    # + word[:1] vai pegar até a primeira letra
    # + 'ay' adicionou a string ay
    # if word.isalpha() realiza a verificação se a str é uma letra
    # else word 
    # for word in lst]