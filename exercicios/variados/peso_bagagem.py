'''
O sistema deve veriicar se o peso da bagagem é permitido
'''
print("O peso de sua bagagem é permitido?")
peso_bagagem = int(input("Qual o peso de sua bagagem? "))

if peso_bagagem <= 18:
   print ("Pode embarcar! Boa viagem!")
else:
   print("Não pode embarcar! Dirija-se ao balcão para mais informações.")