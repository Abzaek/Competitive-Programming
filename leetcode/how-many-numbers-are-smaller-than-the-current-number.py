class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maxMum = float('-inf')
        ans = []
         
        for num in nums:
             if num > maxMum:
                 maxMum = num

        lst = [0]*(maxMum + 1)

        for num in nums:
            lst[num] += 1
        prefixSum = [lst[0]]

        for i in range(1, len(lst)):
            prefixSum.append(prefixSum[i - 1] + lst[i])

        for num in nums:
            if num == 0:
                ans.append(0)
                continue    
            ans.append(prefixSum[num - 1])
        return ans

            


            
