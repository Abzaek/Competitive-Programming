class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def good(val):
            acc = 0
            count = 1
            for num in nums:
                acc += num
                if acc > val:
                    acc = num
                    count += 1
            return count <= k

        l = max(nums) - 1
        r = sum(nums)

        while l + 1 < r:
            mid = l + (r - l)//2

            if good(mid):
                r = mid
            else:
                l = mid
        return(r)
        