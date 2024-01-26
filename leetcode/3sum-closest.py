class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        _sum = sum(nums[:3])
        
        for i in range(len(nums) -2):
            l = i + 1
            r = len(nums) - 1
            
            while r > l:
                currSum = nums[i] + nums[l] + nums[r]
                _sum = currSum if abs(currSum - target) < abs(_sum - target) else _sum             
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    return currSum
            
        return _sum




        