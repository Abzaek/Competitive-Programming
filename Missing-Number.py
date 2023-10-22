class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in nums:
            if i != count:
                return count
            count = count + 1
        return count
