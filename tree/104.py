# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        
        def altura(tree):
            if not tree:
                return 0

            return( max(altura(tree.left),altura(tree.right)) + 1 )

        return altura(root)