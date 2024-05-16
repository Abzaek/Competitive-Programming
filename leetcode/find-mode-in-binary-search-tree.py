# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lookup = defaultdict(int)
        _max = []
        def recc(r):
            nonlocal lookup
            if not r:
                return
            recc(r.right)
            lookup[r.val] += 1
            recc(r.left)
        recc(root)
        for i in lookup.keys():
            if not _max:
                _max.append(i)
            elif lookup[i] == lookup[_max[-1]]:
                _max.append(i)
            elif lookup[i] > lookup[_max[-1]]:
                while _max:
                    _max.pop()
                _max.append(i)
        return _max


        