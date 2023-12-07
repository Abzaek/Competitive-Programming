class Solution:
    def totalMoney(self, n: int) -> int:
       summ = (n //7)*28 

       for i in range(n//7):
           summ += 7*(i)
        
       for i in range(n % 7):
            summ += (n // 7) + 1 + i
        
       return summ
        


        
        