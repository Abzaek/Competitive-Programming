class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
       count = 0

       for i in range(len(nums) - 1):
           if nums[i] > nums[i + 1]:
               if nums[i + 1] < nums[i - 1] and i > 0:
                   nums[i + 1] = nums[i]
               else:
                    pass
               count += 1
           if count > 1:
                return False
       return True

