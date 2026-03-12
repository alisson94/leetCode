def isAnagram(s: str, t: str) -> bool:
    if len(s)!= len(t):
        return False
    tabela = dict()

    for i in range(len(s)):
        if s[i] in tabela:
            tabela[s[i]]+=1
        else:
            tabela[s[i]]=1

    for i in range(len(t)):
        if t[i] in tabela:
            if tabela[t[i]] == 1:
                del tabela[t[i]]
                continue

            tabela[t[i]]-=1
            continue

        return False

    return True  