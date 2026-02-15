"""
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
Difficulty: Medium

Given a string s, return the number of palindromic substrings in it.

Examples:
    Input: s = "abc"
    Output: 3  ("a", "b", "c")

    Input: s = "aaa"
    Output: 6  ("a", "a", "a", "aa", "aa", "aaa")

Constraints:
    - 1 <= s.length <= 1000
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Hint: Expand around each center (2n-1 possible centers for odd
        # and even lengths). Count each valid expansion as a palindrome.
        pass
