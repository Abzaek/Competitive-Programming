class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        right = 0
        lookup = defaultdict(int)
        lookup[0] += 1
        acc = 0
        ans = 0
       
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0
            nums[i] = acc + nums[i]
            acc = nums[i]
        
        while right < len(nums):
          
            lookup[nums[right]] += 1
            if nums[right] - k in lookup:
                ans += lookup[nums[right] - k] 
            right += 1
            
        
        return ans
                
           
                    
      