# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def compare(left, right):
            if not right and not left:
                return True
            elif not right or not left:
                return False
            
            return (left.val == right.val and 
                    compare(left.left, right.right) and
                    compare(left.right, right.left))
        return compare(root.left, root.right)
        