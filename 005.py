def longestPalindrome(s: str) -> str:

    if len(s) == 1:
        return s

    #vi a solucao com prog dinamica, usando matriz, fazer sem referencia

longestPalindrome("abcdef")


    
def longestPalidromeBruteForce(s: str) -> str:
    
    if len(s) == 1:
        return s

    maior_str = s[0]

    for i in range(len(s)):
        str_atual = s[i]
        palidromo_atual = str_atual

        for j in range(i+1, len(s)):
            str_atual += s[j]
            palidromo_atual = s[j] + palidromo_atual

            if str_atual == palidromo_atual:
                if len(str_atual) > len(maior_str):
                    maior_str = str_atual
    
    return maior_str

#print(longestPalidromeBruteForce("ac"))