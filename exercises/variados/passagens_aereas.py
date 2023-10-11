'''
O objetivo desse exercicio era construir um sistma para uma companhia aérea que possui tres tipos de passagem:
- Economica
- Executiva
- Primeira classe

e cada passagem proporciona um desconto de acordo com os pacotes:
Economica para 2 pessoas tem desconto de 3%, 3 pessoas desconto de 4% e 4 pessoas ou mais desconto de 5%
Executiva para 2 pessoas tem desconto de 5%, 3 pessoas desconto de 7% e 4 pessoas ou mais desconto de 8%
Primeira classe para 2 pessoas tem desconto de 10%, 3 pessoas desconto de 15% e 4 pessoas ou mais desconto de 20%
'''

print("Desconto de passagens aéreas!");
print("Temos três tipos de passagens:Econômica - R$100 (1), Executiva - R$200 (2) e Primeira Classe - R$300 (3).")

passagem = float(input("Escolha número do seu tipo de passagem: "));
passageiros = float(input("Temos descontos progressivos para pacotes! Quantos passageiros serão? "))

economica = 100
executiva = 200
primeira_classe = 300

if passagem == 1:
    valor = 100
    if passageiros == 2:
        desconto = 0.03
    elif passageiros == 3:
        desconto =  0.04
    else:
        desconto = 0.05

elif passagem == 2:
    valor = 200
    if passageiros == 2:
        desconto = 0.05
    elif passageiros == 3:
        desconto = 0.07    
    else:
        desconto = 0.08

elif passagem == 3:
    valor = 300
    if passageiros == 2:
        desconto = 0.1
    elif passageiros == 3:
        desconto = 0.15
    else:
        desconto = 0.2
else:
    print(f"Seleção inválida digite novamente!")

valor_bruto = valor * passageiros
valor_desconto = valor_bruto * desconto
valor_liquido = valor_bruto - valor_desconto
valor_medio = valor_liquido / passageiros

print(f"O valor total de seu pedido é de R${valor_bruto:.2f}")
print(f"O valor de seu desconto é de R${valor_desconto:.2f} ({(desconto * 100):.0f}%)")
print(f"O valor final de seu pedido é R${valor_liquido:.2f}")
print(f"Cada passageiro pagará o valor de R${valor_medio:.2f}")

