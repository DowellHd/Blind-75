"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium

Given a string s, find the length of the longest substring without
repeating characters.

Examples:
    Input: s = "abcabcbb"
    Output: 3  ("abc")

    Input: s = "bbbbb"
    Output: 1  ("b")

    Input: s = "pwwkew"
    Output: 3  ("wke")

Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hint: Sliding window with a set. Expand right pointer, adding chars.
        # When a duplicate is found, shrink from the left until no duplicate.
        # Track max window size.
        pass
