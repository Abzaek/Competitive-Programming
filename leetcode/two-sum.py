class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(nums)):
            if nums[i] in lookup and 2*nums[i] == target:
                return [lookup[nums[i]], i]

            lookup[nums[i]] = i
        
        for i in nums:
            if target - i in lookup and lookup[target - i] != lookup[i]:
                return [lookup[i], lookup[target - i]]
        