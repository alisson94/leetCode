class Solution:


    def generateParenthesis(self, n):

        def abre(s: str):
            if s.count('(') >= n:
                return
            s += '('

            if s.count('(') == n and s.count(')') == n:
                lista.append(s)
                return
            
            abre(s)
            fecha(s)

        def fecha(s: str):
            if s.count('(') <= s.count(')'):
                return
            s+= ')'

            if s.count('(') == n and s.count(')') == n:
                lista.append(s)
                return
            
            abre(s)
            fecha(s)
        
        lista = []

        s = ""
        abre(s)

        return(lista)

s= Solution()

print(s.generateParenthesis(3))