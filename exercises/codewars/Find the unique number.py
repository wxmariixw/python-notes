def find_uniq(arr):
    count_dict = {} # criou um dicionário
    for i in arr:
        count_dict[i] = count_dict.get(i, 0) + 1 #atribuiu a quantidade de vezes a cada número

    for key, value in count_dict.items(): #acessou cada item dentro do dicionário
        if value == 1: #verificou qual deles tinha o value 1
            return key #retornou a key de qual tinha o value 1