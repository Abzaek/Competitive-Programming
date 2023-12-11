from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        hshmp = {}

        for i, num in enumerate(nums):
            hshmp[num] = i
        
        for i, j in operations:
            index = hshmp[i]

            nums[index] = j
            hshmp[j] = index

            del hshmp[i]
        return nums 
        