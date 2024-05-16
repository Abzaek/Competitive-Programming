class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = -1 
        r = len(arr)

        while l + 1 < r:
            mid = l + (r - l)//2

            if arr[mid] > x:
                r = mid
            else:
                l = mid
        
        while r - l <= k:

            if (r < len(arr) and arr[r] - x < x - arr[l]) or l == -1:
                r += 1
            else:
                l -= 1

        return arr[l + 1:r]
        

        