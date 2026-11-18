def groupAnagrams(strs):
    
    tabela = {''.join(sorted(strs[0])): [strs[0]]}

    print(tabela)

    for i in range(1, len(strs)):
        ord = ''.join(sorted(strs[i]))
        if ord in tabela:
            tabela[ord].append(strs[i])
            continue

        tabela[ord] = [strs[i]]

    saida = []
    for chaves in tabela.keys():
        print(tabela[chaves])

    

groupAnagrams(["eat","tea","tan","ate","nat","bat"])