instructions = input("Selecione uma opção: \n \n [1] - Adicionar item \t [2] - Deletar item \t [3] - Mostrar lista \n \n \t Para sair digite 'Sair' \t")

lista = []

while instructions != "sair":
    if instructions == "1":
        # Adicionar item na lista
        item = input("Digite o nome do item que você quer adicionar: \n \t Para voltar digite 'Sair'")

        if item != "sair":
            lista.append(item)
        else:
            break

    elif instructions == "2":
        # Tirar item da lista
        typeDelete = input("Você quer deletar por nome ou por indice? \n \n [1] - Nome \t [2] - Indice \n \t Para voltar ao menu inicial digite 'Voltar'")

        if typeDelete == "1":
            item = input("Digite o nome do item que você quer excluir:")
            lista.remove(item.lowercase)

        elif typeDelete == "2":
            item = int(input("Digite o indice do item que você quer excluir:"))
            lista.pop(item)        

        elif typeDelete.lowercase == "voltar":
            break

        else:
            print("Opção inválida")
            
    elif instructions == "3":
        # Listar itens
        print(lista)
        break
    else:
        # Caso a opção seja inválida
        print("Opção inválida")
        break
    