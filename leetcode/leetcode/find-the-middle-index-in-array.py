class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
      left_sum = [0]*len(nums)
      right_sum = [0]*len(nums)

      if len(nums) == 1:
        return 0
      for i in range(len(nums)):
        left_sum[i] += left_sum[i - 1] + nums[i]
        right_sum[len(nums) - 1 - i] += right_sum[(len(nums) - i)%len(nums)] + nums[len(nums) - 1 -i]
      
      if right_sum[1] == 0:
        return 0
      for i in range(1, len(nums) - 1):
        if left_sum[i - 1] == right_sum[i + 1]:
          return i
      if left_sum[len(nums) - 2] == 0:
        return len(nums) - 1

      return -1

        