class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_lookup = {}
        r_lookup = {}
        ans = []

        for i in range(len(nums)):
          if i == 0:
            l_lookup[i] = nums[i]
            r_lookup[len(nums) - 1 - i] = nums[len(nums) - 1]
            continue
          l_lookup[i] = l_lookup[i -1]*nums[i]
          r_lookup[len(nums) - 1 - i] = r_lookup[len(nums) - i]* nums[len(nums) - 1 - i]
        for i in range(len(nums)):
          if i == 0 and i < len(nums) - 1:
            ans.append(r_lookup[1])
            continue
          elif i == len(nums) - 1:
            ans.append(l_lookup[len(nums) - 2])
            continue
          ans.append(l_lookup[i - 1]*r_lookup[i + 1])
        
        return ans
          