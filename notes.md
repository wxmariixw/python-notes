# Notas

## Linguagem
### Tipos de dados
- Tipos númericos - int, float, complex
- Tipo texto - string
- Tipo booleanos - bool
```python
a = "isto é uma string" # tipo string com aspas duplas
b = 'isto também é uma string' # tipo string com aspas simples
c = True # tipo booleano
d = False # tipo booleano
e = 1.4 # tipo float
f = 9 # tipo inteiro
```

### Operadores
```python
a = 1 + 2 # Soma
b = 2 - 1 # Subtração
c = 3 * 4 # Multiplicação
d = 4 / 2 # Divisão
e = 1 # Igualdade
f = 5 // 4 # Divisão inteira
g = 5 % 4 # Resto de uma divisão

# Altera o valor da variável
a += 2 #Aqui ele vai somar 2 a 3 e o valor se tornará 5
b -= 1 #Aqui ele vai diminuir 1 de 1 e o valor se tornará 0
c /= 2 #Aqui ele vai dividir 12 por 2 e o valor se tornará 6
d *= 5 #Aqui ele vai multiplicar 2 por 5 e o valor se tornará 10

# lógica condicional
a == b # Igual à
a != b # Diferente de
a < b # Menor que
a <= b # Menor ou igual à
a > b # Maior que
a >= b # Maior ou igual à
```
- Tabela da verdade para `and`:
``` python
True and True == True
True and False == False
False and True == False
False and False == False
```
- Tabela da verdade para `or`:
``` python
True or True == True
True or False == False
False or True == False
False or False == False
```
- Operador `in` retorna se existe uma determinada string dentro de outra
```python
print("moon" in "talking to the moon")
#saída
True
```

### Entrada do usuário
#### Função `input()`

```python
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)
```

### Condições
A condição If é respondida com booleanos (true ou false), se a instrução for entendida com `True`, será realizada, se for `False` irá dar continuada para a próxima condição
```python
if a < b:
	=return c
elif a == b:
	return d
else:
	return e
```

### Manipulação de strings
Ao precisar utilizar aspas no meio de strings pode ser utilizado tipos diferentes de aspas:
- Quando existe aspas simples no texto, utiliza aspas duplas
- Quando existe aspas duplas no texto, utiliza aspas simples
- Quando existem os dois tipos de aspas, utiliza aspas triplas

#### Método `title()`
- A primeira letra de todas as palavras ficam em maiúsculo
```python
titulo = "moon facts"
print(titulo.title())
#saida
Moon Facts
```

#### Método `split()`
- Sem argumentos, ela separa todos as palavras com espaço em um array
- Ao chamar o mesmo método com argumentos (ex: `split("/n")`) separa de acordo com a posição do argumento
```python
moon_facts = "The Moon is drifting away from the Earth."
print(moon_facts.split())
#saida
("The","Moon","is","drifting","away","from","the","Earth.")
```

#### Método `join()`
- Faz a função contrária, ele junta itens de listas, onde é necessário indicar o item que ficará entre os itens concatenados
```python
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
#saida
"The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year."
```

#### Método `find()`
Busca uma substring dentro de uma string
```python
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print("Moon".find(moon_facts))
#saida
True
```
- Quando não encontra a string buscada a resposta na saída é “-1”
    - Quando a string é encontrada é retornado a posição em que se encontra a string
  
#### Método `count()`
Conta quantas ocorrências existem da busca na string
```python
moon_facts = ["The Moon is drifting away from the Earth."]
print(moon_facts.count(o))
#saida
3
```

#### Método `lower()`
Torna todas as letras ficam no minúsculo
```python
moon_facts = ["The Moon is drifting away from the Earth."]
print(moon_facts.lower())
#saida
"the moon is drifting away from the earth"
```

#### Métodos `upper()`
Todas as letras ficam no maiúsculo
```python
moon_facts = ["The Moon is drifting away from the Earth."]
print(moon_facts.upper())
#saida
"THE MOON IS DRIFTING AWAT FROM THE EARTH"
```

#### Método `isnumeric()`
Confere se todos os caracteres da string são números
```python
moon_facts = ["The Moon is drifting away from the Earth."]
print(moon_facts.isnumeric())
#saida
False
```

