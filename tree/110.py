# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        saida = 1
        def altura(tree):
            nonlocal saida
            if not tree:
                return 0

            left_h = altura(tree.left)
            right_h = altura(tree.right)

            if abs(left_h - right_h) > 1:
                saida = 0

            return max(left_h,right_h) + 1 
        
        altura(root)
        
        return saida == 1