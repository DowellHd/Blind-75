"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/
Difficulty: Easy

Reverse bits of a given 32-bit unsigned integer.

Examples:
    Input: n = 43261596 (00000010100101000001111010011100)
    Output: 964176192 (00111001011110000010100101000000)

Constraints:
    - The input is a 32-bit unsigned integer.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # Hint: Iterate 32 times. Shift result left, add last bit of n
        # (n & 1), then shift n right. result = (result << 1) | (n & 1).
        pass
