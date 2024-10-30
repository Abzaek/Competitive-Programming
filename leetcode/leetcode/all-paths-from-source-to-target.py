class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = []

        n = len(graph)


        def traverse(path, curr):

            if curr == n - 1:
                ans.append(path.copy())
                return

            for node in graph[curr]:
                path.append(node)
                traverse(path, node)
                path.pop()

        traverse([0], 0)

        return ans


        