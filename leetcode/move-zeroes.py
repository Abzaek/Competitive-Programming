class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        where do initialize both pointers

        """

        l = 0
        r = 0

        while r < len(nums):
            if l > r:
                r = l + 1
                continue
            if nums[r] == 0:
                r += 1
                continue
            if nums[l] != 0:
                l += 1
                continue
            
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r += 1
            
                    

        

        
        
        