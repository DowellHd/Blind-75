"""
322. Coin Change
https://leetcode.com/problems/coin-change/
Difficulty: Medium

Given coin denominations and a target amount, return the fewest coins needed.
Return -1 if impossible. Infinite supply of each coin.

Examples:
    Input: coins = [1,2,5], amount = 11
    Output: 3  (5+5+1)

    Input: coins = [2], amount = 3
    Output: -1

Constraints:
    - 1 <= coins.length <= 12
    - 1 <= coins[i] <= 2^31 - 1
    - 0 <= amount <= 10^4
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Hint: Bottom-up DP. dp[0] = 0, dp[i] = infinity initially.
        # For each amount i, for each coin: dp[i] = min(dp[i], dp[i-coin] + 1).
        # Return dp[amount] if not infinity, else -1.
        pass
