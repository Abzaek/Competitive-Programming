class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            
            profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit
