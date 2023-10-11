salario = float(input('Oba, Aumento! Quer descobrir de quanto será o seu? Digite aqui seu salário atual: '))

if salario <= 280:
    porcentagem = 0.2
elif salario < 700:
    porcentagem = 0.15
elif salario < 1500:
    porcentagem = 0.1
else:
    porcentagem = 0.05

aumento = salario * porcentagem
salario_aumento = salario + aumento

print (f'Seu salário era: R${salario:.2f}\
       \nTeve um aumento de: {(porcentagem*100):.0f}%\
       \nNo valor de: R${aumento:.2f}\
       \nValor final: R${salario_aumento:.2f}')