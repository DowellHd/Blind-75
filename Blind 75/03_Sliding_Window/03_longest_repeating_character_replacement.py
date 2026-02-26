"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/
Difficulty: Medium

Given a string s and an integer k, you can choose any character and change
it to any other uppercase English letter at most k times. Return the length
of the longest substring containing the same letter after performing at most
k operations.

Examples:
    Input: s = "ABAB", k = 2
    Output: 4

    Input: s = "AABABBA", k = 1
    Output: 4

Constraints:
    - 1 <= s.length <= 10^5
    - s consists of only uppercase English letters.
    - 0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hint: Sliding window. Track frequency of each char in the window.
        # Window is valid when: window_size - max_frequency <= k.
        # If invalid, shrink from left. Track max window size.
        pass
