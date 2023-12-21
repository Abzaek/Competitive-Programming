'''
[[1,2,3], [4,5,6], [7,8,9]]
OUTPUT: [1, ]
'''


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []

        col = 0
        row = 0
        k = 0
        up = True
        while len(ans) < len(mat) * len(mat[0]):

            if up:
                while col < len(mat[0]) and row > -1:
                    ans.append(mat[row][col])
                    col += 1
                    row -= 1
                if col == len(mat[0]) and row == -1:
                    col = len(mat[0]) - 1
                    row = 1
                elif col == len(mat[0]):
                    col = len(mat[0]) - 1
                    row += 2
                elif row == -1:
                    row = 0
                if col == len(mat[0]) and row == -1:
                    col = len(mat[0]) - 1
                    row = 0
                up = False
            else:
                while col > -1 and row < len(mat):
                    ans.append(mat[row][col])
                    col -= 1
                    row += 1
                if col == -1 and row == len(mat):
                    col = 1
                    row = len(mat) - 1
                elif col == -1:
                    col = 0
                elif row == len(mat):
                    row = len(mat) - 1
                    col += 2
            
                up = True
        return ans
        

        
        

        
