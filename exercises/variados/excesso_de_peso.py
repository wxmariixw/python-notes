from site import execsitecustomize


peso = float(input('Qual o peso? '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O excesso de peso foi de {excesso} e a multa será de {multa}.')

else:
    print(f'O peso foi de {peso} e você não irá pagar multa.')