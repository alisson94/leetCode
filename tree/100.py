# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
            saida = True

            def percorrer(p, q):
                nonlocal saida
                if (p and not q) or (not p and q):
                    saida = False
                    return
                
                if not p and not q:
                    return

                if p.val != q.val:
                    saida = False
                
                percorrer(p.left, q.left)
                percorrer(p.right, q.right)
            
            percorrer(p, q)

            return saida