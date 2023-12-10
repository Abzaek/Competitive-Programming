class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        l = 0

        while l <= r:
            mid = l + ((r - l)//2)
            square = mid**2

            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            else:
                l = mid + 1

        return round(r)                
        
        