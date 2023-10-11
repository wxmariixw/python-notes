import math 

metrosQuadrados = float(input('Quantos M² tem a parede que deseja pintar?'))

litrosTinta = metrosQuadrados / 3
quantidadeDeLatas = math.ceil(litrosTinta/18)
valorLatas = 80 * quantidadeDeLatas

print(f'Você precisará de {quantidadeDeLatas} latas e gastará R${valorLatas:.2f}.')