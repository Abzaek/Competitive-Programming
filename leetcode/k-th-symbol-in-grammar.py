class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def recc(row, col):
            if row == 1:
                return 0

            if col == 2**(row - 1):
                if row % 2:
                    return 0
                else:
                    return 1
            if col == 1 or col == 4:
                return 0
            if col == 2 or col == 3 or col == 5:
                return 1
            
            clmn = None
            rw = None

            if col % 2:
                clmn = (col - 1)//2 + 1
                rw = row - 1
                
                return recc(rw, clmn)
            else:
                clmn = (col)//2 
                rw = row - 1
                return abs(1 - recc(rw, clmn))
        return recc(n, k)

