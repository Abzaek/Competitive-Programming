class Solution:
    def isHappy(self, n: int) -> bool:
        
        while True:
            if n == 1:
                return True
            elif n == 4:
                return False
            else:
                n = sum([int(i)**2 for i in str(n)])
            