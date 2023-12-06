class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1, 0, -1):
            if self.is_triangle(nums[i], nums[i - 1], nums[i - 2]):
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0


    def is_triangle(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False
        