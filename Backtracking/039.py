class Solution:
    def combinationSum(self, candidates, target):
        res = []    
        sub = []
        soma = 0

        def dfs(i, soma_atual):
            if soma_atual == target:
                res.append(sub[:])
                return
            if i >= len(candidates):
                return
            if soma_atual > target:
                return
            

            print(soma_atual)
            sub.append(candidates[i])
            soma_atual += candidates[i]
            dfs(i, soma_atual)
            soma_atual -= candidates[i]
            sub.pop()
            dfs(i+1, soma_atual)
        
        dfs(0, soma)

        return res

s = Solution()
print(s.combinationSum([2,5,6,9], 9))


# 2 2 2 2 9 