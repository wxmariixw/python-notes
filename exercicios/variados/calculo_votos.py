print("Cálculo de votos")
print("Insira os votos de cada membro da equipe: ")

playstation = float(input("Quantos votos foram para playstation? "))
xbox = float(input("Quantos votos foram para xbox? "))
nintendo = float(input("Quantos votos foram para nintendo? "))

if playstation > xbox and playstation > nintendo:
    print(f"O video-game escolhido foi playstation com {playstation} votos")

elif xbox > nintendo and xbox > playstation:
    print(f"O video-game escolhido foi xbox com {xbox} votos")

else:
    print(f"O video-game escolhido foi nintendo com {nintendo} votos")
