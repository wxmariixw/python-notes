'''
A atividade consistia em criar um sistema que calculasse o bonus de cliente
de acordo com o tipo de plano escolhido e o faturamento anual

- O plano Basic recebe 30% de bônus
- O plano Silver recebe 20% de bônus
- O plano Gold recebe 10% de bônus
- O plano Platinum recebe 5% de bônus

Caso a opção digitada não existe é necessário digitar outra opção
'''
print("---Cálculo do bônus---");
print("Qual seu tipo de assinatura?")
assinatura = float(input("1- Basic \n2- Silver \n3- Gold \n4- Platinum"));
faturamento_anual = float(input("Qual seu faturamento anual?"));

if assinatura == 1:
    valor_bonus = faturamento_anual * 0.3
    print(f"O bônus a ser pago é R${valor_bonus:.2f}")

elif assinatura == 2:
    valor_bonus = faturamento_anual * 0.2
    print(f"O bônus a ser pago é R${valor_bonus:.2f}")

elif assinatura == 3:
    valor_bonus = faturamento_anual * 0.1
    print(f"o bônus a ser pago é R${valor_bonus:.2f}")

elif assinatura == 4:
    valor_bonus = faturamento_anual * 0.05
    print(f"O bônus a ser pago é R${valor_bonus:.2f}")

else: print("Opção inválida, digite novamente")