"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
Difficulty: Hard

Given two strings s and t, return the minimum window substring of s such
that every character in t (including duplicates) is included in the window.

Examples:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

    Input: s = "a", t = "a"
    Output: "a"

    Input: s = "a", t = "aa"
    Output: ""

Constraints:
    - 1 <= s.length, t.length <= 10^5
    - s and t consist of uppercase and lowercase English letters.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Hint: Sliding window with two hash maps (need vs have). Expand right
        # to include chars, shrink left when all chars are satisfied.
        # Track the minimum valid window.
        pass
