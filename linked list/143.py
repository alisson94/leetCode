# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        reversed = None
        while head != None:
            aux = head
            head = head.next
            aux.next = reversed
            reversed = aux

        return reversed

    def reorderList(self, head) -> None:
        #   PRIMEIRA SOLUÇÃO, MUITO TEMPO DE EXEC
        # it = head
        # while it.next:
            
        #     aux = it.next
        #     ultimo = aux

        #     aux2 = ultimo
        #     while ultimo.next:
        #         aux2 = ultimo
        #         ultimo = ultimo.next

        #     if ultimo == aux:
        #         break
            
        #     aux2.next = None

        #     ultimo.next = aux

        #     it.next = ultimo
        #     it = aux

        #SEGUNDA SOLUCAO
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow = self.reorderList(slow)

        slow.next = head.next
        head.next = slow

        it = head
        while it:
            if slow.next:
                aux = slow.next
            slow.next = it.next
            it.next = slow

            it = slow.next
            slow = aux

    



l = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

s = Solution()
s.reorderList(l)

while l:
    print(l.val)
    l = l.next