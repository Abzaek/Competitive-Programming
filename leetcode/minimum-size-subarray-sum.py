class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        summ = 0
        l = 0

        for i in range(len(nums)):
            summ += nums[i]

            while summ >= target:
                ans = min(ans, i - l + 1)
                summ -= nums[l]
                l += 1
        return 0 if ans == len(nums) + 1 else ans


            


    