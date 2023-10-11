# Tipos numéricos
inteiro = 1
decimal = 2.6

# Tipos strings
frase = "String"
frase_2 = 'string'

# Tipos booleanos
booleanoTrue = True
booleandoFalse = False

# A função type mostra o tipo que o Python inferiu ao valor.
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# conversão de tipos, coerção
# type convertion, typecasting, coercion
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')