#### Método `isdecimal()`
Verifica se os caracteres são decimais, podem ser números na base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Basicamente qualquer caractere da categoria "Nd" do Unicode General Category “Nd”.

#### Método `startwith()`
Verifica se a substring indicada no método existe no começo da string indicada
```python
moon_facts = ["The Moon is drifting away from the Earth."]
print(moon_facts.lower())
#saida
"The Moon is drifting away from the Earth."
```

#### Método `endwith()`
Verifica se a substring indicada no método existe no fim da string indicada
```python
moon_facts = ["The Moon is drifting away from the Earth."]
print(moon_facts.lower())
#saida
"The Moon is drifting away from the Earth."
```

#### Método `replace()`
dois argumentos devem ser indicados, o dado a ser tirado e o que deve ser adicionado
#### Método format()

O método `.format()` usa chaves (`{}`) como espaços reservados em uma cadeia de caracteres e usa a atribuição de variável para substituir o texto.

```python
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

#Saída: `On the Moon, you would weigh about 1/6 of your weight on Earth.`

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
```
https://docs.python.org/pt-br/3/library/string.html

## Interpolação de string

string = s

int = d ou s

float = f

hexadecimal = x ou X (ABCDEF0123456789)

```python
nome = 'Luiz'
preco = 100,2546817
variavel = '%s, o preço é R$%0.2f' % (nome, preco)

print(variavel)
print ('O hexadecimal de %i é %08x' % (preco, preco)) #o 0 é o caractere e o 8 é a quantidade de caracteres a serem preenchidos
```

formatação de string

(Caractere)(><^)(quantidade)

> - Esquerda

< - Direita

^ - Centro

= - Força o número a aparecer antes dos zeros

Sinal - + ou -

Conversion flags - !r !s !a

```python
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
```

Fatiamento de string

Fatiamento [i:f:p] [::]

variavel = 'Olá mundo'
print(variavel[::-1])

```python
frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
```






- dicionário acessa por chaves {} e classe acessa por ponto .


```python
sum = 1 + 2
print(sum)
```

- O print é uma função que imprime o valor no console
- Qualquer função é executada com um parênteses ( )



# Manipulação de numerais

- Ao usar o método `abs()` o número é convertido em número absoluto, ignorando se é positivo ou negativo
- Para se arredondar um número utilize o método `round()`, quando o decimal for maior ou igual que .5 o arredondamento serão para cima, se for menor que .5 o arredondamento será para baixo

# Loops

# Listas

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```

- Para acessar os itens da lista deve ser colocado o índice entre colchetes [ ] (ex: `planets[5]`)
- Os índices sempre se iniciam pelo índice 0 e quando o índice é negativo é contado a partir do último item
- Para determinar o tamanho de uma lista usa-se a função `len()`, entre parenteses coloca-se a variável da lista
- Para adicionar um item no final da lista, usa-se o método `append()`, entre parenteses coloca-se o valor que quer adicionar
- Para remover usa-se o método `pop()`, que remove o útimo item da lista
- Para localizar um item utilizar o método `index()`, indicando o valor a ser descoberto o indez
- As funções min() e max() indicam o menor número da lista e o maior número da lista
- Para selecionar itens específicos da lista indique a variável e o index do primeiro item e onde é necessário fazer o corte, esta cria uma nova lista sem alterar a lista original

```python
planets[0:3]

resposta:
["Mercury", "Venus", "Earth"]
```

- É possível unir duas listas com um +
- Para classificar listas usa-se o método `sort()`, assim sendo automaticamente ordenado por ordem alfabética ou numérica
    - Caso queira em ordem decrescente ou contraria à alfabética é necessário coloca-se `reverse = True` como argumento

# While

```python
user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')
```

# For

```python
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

