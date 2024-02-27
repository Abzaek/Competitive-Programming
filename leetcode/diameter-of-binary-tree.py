# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = float('-inf')
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        def recc(r):
            if not r: return 0
            
            l = recc(r.left)
            r = recc(r.right)

            self.max = max(self.max, l + r)
            return max(r, l) + 1
        recc(root)

        return self.max




        
        

            
