# Manipulação de strings
# Manipulação de strings é basicamente a modificação do tipo de dado string

# title() - Transforma as primeiras letras da palavra em maiúscula
titulo = "As funções do python"
titulo.title()

# lower() - Transforma todos os caracteres em minúsculo
moon_facts = "The Moon is drifting away from the Earth."
print(moon_facts.lower())

# upper() - Transforma todos os caracteres em maiúsculo
moon_facts = "The Moon is drifting away from the Earth."
print(moon_facts.upper())

# split() - Separa as palavras da string em um array
## Obs: Ao chamar o mesmo método com argumentos (ex: `split("/n")`) separa de acordo com a posição do argumento
moon_facts = "The Moon is moving."
print(moon_facts.split())

# join() - Junta as strings de uma array
moon_facts = ["The Moon.", "is moving."]
print(' '.join(moon_facts))

# find() - Busca uma substring dentro de uma string
moon_facts = "The Moon is moving"
print("Moon".find(moon_facts))

# count() - Conta quantas ocorrências existem da busca na string
moon_facts = "The Moon is drifting away from the Earth."
print(moon_facts.count('o'))

# isnumeric() - Verifica se na string existem números (qualquer um da tabela encode)

# isdecimal() - Verifica se a string é feita apenas de números decimais (0-9)

# startwith() - Verifica se a string inicia com a substring solicitada

# endwith() - Verifica se a string acaba com a substring solicitada

# replace() - Altera a string, retirando o primeiro parâmetro dado e alterando para o segundo parâmetro dado
moon = "the moon is a planet"
print(moon.replace("planet", "satellite"))

# format() - Usa chaves (`{}`) como espaços reservados em uma cadeia de caracteres e usa a atribuição de variável para substituir o texto.
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

"""
Ao precisar utilizar aspas no meio de strings pode ser utilizado tipos diferentes de aspas:
- Quando existe aspas simples no texto, utiliza aspas duplas
- Quando existe aspas duplas no texto, utiliza aspas simples
- Quando existem os dois tipos de aspas, utiliza aspas triplas
"""

"""
Interpolação de string
- string = s
- int = d ou s
- float = f
- hexadecimal = x ou X (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 100.2546817
variavel = '%s, o preço é R$%0.2f' % (nome, preco)

print(variavel)
print ('O hexadecimal de %i é %08x' % (preco, int(preco)))
# O 0 é o caractere e o 8 é a quantidade de caracteres a serem preenchidos

""" 
Formatação de string
> - Alinha a esqueda
< - Alinha a direita
^ - Alinha no centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')


# Fatiamento de string [i:f:p] [::]
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

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
""" https://docs.python.org/pt-br/3/library/string.html """

