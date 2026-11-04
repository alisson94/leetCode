
def binario(lista, num, inicio = 0, fim = None):

    if fim is None:
        fim = len(lista) - 1

    meio = (fim + inicio)//2

    if inicio > fim:
        return -1

    if lista[meio] ==  num:
        return meio

    if num > lista[meio]:
        return binario(lista, num, meio+1, fim)
    else:
        return binario(lista, num, inicio, meio-1)
    

print(binario([1,2,5,7,12,14], 11))

