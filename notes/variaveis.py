# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _.

nome_completo = 'Luiz Otávio Miranda'
soma_dois_mais_dois = 2 + 2
int_um = bool('1')
print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois)

nome = 'Luiz'
idade = 17
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)

nome = 'Luiz Otávio'
sobrenome = 'Miranda'
idade = 18
ano_nascimento = 2022 - idade
maior_de_idade = idade >= 18
altura_metros = 1.80

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)