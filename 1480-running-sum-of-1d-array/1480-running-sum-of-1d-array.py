class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0
        
        for i, item in enumerate(nums):
            nums[i] = item + runningSum
            runningSum = nums[i]
        return nums
            