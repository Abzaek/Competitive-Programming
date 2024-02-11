class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        left = 0
        right = 0
        
        for i in range(len(nums)):
            ans[i] += nums[i]*i - left
            left += nums[i]

            ans[len(nums) - 1 - i] += right - nums[len(nums) - 1 -i]*i
            right += nums[len(nums) - 1 - i]
        return ans
            
