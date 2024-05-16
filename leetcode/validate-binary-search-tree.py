# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validator(rt, upper, lower):
            if not rt:
                return True
            if rt.val >= upper or rt.val <= lower:
                return False


            low = max(lower, rt.val)
            up = min(upper, rt.val)

            return validator(rt.right, upper, low) and validator(rt.left,up, lower)
        return validator(root, float('inf'), float('-inf'))
            

            
        