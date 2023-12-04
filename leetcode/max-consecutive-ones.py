class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxnum = 0
        currnum = 0
        if 1 not in nums:
            return 0
        for i in range(len(nums) - 1):
            if nums[i] == 1 and nums[i + 1] == 1:
                currnum += 1
                maxnum = max(currnum, maxnum)
            else:
                currnum = 0
        return maxnum + 1
        