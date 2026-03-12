
def topKFrequent(nums, k: int):
    tabela = dict()

    for i in range(len(nums)):
        if nums[i] in tabela:
            tabela[nums[i]]+=1
            continue

        tabela[nums[i]] = 1

    saida = []

    tabela = sorted(tabela.items(), key=lambda item: item[1])
    print(tabela)
    for i in range(k):
        saida.append(tabela[len(tabela) - 1 - i][0])

    return saida

    
print(topKFrequent([1,1,1,2,2,3], 2))