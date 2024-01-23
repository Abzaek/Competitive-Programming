class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        _max = 1

        nums.sort()

        _max = max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
        return _max
        