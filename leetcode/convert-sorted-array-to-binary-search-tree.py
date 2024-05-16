# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(l,r):
            if l >= r:
                return
            mid = (r + l)//2

            root = TreeNode(nums[mid], convert(l, mid), convert(mid + 1, r)) 

            return root
        return convert(0, len(nums))       