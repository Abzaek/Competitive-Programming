# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def traverse(rt):
            if not rt:
                return

            traverse(rt.left)
            arr.append(rt.val)
            traverse(rt.right)
        traverse(root)

        def construct(lst):
            if not lst:
                return None
            m = len(lst)//2

            rt = TreeNode(lst[m])
            rt.right = construct(lst[m + 1:])
            rt.left = construct(lst[:m])
            return rt
        return construct(arr)