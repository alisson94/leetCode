import heapq

class KthLargest:

    def __init__(self, k: int, nums):
        self.k_th = k
        self.nums = nums

        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        heapq.heappop(self.nums)

        return self.nums[0]



kth = KthLargest(3, [1, 3, 3, 2])

kth.add(3)   
kth.add(5)   
kth.add(6)   
kth.add(7)  
print(kth.add(8))