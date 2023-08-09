print("Bem vindo ao jogo da Advinhação!")

numero_secreto = 42 
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou o número secreto!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        else:
            print("Você errou! O seu chute foi menor que o número secreto.")

    rodada = rodada + 1