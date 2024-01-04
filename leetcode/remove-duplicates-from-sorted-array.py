class Solution:
  def removeDuplicates(self, nums):
    if not nums:
        return 0  
    
    l = 0  
    r = 1  

    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
        r += 1
    return l + 1  

