# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        num = [None]
        def traverse(rt, cnt):
            nonlocal num
            if not rt:
                return cnt
            
            val = traverse(rt.left, cnt) + 1
            if val == k:
                num[0] = rt.val
            val = traverse(rt.right, val)

            return val
            
        traverse(root, 0)
        return num[0]



