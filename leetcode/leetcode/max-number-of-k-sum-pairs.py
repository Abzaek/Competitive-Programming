class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0

        l = 0 
        r = len(nums) - 1

        while r > l:
            if sum([nums[r], nums[l]]) > k:
                r -= 1
            elif sum([nums[r], nums[l]]) < k:
                l += 1
            else:
                ans += 1
                l += 1
                r -= 1
        return ans