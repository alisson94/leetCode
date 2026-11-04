
def soma(lista):
    if len(lista) == 1:
        return lista[0]

    return lista[0] + soma(lista[1:])

print(soma([4,3,4,2]))

