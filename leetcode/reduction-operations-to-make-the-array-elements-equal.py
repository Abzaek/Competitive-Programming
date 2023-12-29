class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        hshmp = defaultdict(int)
        nums.sort(reverse=True)
        
        ans = 0

        for i in nums:
            hshmp[i] += 1
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            ans += hshmp[nums[i]]
            hshmp[nums[i + 1]] += hshmp[nums[i]]

        return ans
            

        