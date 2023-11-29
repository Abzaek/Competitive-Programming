class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:len(matrix[i]) - 1] != matrix[i + 1][1:len(matrix[i])]:
                return False
        return True
        