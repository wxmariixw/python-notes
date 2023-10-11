import math 

metrosQuadrados = float(input('Quantos M² tem a parede que deseja pintar?')) * 1.1


litrosTinta = metrosQuadrados / 6

quantidadeDeLatasrGrandes = math.ceil(litrosTinta/18)
valorLatasGrandes = 80 * quantidadeDeLatasrGrandes
print(f'Você vai precisar de {quantidadeDeLatasrGrandes} latas grandes e gastará R${valorLatasGrandes}.')


quantidadeDeLatasrPequenas = math.ceil(litrosTinta/3.6)
valorLatasPequenas = 25 * quantidadeDeLatasrPequenas
print(f'Você vai precisar de {quantidadeDeLatasrPequenas} galões pequenos e gastará R${valorLatasPequenas:.2f}.')

quantidadeDeLatasrGrandes = math.floor(litrosTinta/18)
valorLatasGrandes = 80 * quantidadeDeLatasrGrandes
litrosTintaRestante = litrosTinta - (quantidadeDeLatasrGrandes * 18)
quantidadeDeLatasrPequenas = math.ceil(litrosTintaRestante/3.6)
valorLatasPequenas = 25 * quantidadeDeLatasrPequenas
valorTotal = valorLatasGrandes + valorLatasPequenas
print(f'Você vai precisar de {quantidadeDeLatasrGrandes} latas grandes e {quantidadeDeLatasrPequenas} galões pequenos e gastará R${valorTotal}.')
