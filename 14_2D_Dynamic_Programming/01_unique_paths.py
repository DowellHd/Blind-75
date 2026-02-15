"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/
Difficulty: Medium

A robot is on an m x n grid at the top-left corner. It can only move
down or right. How many unique paths are there to the bottom-right corner?

Examples:
    Input: m = 3, n = 7
    Output: 28

    Input: m = 3, n = 2
    Output: 3

Constraints:
    - 1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Hint: DP. dp[i][j] = dp[i-1][j] + dp[i][j-1].
        # First row and first column are all 1s. Can optimize to 1D array.
        pass
