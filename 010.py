def isMatch(s: str, p: str) -> bool:

    match = ''

    cursor = 0
    anterior = ''

    for i in range(len(p)):
        if p[i] == '.':
            match += s[cursor]
            anterior = p[i]
            cursor+=1

            continue

        if p[i] == '*':
            if s[cursor] == anterior or anterior == '.':
                while s[cursor] == anterior or anterior == '.':
                    match += s[cursor]
                    cursor+=1

                    if cursor >= len(s):
                        break 

                continue
            else:
                return False

        if p[i] == p[cursor]:
            match += s[cursor]
            anterior = p[i]
            cursor+=1
            
            continue

        return False

    print(match)

isMatch('ab', '.*')