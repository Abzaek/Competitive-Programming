class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []

        for i in range(len(matrix[0])):
            temp = []
            for j in matrix:
                temp.append(j[i])
            ans.append(temp)
        return ans
