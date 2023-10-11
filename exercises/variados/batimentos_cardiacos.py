'''
Neste exercício preciso criar um sistema que indique se os batimentos cardíacos da pessoa estão dentro dos conformes:

Se a pessoa tiver idade = ou > a 60 anos os batimentos devem estar entre 60 e 50;
Se a pessoa tiver idade = ou > a 18 anos os batimentos devem estar entre 80 e 70;
Se a pessoa tiver idade = ou > a 08 anos os batimentos devem estar entre 100 e 80;
Se a pessoa tiver idade até 7 anos os batimentos devem estar entre 140 e 120;
'''

print("Vamos verificar seus batimentos cardíacos!")

idade = float(input("Informe sua idade: "))
batimentos = float(input("Informe seus batimentos cardíacos: "))

batimentosAltos = "Seus batimentos estão acima do esperado!"
batimentosBons = "Seus batimentos estão ótimos"
batimentosBaixos = "Seus batimentos estão abaixo do esperado!"

if idade >= 60:
    if batimentos >= 61:
        print(batimentosAltos);
    elif batimentos >= 51:
        print (batimentosBons);
    else:
        print (batimentosBaixos);
elif idade >= 18:
    if batimentos >= 81:
        print(batimentosAltos);
    elif batimentos >= 71:
        print (batimentosBons);
    else:
        print(batimentosBaixos);
elif idade >= 8:
    if batimentos >= 101:
        print(batimentosAltos);
    elif batimentos >= 81:
        print (batimentosBons);
    else:
        print(batimentosBaixos);
else:
    if batimentos >= 141: print(batimentosAltos);
    elif batimentos >= 121: print (batimentosBons);
    else: print(batimentosBaixos);