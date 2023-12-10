class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = list([] for i in range(len(matrix[0])))
        for i in matrix:

            for j in range(len(i)):
                ans[j].append(i[j])
        return ans

        