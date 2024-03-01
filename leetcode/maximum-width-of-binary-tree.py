from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Pair:
    def __init__(self, node, index):
        self.node = node
        self.index = index

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        ans = 0
        q = deque()  # {node, index}
        q.append(Pair(root, 1))

        while len(q) > 0:
            offset = q[0].index * 2
            ans = max(ans, q[-1].index - q[0].index + 1)
            for _ in range(len(q)):
                pair = q.popleft()
                node = pair.node
                index = pair.index
                if node.left is not None:
                    q.append(Pair(node.left, index * 2 - offset))
                if node.right is not None:
                    q.append(Pair(node.right, index * 2 + 1 - offset))

        return ans
