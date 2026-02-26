"""
91. Decode Ways
https://leetcode.com/problems/decode-ways/
Difficulty: Medium

A message of letters A-Z is encoded as numbers: 'A' -> "1", ..., 'Z' -> "26".
Given a digit string s, return the number of ways to decode it.

Examples:
    Input: s = "12"
    Output: 2  ("AB" or "L")

    Input: s = "226"
    Output: 3  ("BZ", "VF", "BBF")

    Input: s = "06"
    Output: 0  (leading zero invalid)

Constraints:
    - 1 <= s.length <= 100
    - s contains only digits and may contain leading zeros.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # Hint: DP. dp[i] = ways to decode s[:i].
        # If s[i-1] is 1-9, add dp[i-1]. If s[i-2:i] is 10-26, add dp[i-2].
        # Handle '0' carefully - it can't stand alone.
        pass
