class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
    
        _minimum = [-1, nums[0]]
        _maximum = [-1, nums[len(nums) - 1]]

        for i in range(2, len(nums)):

            _minimum.append(min(nums[i - 1], _minimum[-1]))

            _maximum.append(max(nums[len(nums) - i], _maximum[-1]))

        _maximum.reverse()

        for i in range(1, len(nums) - 1):
            if _minimum[i] < nums[i] and nums[i] < _maximum[i]:
                return True
        
        return False


        


            
        
