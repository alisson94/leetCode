# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):

        def inv2(root):
            if not root:
                return
            
            temp = root.left
            root.left = root.right
            root.right = temp

            inv2(root.left)
            inv2(root.right)
        
        return root

        def inv(root):
            temp = root.left
            root.left = root.right
            root.right = temp
            if root.left:
                inv(root.left)
            if root.right:
                inv(root.right)
        
        return root
