from typing import List


# Runtime O(n) and space complexity O(1)
class Solution:
    def maxProfit_dp(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy_price = prices[0]
        max_profit = 0
        for price in prices:
            buy_price = min(buy_price, price)
            max_profit = max(max_profit, price - buy_price)

        return max_profit


"""
Runtime: O(n)
Space: O(1)

Runtime: 64 ms, faster than 61.89% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.9 MB, less than 73.56% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
