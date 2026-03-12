def reverse(x: int) -> int:
    str_int = str(x)

    if str_int[0] == '-':
        str_int = '-' + str_int[:0:-1]

    else:
        str_int = str_int[::-1]

    novo_int = int(str_int)

    if novo_int < -2**31 or novo_int > 2**31 - 1:
        return 0

    return novo_int
    