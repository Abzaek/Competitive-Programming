class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
       count = 0
       k = len(set(nums))

       for i in range(len(nums)):
           s = set()

           for j in range(i, len(nums)):
               if nums[j] not in s:
                   s.add(nums[j])
               if len(s) == k:
                   count  += 1
       return count

        
        


        