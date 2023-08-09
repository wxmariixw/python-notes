'''
infica o maior e menor numero
'''
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

if numero1 > numero2:
    if numero2 > numero3:
        print (f"O maior número é {numero1} e o menor é {numero3}")
    else:
        print (f"O maior número é {numero1} e o menor é {numero2}")

elif numero2 > numero3:
    if numero1 > numero3:
        print (f"O maior número é {numero2} e o menor é {numero3}")
    else:
        print (f"O maior número é {numero2} e o menor é {numero1}")

else:
    if numero2 > numero1:
        print (f"O maior número é {numero3} e o menor é {numero1}")
    else: 
        print (f"O maior número é {numero3} e o menor é {numero2}")
