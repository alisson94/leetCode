
def max(lista):
    if len(lista) == 1:
        return lista[0]

    if lista[0] > max(lista[1:]):
        return lista[0]

    return max(lista[1:])
    

print(max([4,3,4,2]))

