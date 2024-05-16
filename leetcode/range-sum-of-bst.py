# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def _sum(r):
            if not r:
                return 0
            if r.val < low:
                return _sum(r.right)
            elif r.val > high:
                return _sum(r.left)
            else:
                return r.val + _sum(r.right) + _sum(r.left)

        return _sum(root)