# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n 
        low = 1
        curr = 0

        while high >= low:
            mid = low + (high - low)//2

            if isBadVersion(mid):
                curr = mid
                high = mid - 1
            else:
                low = mid + 1
        return curr

        