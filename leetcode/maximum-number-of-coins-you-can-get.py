class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        l = 0
        r = len(piles) - 2

        while r > l:
            ans += piles[r]
            r -= 2
            l += 1
            
        return ans


        