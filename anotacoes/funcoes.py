# Para criar uma função use `def + um nome para a função`

def printar_frase(): # No caso essa função não tem argumentos para que ela aconteça, por isso os parenteses estão vazios
    print("payload, propellant, structure")

def days_to_complete(distance, speed): # Essa função possue argumentos, que são inicializados na hora que chama a função
    hours = distance/speed
    return hours/24
   
days_to_complete(1500, 60)

# lambda - cria uma função de forma fácil
f = lambda x: x**2 # O argumento dessa função é x e o que vem após os dois pontos indica o que a função vai realizar

# map()` - aplica uma função à todos os itens de uma lista
numeros = [1, 2, 3, 4, 5]
f = lambda x: x**2
    # recebe o primeiro argumento como a função a ser aplicada e em seguida a lista que será utilizada na função
lista_quadrados = list(map(f, numeros))
print(lista_quadrados)

    # exemplo 2
lista_quadrados = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(lista_quadrados)

