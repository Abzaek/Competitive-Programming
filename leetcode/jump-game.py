class Solution:
  def canJump(self, nums: List[int]) -> bool:
    i = 0
    reach = 0

    while i < len(nums) and i <= reach:
      reach = max(reach, i + nums[i])
      i += 1

    return i == len(nums)
        # hshmp = {}
        # if len(nums) != 1 and nums[0] == 0:
        #     return False

        # tsumm = 0
        # count = 0
        # for i in range(len(nums) - 1):
        #     summ = 0
        #     if nums[i] == 0:
        #         summ += i
        #         for j in range(i):
        #             if nums[j] + j <= i:
        #                 count += 1
        #         tsumm += summ
        #         if count == summ:
        #             return False
        # return True
       
        
        
        
        

        