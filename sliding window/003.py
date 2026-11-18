
def lengthOfLongestSubstringBruteForce(s: str) -> int:
    tamanho = len(s)
    maior = 0

    def charJaEsta(c, substr):
        if substr.find(c) == -1:
            return False
        
        return True

    for i in range(tamanho):
        sub_str = s[i]
        for j in range(i+1, tamanho):
            if charJaEsta(s[j], sub_str):
                break
            sub_str += s[j]
            print(sub_str)
            novo_maior = len(sub_str)
            if novo_maior > maior:
                maior = novo_maior

    print(maior)

#usando set, foi muito bem
def lengthOfLongestSubstring(s: str) -> int:
    set = {s[0]}

    left = 0
    right = 1
    maior = 1

    if len(s) == 0:
        return 0

    while right < len(s):
        if s[right] not in set:
            set.add(s[right])
            right += 1
            if len(set) > maior:
                maior = len(set)
            
        else:
            set.discard(s[left])
            left += 1
        print(set)
    
    return maior

print(lengthOfLongestSubstring("pwwkew"))
