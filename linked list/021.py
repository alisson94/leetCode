# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        saida = ListNode()
        cur = saida
        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
            elif list1 != None:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        return saida.next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(5)))

s = Solution()

saida = s.mergeTwoLists(list1, list2)

while saida is not None:
    print(saida.val)
    saida = saida.next
    