class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def good(val):
            result = 0
            for num in nums:
                result += math.ceil(num/val)

            return result <= threshold
        
        l = 0
        r = 2**32

        while l + 1 < r:
            mid = l + (r - l)//2

            if good(mid):
                r = mid
            else:l = mid
        return r

        