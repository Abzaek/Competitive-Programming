class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        p_sum = list(accumulate(nums))
        largest_sum = float('-inf')
        _min = 0

        r = 0
        while r < len(p_sum):
            if max(largest_sum, p_sum[r] - _min) == p_sum[r] - _min:
                largest_sum = p_sum[r] - _min

            if _min > p_sum[r]:
                _min = p_sum[r]
            r += 1

        return largest_sum


