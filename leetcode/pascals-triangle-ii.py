class Solution:
    def __init__(self):
        self.dict = {}
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        def pascal(row, index):
            nonlocal arr
            curr  = 0
            for i in range(index):
                acc = recc(row - 1, i)
                arr.append(curr + acc)
                curr = acc
        def recc(row, index):
            if not row or not index or row == index:
                return 1
            
            if (row, index) not in self.dict:
                x = recc(row - 1, index - 1) 
                y = recc(row - 1, index)
                self.dict[(row, index)] = x + y
                return x + y
            else:
                return self.dict[(row, index)]

        pascal(rowIndex, rowIndex + 1)
        if arr:
            arr[-1] = 1
        return arr
        
        
        