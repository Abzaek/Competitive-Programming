class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxmm = max(candies)
        ans = []

        for i in candies:
            ans.append(i + extraCandies >= maxmm)

        return ans