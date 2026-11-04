
def num_itens(lista):
    if len(lista) == 1:
        return 1

    return 1 + num_itens(lista[1:])

print(num_itens([4,3,4,2]))

