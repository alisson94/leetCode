def intToRoman(num: int) -> str:

    numeros = { 4: {0: 'IV',1: 'XL',2: 'CD'}, 9: {0: 'IX',1: 'XC',2: 'CM'} }

    saida = ''
    i = 0
    while num > 0:
        digito = num%10
        if digito == 4:
            saida += numeros[4][]