'''
Indica o sexo escolhido
'''
sexo = input('Selecione o sexo: \n F \n M \n')

if sexo.upper() == "F":
    print(f'{sexo.upper()} - Feminino')
elif sexo.upper() == "M":
    print(f'{sexo.upper()} - Masculino')
else: 
    print('Sexo inválido')
