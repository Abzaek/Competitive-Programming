class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = inf
        l = 0
        r = len(nums) - 1

        def recc(l, r):
            nonlocal min_val
            min_val = min(min_val, nums[l], nums[r])
            if l + 1 >= r:
                return
            mid = l + (r - l)//2
            recc(l, mid)
            recc(mid, r)

        recc(l, r)
        return min_val
        