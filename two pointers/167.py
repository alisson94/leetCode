from typing import List

class Solution:
    #usando solucao equivalente ao 001
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = dict()
    
        for i in range(len(numbers)):
            elemento = numbers[i] 
            if target - elemento in hash:
                return ([hash[target - elemento] + 1, i + 1])
            
            hash[elemento] = i

    #usando solucao com two pointers
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            
            if numbers[left] + numbers[right] < target:
                left += 1
                continue

            if numbers[left] + numbers[right] > target:
                right -= 1
                continue