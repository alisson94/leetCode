class Solution:
    def productExceptSelf(nums):
        produto = 1
        saida = []

        for i in range(len(nums)):
            produto *= nums[i]

        for i in range(len(nums)):
            if nums[i] == 0:
                temp = 1
                for j in range(len(nums)):
                    if j != i:
                        temp *= nums[j] 
                saida.append(temp)
                continue
            
            saida.append(int(produto/nums[i]))

        return saida