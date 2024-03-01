# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def dandc(arr):
            if not arr:
                return None
            
            largest_val = arr[0]
            index = 0
            for i in range(1, len(arr)):
                if arr[i] > largest_val:
                    largest_val = arr[i]
                    index = i
            root = TreeNode(largest_val)

            root.right = dandc(arr[index + 1:])
            root.left = dandc(arr[:index])
            return root
        return dandc(nums)