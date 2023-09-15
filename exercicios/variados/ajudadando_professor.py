'''
O sistema deve lembrar o professor de enviar e-mail para os alunos com notas maiores que 8.5
'''
print("Ajudando o professor")

email_aluno = input("Informe o e-mail do aluno: ")
nota_semestral = float(input("Informe a nota semestral: "))

if nota_semestral > 8.5:
   print(f"ENVIANDO E-MAIL PARA {email_aluno}")