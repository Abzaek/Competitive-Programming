import numpy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       ans = []
       def backtrack(left, right, arr):
           nonlocal ans
           nonlocal k 
           if len(arr) == k:
               ans.append(numpy.copy(arr))
               return 

           for i in range(left, right + 1):
               arr.append(i)
               backtrack(i + 1, right, arr)
               arr.pop()
       backtrack(1, n, [])
       return ans


            
            

            
        