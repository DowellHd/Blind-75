"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/
Difficulty: Easy

Given an integer n, return an array ans of length n+1 where ans[i] is the
number of 1's in the binary representation of i.

Examples:
    Input: n = 2
    Output: [0,1,1]

    Input: n = 5
    Output: [0,1,1,2,1,2]

Constraints:
    - 0 <= n <= 10^5
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Hint: dp[i] = dp[i >> 1] + (i & 1).
        # Right-shift halves the number (known count) + check if last bit is 1.
        pass
