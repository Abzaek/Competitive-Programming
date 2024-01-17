class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = 0

        for i in range(k):
           _sum += nums[i]

        if k == len(nums):
            return _sum/k
        
        max_sum = _sum
        
        for i in range(k, len(nums)):
            _sum += nums[i]
            _sum -= nums[i - k]
            max_sum = max(_sum, max_sum)


        return max_sum/k
        
       

    