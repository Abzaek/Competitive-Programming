class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        l = 0
        r = 0
        

        while l < len(mat):
            summ += mat[l][l]
            
            l += 1
        
        l = len(mat) - 1
        while r < len(mat):
            if l == r:
                l -= 1
                r += 1
                continue
            summ += mat[r][l]
            l -= 1
            r += 1
        return summ
        