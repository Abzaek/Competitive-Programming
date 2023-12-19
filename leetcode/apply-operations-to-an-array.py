class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        pointer = 1

        while pointer < len(nums):
            if nums[pointer - 1] == nums[pointer]:
                nums[pointer - 1] *= 2
                nums[pointer] = 0
                pointer += 2
                continue
            pointer += 1
        ans = []

        for i in nums:
            if i != 0:
                ans.append(i)
        while len(ans) < len(nums):
            ans.append(0)
        return ans
        