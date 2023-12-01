class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 3:
            if n % 3 == 2: 
                return False

            n = (n // 3) 

        return True if n != 2 else False

           