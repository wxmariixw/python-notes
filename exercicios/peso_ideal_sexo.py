genero = input ('Você é homem ou mulher? ')

altura = float (input('Qual sua altura? '))

if genero.lower() == 'homem':
    pesoIdealHomem = (72.2 * altura) - 58
    print (f'Seu peso ideal é de {pesoIdealHomem}')

elif genero.lower() == 'mulher':
    pesoIdealMulher = (62.1 * altura) - 44.7
    print (f'Seu peso ideal é de {pesoIdealMulher}')
    
else:
    print ('Resposta inválida')