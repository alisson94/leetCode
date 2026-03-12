class Solution:
    def isValid(self, s: str) -> bool:
        lista = list(s)
        direita = []
        while len(lista) > 0:
            ultimo = lista.pop()
            if ultimo == ')' or ultimo == ']' or ultimo == '}':
                direita.append(ultimo)
                continue
            
            if len(direita) == 0:
                return False

            if ultimo == '(':
                if direita.pop() != ')':
                    return False
                
                continue

            if ultimo == '[':
                if direita.pop() != ']':
                    return False
                continue
            if ultimo == '{':
                if direita.pop() != '}':
                    return False
                continue
        
        if len(direita) == 0:
            return True
        return False
