class Solution:
    def evalRPN(self, tokens) -> int:
        numeros = []
        sim_operadores = '+-*/'
        
        def operacao(a, b, oper):
            operadores = {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b
            }

            return int(operadores[oper](a, b))

        for token in tokens:
            if token in sim_operadores:
                num1 = numeros.pop()
                num2 = numeros.pop()

                numeros.append(operacao(num2, num1, token))
                continue

            numeros.append(int(token))
        
        print(numeros)
        return numeros[-1]
    
s = Solution()

print(s.evalRPN(["25","5", "/"]))