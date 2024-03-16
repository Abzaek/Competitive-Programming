class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def good(val):
            acc = 0
            count = 1
            for weight in weights:
                acc += weight
                if acc > val:
                    acc = weight
                    count += 1
            if val == 3:
                print(count)
            return count <= days
        
        l = max(weights) - 1
        r = sum(weights)

        while l + 1 < r:
            mid = l + (r - l)//2

            if good(mid):
                r = mid
            else:
                l = mid
        return(r)

        