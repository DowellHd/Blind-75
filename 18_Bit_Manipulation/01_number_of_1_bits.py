"""
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
Difficulty: Easy

Given a positive integer, return the number of set bits (1-bits) in its
binary representation (Hamming weight).

Examples:
    Input: n = 11 (binary: 1011)
    Output: 3

    Input: n = 128 (binary: 10000000)
    Output: 1

Constraints:
    - 1 <= n <= 2^31 - 1
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Hint: n & (n - 1) removes the lowest set bit.
        # Count how many times you can do this before n becomes 0.
        pass
