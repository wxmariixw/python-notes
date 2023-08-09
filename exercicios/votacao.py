'''
O exercicio consistia e computar os votos de cada dia e 
identificar o dia que recebeu mais votos para ser realizado as lives
'''
print("---Votação para o melhor dia de realização das lives---");

segunda = float(input("Quantos votos Segunda-feira recebeu?\n"))
terca = float(input("E quantos votos Terça-feira?\n"))
quarta = float(input("E quantos votos Quarta-feira?\n"))
quinta = float(input("E quantos votos Quinta-feira?\n"))
sexta = float(input("E quantos votos Sexta-feira?\n"))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print(f"O dia escolhido foi Segunda-Feira com {segunda} votos")

elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print(f"O dia escolhido foi Terça-Feira com {terca} votos")

elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print(f"O dia escolhido foi Quarta-Feira com {quarta} votos")

elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print(f"O dia escolhido foi Quinta-Feira com {quinta} votos")

elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print(f"O dia escolhido foi Sexta-Feira com {sexta} votos")

else:
    print(f"Houve um empate, os resultados foram {segunda} votos para Segunda-Feira,\
           {terca} votos para Terça-feira, {quarta} votos para Quarta-feira,\
              {quinta} votos para Quinta-Feira e {sexta} votos para Sexta-Feira")