class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        sub = []
        soma = 0
        ja_foi = set()

        candidates.sort()

        def dfs(i, soma_atual):
            if soma_atual == target:
                res.append(sub.copy())
                return
            if i >= len(candidates):
                return
            if soma_atual > target:
                return
            
            if candidates[i] == sub[0]:
                return

            sub.append(candidates[i])
            soma_atual += candidates[i]
            dfs(i+1, soma_atual)

            soma_atual -= candidates[i]
            sub.pop()
            dfs(i+1, soma_atual)
        
        dfs(0, soma)

        return res

s = Solution()
print(s.combinationSum2([9,2,2,4,6,1,5], 8))
