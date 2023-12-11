class Solution:
    from collections import Counter
    def majorityElement(self, nums: List[int]) -> int:
        hshmp = Counter(nums)
        
        for i in hshmp:
            if hshmp[i] > len(nums)//2:
                return i