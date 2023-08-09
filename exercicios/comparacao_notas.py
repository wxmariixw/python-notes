'''
O objetivo deste exercicio é comparar as médias das duas turmas e indicar qual foi a mais alta
'''
print ("Notas dos alunos")

sum_par = 0
sum_impar = 0

for numero_chamada in range(1, 51):
    nota_aluno = float(input(f"Por favor, insira a nota do aluno número {numero_chamada} "))
    if (numero_chamada % 2) == 0:
        sum_par += nota_aluno
    else:
        sum_impar += nota_aluno

media_par = sum_par/25
media_impar = sum_impar/25

print(f"A média da turma par é de {media_par} pontos")
print(f"A média da turma impar é de {media_impar} pontos")

if media_impar > media_par:
    print("A turma ímpar obteve a maior média de notas")
elif media_impar < media_par:
    print("A turma par obteve a maior média de notas")
else:
    print("A média de notas entre as duas turmas foram iguais")