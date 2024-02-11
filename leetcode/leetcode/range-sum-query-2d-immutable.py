from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = []
        accumulator_row = 0
        accumulator_col = 0
        for i in matrix:
            self.prefix_sum.append([0]*len(i))
        
                    
        for i in range(len(matrix[0])):
            accumulator_row += matrix[0][i]
            self.prefix_sum[0][i] = accumulator_row
            
        for j in range(len(matrix)):
            accumulator_col += matrix[j][0]
            self.prefix_sum[j][0] = accumulator_col
        
        for j in range(1, len(matrix)):
            for i in range(1, len(matrix[0])):
                self.prefix_sum[j][i] = matrix[j][i] + self.prefix_sum[j - 1][i] + self.prefix_sum[j][i - 1] - self.prefix_sum[j - 1][i - 1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix_sum[row2][col2]
        elif row1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row2][col1 - 1]
        elif col1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row1- 1][col2] 

            
        return self.prefix_sum[row2][col2] - self.prefix_sum[row2][col1 - 1] - self.prefix_sum[row1- 1][col2] + self.prefix_sum[row1 - 1][col1 - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2