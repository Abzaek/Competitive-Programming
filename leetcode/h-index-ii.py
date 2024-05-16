class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def good(ind):
            if len(citations) - ind <= citations[ind]:
                return True
            return False
        
        l = -1 
        r = len(citations)

        while l + 1 < r:
            mid = l + (r - l)//2

            if good(mid):
                r = mid 
            else:
                l = mid
        return len(citations) - r

        