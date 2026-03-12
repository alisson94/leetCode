# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        maior_caminho = 0
        def altura(tree):
            if not tree:
                return 0

            hl = altura(tree.left)
            hr = altura(tree.right)

            print(hl)
            print(hr)

            if hl + hr > maior_caminho:
                maior_caminho = hr + hl 

            return( max(hl,hr) + 1 )
        
        return maior_caminho

