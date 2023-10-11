""" Como entrada e saida de dados pelo e para o usuário usa-se as seguintes funções """

# Entrada - É declarado a variável diretamente, assim quando a entrada for digitada ela fica salva nessa variável
entrada = input("Digite aqui sua entrada")

# Saída - O print imprime os valores no console do prompt de comando
print(entrada)

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
