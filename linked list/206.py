# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        reversed = None
        while head != None:
            aux = head
            head = head.next
            aux.next = reversed
            reversed = aux

        return reversed
        
        
