class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0

        while True:
            if n == 1:
                return count

            if n % 2 == 0:
                count += n//2
                n = n//2
            else:
                count += (n - 1)//2
                n = (n - 1)//2 + 1

            
            
            
        
            
        