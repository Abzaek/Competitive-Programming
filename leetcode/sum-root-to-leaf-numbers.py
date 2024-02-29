# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        def recc(node, path):
            nonlocal arr
            if node:
                path.append(node.val)
            else:
                return

            if not node.right and not node.left:
                arr.append(''.join(map(str, path)))
                path.pop()
                return

            recc(node.right, path)
            recc(node.left, path)
            path.pop()
        recc(root, [])
        return sum(list(map(int, arr)))



        