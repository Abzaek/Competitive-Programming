class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        arr = list(map(len, s.split()))
        ans = [""]*max(arr)

        arr2 = s.split()

        for i in range(len(arr)):
            for j in range(arr[i]):
                ans[j] += arr2[i][j]
            j = arr[i]
            while j < len(ans):
                ans[j] += " "
                j += 1
        return [i.rstrip() for i in ans]
            

            
        return ans
            
            






        