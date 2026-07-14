class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Naive Solution
        # Brute force check every buy-sell pair and keep the highest profit
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res