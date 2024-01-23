class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        _sum = 0

        for i in range(0, len(nums), 2):
            _sum += nums[i]
        return _sum 

        