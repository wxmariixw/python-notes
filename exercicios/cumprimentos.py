'''
Indica se é bom dia, boa tarde ou boa noite de acordo com a hora
'''

turno = input('Qual turno você estuda? \n Digite: \n M - Matutino \n V - Vespertino \n N - Noturno \n')

if turno.upper() == "M":
    print('Bom dia!')

elif turno.upper() == "V":
    print('Boa tarde!')

elif turno.upper() == "N":
    print('Boa noite!')

else:
    print('Valor inválido')