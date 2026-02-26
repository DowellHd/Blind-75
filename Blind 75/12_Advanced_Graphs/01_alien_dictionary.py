"""
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/
Difficulty: Hard

There is a new alien language that uses the English alphabet but with a
different order. Given a list of words sorted lexicographically by the rules
of this new language, derive the order of letters.

Examples:
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

    Input: words = ["z","x"]
    Output: "zx"

    Input: words = ["z","x","z"]
    Output: ""  (invalid order)

Constraints:
    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 100
    - words[i] consists of only lowercase English letters.
"""

from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Hint: Compare adjacent words to extract ordering rules (edges).
        # Build a directed graph. Topological sort (BFS/Kahn's or DFS).
        # If cycle detected, return "". Watch for edge case: ["abc","ab"]
        # is invalid (prefix comes after longer word).
        pass
