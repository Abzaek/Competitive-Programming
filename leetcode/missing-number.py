class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hshtbl1 = {}
        hshtbl2 = {}

        for i in range(len(nums) + 1):
            hshtbl1[i] = 0
        for i in nums:
            hshtbl2[i] = 0
        
        for i in hshtbl1:
            if i not in hshtbl2:
                return i
        