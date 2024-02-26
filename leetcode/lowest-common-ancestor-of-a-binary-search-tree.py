# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        ancestor = root
        curr = root
        while root.val != p.val:
            stack.append(root)
            root = root.left if p.val < root.val else root.right
        stack.append(root)
        stack.reverse()
    
        def recc(root, valu, arr):
            nonlocal ancestor 
            if arr and root.val == arr[-1].val:
                ancestor = root
                arr.pop()
                if root.val == valu.val:
                    return valu
                if valu.val > root.val:
                    recc(root.right, valu, arr)
                else:
                    recc(root.left, valu, arr)
            return ancestor
        return recc(curr, q, stack)
        



        