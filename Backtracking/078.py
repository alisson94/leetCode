from ast import List

class Solution:
    def subsets(self, nums):
        resultado = []

        def back(indice, caminho):
            resultado.append(list(caminho))

            for i in range(indice, len(nums)):
                caminho.append(nums[i])

                back(i+1, caminho)

                caminho.pop()

        back(0, [])
        return resultado
    
    def subsets2(self, nums):
        res = []
        atual = []

        def dfs(i):
            if i>= len(nums):
                res.append(list(atual))
                return

            atual.append(nums[i])
            dfs(i+1)
            atual.pop()
            dfs(i+1)


        dfs(0)
        return res

    

c = Solution()

print(c.subsets([1,2,3]))