'''
Indica se o aluno passou ou não
'''

nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))

media = (nota1 + nota2)/2

if media == 10:
    print ('Aprovado com distinção')
elif media >= 7: 
    print ('Aprovado')
else: 
    print ('Reprovado')