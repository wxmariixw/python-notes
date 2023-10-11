# Operadores aritiméticos
soma = 2 + 1
subtracao = 2 - 1
multiplicacao = 3 * 4
divisao = 4 / 2
divisao_inteira = 5 // 4
resto_modulo = 5 % 4
expotenciacao = 5 ** 2

# Operadores de atribuição
igualdade = 1

iteracao_soma = 1 # é necessário declarar a variável antes de atribuir um segundo valor a ela
iteracao_soma += 1

iteracao_subtracao = 1
iteracao_subtracao -= 1

iteracao_multiplicacao = 1
iteracao_multiplicacao *= 1

iteracao_divisao = 1
iteracao_divisao /= 1

iteracao_resto = 1
iteracao_resto %= 1

# Operadores de comparação
## Retorna True ou False
maior_que = 10 # é necessário declarar a variável antes de comparar valores
maior_que > 5

menor_que = 10
menor_que < 5

igual_a = 5
igual_a == 5

diferente_de = 9
diferente_de != 5

maior_ou_igual = 7
maior_ou_igual >= 5

menor_ou_igual = 4
menor_ou_igual <= 5

# Operadores lógicos
## Retorna True ou False
x = 8
y = 5

x > 1 and y < 5
x > 1 or y < 5
not(x > 1 and y < 5)

# Operadores de identidade
x = 6
x is 10
x is not 4

# Operadores de associação
x = 'Mariana Freitas de Abreu'
y = 'Mariana'
z = 'Julia'

y in x
z not in x

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )


""" Operadores lógicos

and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras.

Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor

São considerados falsy 0 0.0 '' False

Também existe o tipo None que é usado para representar um não valor """

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
senha = input('Senha: ') or 'Sem senha'
print(senha)

""" Operador lógico "not"
Usado para inverter expressões

not True = False
not False = True"""
print(not True)  # False
print(not False)  # True

# Operadores in e not in

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
