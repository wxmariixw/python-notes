# Manipulação de numerais

## abs() - Converte o número em absoluto
number_of_moons = 6
moons_destroyed = -1
print(abs(number_of_moons))
print(abs(moons_destroyed))

# round() - Arredonda o número
## Para se arredondar um número utilize o método `round()`
moon = 2.5867
print(round(moon))
print(round(moon, 2))

""" 
- Quando o decimal for maior ou igual que .5 o arredondamento será para cima, se for menor que .5 o arredondamento será para baixo
- O primeiro parâmetro é obrigatório, indica o número a ser arredondado e o segundo parâmetro é opcional, indica a quantidade de casa decimais
 """