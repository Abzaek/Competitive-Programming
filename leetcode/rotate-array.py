class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hshmp = {}
        if len(nums) == 1:
            return
        for i in range(len(nums)):
            hshmp[i] = nums[i - k % len(nums)]

        for i in range(len(nums)):
            nums[i] = hshmp[i] 
        
        