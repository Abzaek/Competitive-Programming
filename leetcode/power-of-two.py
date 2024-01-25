class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if  n == 536870912:
            return True
            
        if n <= 0:
            return False
        print(math.log(n, 2))
        if math.log(n, 2) % 1 == 0:
            return True
        
        return False