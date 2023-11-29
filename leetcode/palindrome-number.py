class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[:: -1]

        return x == y
        # x = str(x)
        
        # for i in range(len(x)//2):
        #     if x[i] != x[len(x) - 1 - i]:
        #         return False
        # return True
        