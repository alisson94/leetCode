class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = sorted(nums)
        left = 0
        right = 0
        maior = 1

        while right < (len(nums) - 1):
            if nums[right + 1] == nums[right] + 1:
                right += 1
                if right - left + 1 > maior:
                    maior = right - left + 1
            else: 
                left = right

        print(maior)

s = Solution()
s.longestConsecutive([100,4,200,1,3,2])