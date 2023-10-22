class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = list(x)
        y = ''
        if x[0] == '-':
            for i in range(len(x) - 1):
                y = y + x[len(x) - (i + 1)]
            y = '-' + y
        else: 
            for i in range(len(x)):
                y = y + x[len(x) - (i + 1)]
        if int(y) < (-(2**31)) or int(y) > ((2**31) - 1):
            return 0
        return int(y)
