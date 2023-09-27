''' Listas ou arrays são conjuntos de itens, esses itens podem ter qualquer tipagem,
como inteiros, strings ou booleanos'''

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# funções
## len() - determina o tamanho do array, entre parênteses coloca-se a variável da lista
print(len(planets))

## append() - adiciona um item no final da lista, entre parênteses coloca-se o valor que quer adicionar
planets.append("Sun")
print(planets)

## pop() - Remove itens da lista
planets.pop(-1)
print(planets)

## index() - Localiza um item dentro do array
print(planets.index("Venus"))

## min() - Indica o menor número do array
arr = [1, 2, 3, 4, 5]
print(min(arr))

## max() - Indica o maior número do array
print(max(arr))

## sort() - Organiza listas de acordo com a ordem alfabética ou numérica
### Caso queira em ordem decrescente ou contraria à alfabética é necessário coloca-se `reverse = True` como argumento
lista = [1, 4, 7, 8, 5, 2, 1, 4, 7, 8, 5, 2]
lista.sort()
print(lista)

## enumerate() - Enumera cada item de uma lista de acordo com o próprio index, juntando o index e o item em uma tupla
enumerado = enumerate(lista)
print(list(enumerado))



