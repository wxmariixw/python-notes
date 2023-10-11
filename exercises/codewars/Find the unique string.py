def find_uniq(arr):
    count_dict = {}
    lista = []
    print(arr)
    for i in arr:
        i.replace(' ', '')
        if len(i) <= 1:
            arr.remove(i)

        for c in i:
            count_dict[c] = count_dict.get(c, 0) + 1
            lista.append(count_dict)
    print(lista)
        # print(count_dict)

    print(arr)
        
    #     count_dict[i] = count_dict.get(i, 0) + 1
        
    # for key, value in count_dict.items():
    #     if value == 1:
    #         return key

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])