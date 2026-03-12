from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tempo = []

        for i in range(len(position)):
            _tempo = (target - position[i]) / speed[i]

            #if _tempo not in tempo:
            tempo.append(_tempo)

        return tempo
    

s = Solution()

print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))