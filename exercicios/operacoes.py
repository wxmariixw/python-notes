numeroInteiro1 = int(input('Digite um número inteiro: '))
numeroInteiro2 = int(input('Digite outro número inteiro: '))
numeroReal = float(input('Digite um número real: '))

operacao1 = (2 * numeroInteiro1) * (numeroInteiro2 / 2)
operacao2 = (3 * numeroInteiro1) + numeroReal
operacao3 = (numeroReal**3)

print (f'O produto do dobro de {numeroInteiro1} com metade de {numeroInteiro2} é de {operacao1}.')
print (f'A soma do triplo de {numeroInteiro1} com {numeroReal} é de {operacao2}.')
print (f'{numeroReal} elevado ao cubo é {operacao3}.')