# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        hash = dict()

        while head.next is not None:
            if head in hash:
                return True

            hash[head] = 0
            head = head.next
        
        return False

s = Solution()

s.hasCycle