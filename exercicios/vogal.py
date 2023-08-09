'''
Indica se a letra é uma vogal com consoante
'''
letra = input('Digite uma letra: ')

if letra.upper() == "A" or letra.upper() == "E" or letra.upper() == "I" or letra.upper() == "O" or letra.upper() == "U:":
    print('Vogal')
else:
    print('Consoante')