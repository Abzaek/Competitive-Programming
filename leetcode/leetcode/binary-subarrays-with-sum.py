class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0]*len(nums) 
        accumulator = 0
        lookup = defaultdict(int)
        _count = 0
        lookup[0] += 1
        for i, item in enumerate(nums):
            accumulator += item
            prefix_sum[i] = accumulator
        
        for i in range(len(nums)):
            _count += lookup[prefix_sum[i] - goal]
            lookup[prefix_sum[i]] += 1

        return _count 



      