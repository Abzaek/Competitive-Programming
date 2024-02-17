import math
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _sum = nums[0]
        
        res = nums[0]
        
        for i in range(1, len(nums)):
            if (_sum + nums[i]) / (i + 1) > res:
                res = math.ceil((_sum + nums[i]) / (i + 1))
            
            _sum += nums[i]
            
        return res
                