'''
indica o produto mais barato
'''
produto1 = float( input('Qual o valor do primeiro produto? '))
produto2 = float( input('E qual o valor do segundo produto? '))
produto3 = float( input('E qual o valor do terceiro produto? '))

if produto1 > produto2 and produto1 > produto2:
    print(f'você deverá comprar primeiro produto.')

elif produto2 > produto1 and produto2 > produto3:
    print(f'Você deverá comprar o segundo produto.')

else:
    print(f'Você deverá comprar o terceiro produto.')