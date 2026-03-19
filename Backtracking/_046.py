from ast import List

class Solution:
    def permute(self, nums):
        res = []
        atual = []

        def dfs(i):
            if len(atual) >= len(nums):
                res.append(list(atual))
                return
            
            # if i >= len(nums):
            #     return

            atual.append(nums[i])
            dfs((i+1)%len(nums))
            atual.pop()
            


        dfs(0)
        return res


s = Solution()
print(s.permute([1,2,3]))