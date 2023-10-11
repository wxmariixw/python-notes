ganhoHora = float (input('Quanto você recebe por hora? '))
horasTrabalhadas = float(input('Quantas horas foram trabalhadas? '))

salarioBruto = ganhoHora * horasTrabalhadas
impostoDeRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - impostoDeRenda - inss - sindicato

print (f'+ Salário Bruto : R${salarioBruto:.2f}\
        \n- IR (11%) : R${impostoDeRenda:.2f}\
        \n- INSS (8%) : R${inss:.2f}\
        \n- Sindicato (5%) : R${sindicato:.2f}\
        \n= Salário Liquido : R${salarioLiquido:.2f}')