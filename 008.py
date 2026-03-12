def myAtoi(s: str) -> int:
    if s == '' or s.isspace():
        return 0

    b = s.strip()

    neg = False
    if b[0] == '-':
        b = b[1:]
        neg = True
    elif b[0] == '+':
        b = b[1:]

    if b.isalpha():
        return 0
    
    def final(num):
        int_saida = int(num)
        if neg:
            int_saida *= -1
    
        if int_saida < -2**31:
            return -2**31
        
        if int_saida > 2**31 - 1:
            return 2**31 -1
        
        return int_saida

    if b.isdigit():
        return final(b)

    str_saida = ''
    for i in range(len(b)):
        if not b[i].isdigit():
            break
        
        str_saida += b[i]
    
    if str_saida == '':
        return 0
    else:
        return final(str_saida)

