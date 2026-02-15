"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

Given an array prices where prices[i] is the price on the ith day,
find the maximum profit from one buy and one sell (buy before sell).

Examples:
    Input: prices = [7,1,5,3,6,4]
    Output: 5  (buy at 1, sell at 6)

    Input: prices = [7,6,4,3,1]
    Output: 0  (no profitable transaction)

Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Hint: Track the minimum price seen so far. At each day, calculate
        # profit = price - min_price. Track the maximum profit.
        pass
