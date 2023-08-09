'''
Ordena os numeros de maior pra menor
'''
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o último número: '))

if numero1 > numero2:
    if numero2 > numero3:
        print (f'A ordem dos números é {numero1}, {numero2} e {numero3}')
    else:
        print (f'A ordem dos números é {numero1}, {numero3} e {numero2}')

elif numero2 > numero3:
    if numero1 > numero3:
        print (f'A ordem dos números é {numero2}, {numero1} e {numero3}')
    else:
        print (f'A ordem dos números é {numero2}, {numero3} e {numero1}')

else:
    if numero2 > numero1:
        print (f'A ordem dos números é {numero3}, {numero2} e {numero1}')
    else: 
        print (f'A ordem dos números é {numero3}, {numero1} e {numero2}')
