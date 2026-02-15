"""
139. Word Break
https://leetcode.com/problems/word-break/
Difficulty: Medium

Given a string s and a dictionary of strings wordDict, return true if s can
be segmented into a space-separated sequence of dictionary words.

Examples:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

Constraints:
    - 1 <= s.length <= 300
    - 1 <= wordDict.length <= 1000
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Hint: DP. dp[i] = True if s[:i] can be segmented.
        # dp[0] = True. For each i, check all j < i:
        # if dp[j] and s[j:i] in word_set, then dp[i] = True.
        pass
