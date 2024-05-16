# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lookup = defaultdict(list)

        def recc(node, position):
            if node:
                lookup[position[1]].append([position[0], node.val])
            else:
                return
            
            position[1] -= 1
            position[0] += 1
            recc(node.left, position)
            position[1] += 2
            recc(node.right, position)
            position[0] -= 1
            position[1] -= 1
        recc(root, [0,0])

        keys = sorted(list(lookup.keys()))
        final = []
        for i in keys:
            final.append([k[1] for k in sorted(lookup[i])])
    
        return final

        
        

        