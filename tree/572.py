# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        #tentando fazer sol com stack, deu certo, fica muito mais rapido
        
        def igual(p, q):
            stack = [(p,q)]

            while stack:
                (p, q) = stack.pop()
                if p and not q:
                    return False
                
                if not p and q:
                    return False
                
                if not p and not q:
                    continue
                
                if p.val == q.val:
                    stack.append((p.left, q.left))
                    stack.append((p.right, q.right))
                    continue

                return False

            return True

        stack = [root]

        while stack:
            p = stack.pop()

            if igual(p, subRoot):
                return True
            
            if p:
                stack.append(p.left)
                stack.append(p.right)

        return False

        