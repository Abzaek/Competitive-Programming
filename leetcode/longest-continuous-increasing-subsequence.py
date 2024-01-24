class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        _max = 0

        l = 0
        r = 0

        while r < len(nums) - 1:
            
            if nums[r] >= nums[r + 1]:
                l = r + 1
            r += 1
            _max = max(_max, r - l)

        return _max + 1
