"""
371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/
Difficulty: Medium

Calculate the sum of two integers a and b without using + or -.

Examples:
    Input: a = 1, b = 2
    Output: 3

    Input: a = 2, b = 3
    Output: 5

Constraints:
    - -1000 <= a, b <= 1000
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Hint: Use bit manipulation.
        # XOR gives sum without carry: a ^ b
        # AND + left shift gives carry: (a & b) << 1
        # Repeat until carry is 0.
        # In Python, handle negative numbers with a 32-bit mask.
        pass