for i in range(start, stop, s
tep)
```

- A palavra `for`, seguida por um espaço.
- O nome da variável que você deseja criar para cada valor da sequência (`number`).
- A palavra `in`, cercada por espaços.
- O nome da lista (`countdown`, no exemplo anterior) ou do objeto iterável que você deseja percorrer com o loop, seguido de dois-pontos (`:`).
- O código que você deseja executar para cada item do objeto iterável, separado por espaço em branco aninhado.
- Com a função `sleep()`, é possível colocar um tempo de espera para a próxima leitura do loop
  
# Dicionário

```python
planet = {
    'name': 'Earth',
    'moons': 1
}
```

- Para ler os valores de respectivas chaves do dicionário usa-se o método `get()`
    
    ```python
    print(planet.get['name'])
    ```
    
- Para modificar o valor da chave de um dicionário utiliza-se o método `update()`, a principal vantagem de usar `update` é a capacidade de modificar vários valores em apenas uma operação
    
    ```python
    planet.update({'name': 'Makemake'})
    
    ou
    
    planet['name'] = 'Makemake'
    ```
    
- Adicionar e remover chaves
    
    ```python
    Para adicionar escreva dessa forma:
    planet['orbital period'] = 4333
    
    # planet dictionary now contains: {
    #   name: 'jupiter'
    #   moons: 79
    #   orbital period: 4333
    # }
    
    Para remover utilize o método .pop()
    planet.pop('orbital period')
    
    # planet dictionary now contains: {
    #   name: 'jupiter'
    #   moons: 79
    # }
    ```
    
- Tipos de dados complexos
    - Quando o dado tem uma chave dentro de outra chave:
        
        ```python
        planet['diameter (km)'] = {
            'polar': 133709,
            'equatorial': 142984
        }
        ```
        
- Para resgatar o dado utiliza-se a encadeamento de colchetes ou `get()`
    
    ```python
    print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
    
    ou
    
    print(planet.get('name') + " polar diameter: " + planet["diameter (km)"].get('polar'))
    ```
    
- Pra recuperar chaves e valores usa-se o método `keys()`

```python
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys()
	print(key)
```

Funções

- Funções sem argumentos
    - Para criar uma função use `def + um nome para a função`
    
    ```python
    def rocket_parts():
        print("payload, propellant, structure")
    ```
    
    - No caso essa função não tem argumentos para que ela aconteça, por isso os parenteses estão vazios
    - Para executa-la chama ela pelo nome e usa-se parenteses `rocket_parts()`
- Funções com argumentos
    
    ```python
    def days_to_complete(distance, speed):
        hours = distance/speed
        return hours/24
    
    days_to_complete(1500, 60)
    
    ```
    


## Ferramentas
### Datas
- Importar o módulo "date"
```python
from datetime import date
```
https://docs.python.org/pt-br/3/library/datetime.html

### Biblioteca de matemática

```python
from math import ceil, floor
```
## Ambientes virtuais
Ambientes virtuais ajudam o programador a reunir todos os recursos necessários, como os requieriments.txt e também evitar que outros recursos atrapalhem o 

```shell
py -m venv venv
venv/Scripts/Activate
```
### Compartilhar os requirements.txt
```shell
pip freeze > requirements.txt
```
### Instalar os requirements.txt
```shell
pip install -r requirements.txt
```

# Usando um pacote

```python
from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)
```

## **Aplicar uma estratégia de atualização**

Os pacotes usam algo chamado *controle de versão semântico*. Isso significa que, se você olhar para um número como a versão "1.2.3", poderá desmembrar esse número:

| Principal | Secundária | Patch |
| --- | --- | --- |
| 1 | 2 | 3 |
- O número mais à esquerda é chamado de `Major`. Se esse número aumentar, isso significará que muitas coisas mudaram e você não poderá mais supor que os métodos sejam nomeados da mesma forma ou tenham o mesmo número de argumentos que antes.
- O número do meio é chamado de `Minor`. Se ele mudar, isso significará que um recurso será adicionado.
- O número mais à direita é chamado de `Patch`. Se esse número aumentar, provavelmente significará que um bug foi corrigido.

https://www.datacamp.com/tutorial/f-string-formatting-in-python?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=143216588537&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=665485585140&utm_targetid=aud-299261629574:dsa-1947282172981&utm_loc_interest_ms=&utm_loc_physical_ms=1001773&utm_content=dsa~page~community-tuto&utm_campaign=230119_1-sea~dsa~tutorials_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-ltsjul23&gclid=CjwKCAjw8symBhAqEiwAaTA__ErOSRXBRe_RD5fQFsIVhfL13sIlElgjVZtwIrqaepXRsAnsrwPlLxoCTY0QAvD_BwE