class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Sliding window - left pointer is buy day, right pointer is sell day
        # If right is higher than left, profit is made, so update the maximum
        # If right is lower, right becomes the new left pointer
        # Time: O(n) / Space: O(1)
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_profit
        

        # # Brute force - check every buy-sell pair and keep the highest profit
        # # Time: O(n^2) / Space: O(1)
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell  = prices[j]
        #         res = max(res, sell - buy)
        # return res