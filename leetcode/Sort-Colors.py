class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*(3)

        for i in range(len(nums)):
            nums[i] += 1
        
        for num in nums:
            count[num - 1] += 1
        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[index] = i
                index += 1
                count[i] -= 1

        return nums
