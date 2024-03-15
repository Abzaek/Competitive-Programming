class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def good(val):
            count = 0
            for pile in piles:
                count += math.ceil(pile/val)
            return count <= h

        l = 1
        r = max(piles)

        while l <= r:
            mid = l + (r - l)//2

            if good(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

        