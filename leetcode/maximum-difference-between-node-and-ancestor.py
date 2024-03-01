# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        max_diff = float('-inf')
        def finder(rt, mx, mn):
            nonlocal max_diff

            if not rt:
                return
            local_max = max(mx, rt.val)
            local_min = min(mn, rt.val)

            max_diff = max(local_max - local_min, max_diff)
            finder(rt.left, local_max, local_min)
            finder(rt.right, local_max, local_min)
        finder(root, root.val, root.val)
        return max_diff

            
        