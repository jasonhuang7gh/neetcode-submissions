class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # DP - keep track of lowest price so far and best profit so far
        # Time: O(n) / Space: O(1)
        max_profit = 0
        min_buy = prices[0]
        for curr_price in prices:
            max_profit = max(max_profit, curr_price - min_buy)
            min_buy = min(min_buy, curr_price)
        return max_profit

        # # Sliding window - left pointer is buy day, right pointer is sell day
        # # If right is higher than left, profit is made, so update the maximum
        # # If right is lower, right becomes the new left pointer
        # # Time: O(n) / Space: O(1)
        # left, right = 0, 1
        # max_profit = 0
        # while right < len(prices):
        #     if prices[right] > prices[left]:
        #         max_profit = max(max_profit, prices[right] - prices[left])
        #     else:
        #         left = right
        #     right += 1
        # return max_profit
        

        # # Brute force - check every buy-sell pair and keep the highest profit
        # # Time: O(n^2) / Space: O(1)
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell  = prices[j]
        #         res = max(res, sell - buy)
        # return res