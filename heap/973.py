import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap_points = []
        
        for p in points:
            d = sqrt(p[0]*p[0] + p[1]*p[1])
            
            heapq.heappush(heap_points, ( -d, p ))

            if len(heap_points) > k:
                heapq.heappop(heap_points)

        return [p for c, p in heap_points]


s = Solution()
print(s.kClosest([[0,2],[2,0],[2,2]], 2))
