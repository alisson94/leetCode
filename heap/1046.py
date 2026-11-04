import heapq

class Solution:
    def lastStoneWeight(self, stones) -> int:
        _stones = []
        for s in stones:
            heapq.heappush(_stones, (-s, s))

        while len(_stones) > 1:
            x = heapq.heappop(_stones)
            y = heapq.heappop(_stones)

            if x[1] > y[1]:
                heapq.heappush(_stones, (y[1]-x[1], x[1]-y[1]))

        if _stones:
            return _stones[0][1]

        return 0

s = Solution()
print(s.lastStoneWeight([2,3,6,2,4]))