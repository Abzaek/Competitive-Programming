class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_prefix = [0]*len(nums)
        right_prefix = [0]*len(nums)
        ans = [0]*len(nums)

        for i in range(len(nums)):
            left_prefix[i] += left_prefix[i - 1] + nums[i]
            right_prefix[len(nums) - 1 - i] += right_prefix[(len(nums) - i)%len(nums)] + nums[len(nums) - 1 - i] 
       
        for i in range(len(nums)):
            if i == 0:
                ans[i] = right_prefix[i + 1] - nums[i]*(len(nums) - 1 - i)
                continue
            elif i == len(nums) - 1:
                ans[i] = nums[i]*i - left_prefix[i - 1]
                continue
            ans[i] += right_prefix[i + 1] - nums[i]*(len(nums) - 1 - i)
            ans[i] += nums[i]*i - left_prefix[i - 1]
        return ans
            
