def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    str_num = str(x)

    if str_num == str_num[::-1]:
        return True
    
    return False

#desafio: resolver sem tranformar em str, OBS: TENTAR FAZER DENOVO
def isPalindromeNotString(x: int) -> bool:
    if x < 0:
        return False
    
    copia = x

    #while copia > 0:

    
