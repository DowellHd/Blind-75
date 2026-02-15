"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
Difficulty: Medium

Given two strings text1 and text2, return the length of their longest
common subsequence. A subsequence is derived by deleting some (or no)
characters without changing the relative order.

Examples:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3  ("ace")

    Input: text1 = "abc", text2 = "abc"
    Output: 3

    Input: text1 = "abc", text2 = "def"
    Output: 0

Constraints:
    - 1 <= text1.length, text2.length <= 1000
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Hint: 2D DP. If chars match: dp[i][j] = dp[i-1][j-1] + 1.
        # Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
        pass
