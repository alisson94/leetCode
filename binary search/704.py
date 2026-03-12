class Solution:
    def search(self, nums, target: int) -> int:
        inicio = 0
        fim = len(nums) - 1

        while inicio < fim:
            meio = int((inicio + fim)/2)
            if nums[meio] == target:
                return meio
            
            print(f"inicio {inicio}")
            print(f"fim {fim}")

            if target > nums[meio]:
                inicio = meio + 1
                continue
            if target < nums[meio]:
                fim = meio
                continue
        
        return -1
    
s = Solution()

s.search([-1, 0,2,4,6,8], 3)