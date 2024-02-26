# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lookup = defaultdict(list)

        def recc(root, row):
            if not root:
                return
            
            lookup[row].append(root.val)
            row += 1
            recc(root.left, row)
            recc(root.right, row)
            row -= 1
        recc(root, 0)

        for i in lookup.keys():
            if i % 2:
                lookup[i].reverse()

        return lookup.values()
        

        