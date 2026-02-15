"""
212. Word Search II
https://leetcode.com/problems/word-search-ii/
Difficulty: Hard

Given an m x n board of characters and a list of words, return all words
that can be found on the board. Each word must be constructed from
letters of sequentially adjacent cells (horizontal or vertical neighbors).
The same cell may not be used more than once in a word.

Examples:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
           words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Constraints:
    - m == board.length, n == board[i].length
    - 1 <= m, n <= 12
    - 1 <= words.length <= 3 * 10^4
"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Hint: Build a Trie from the word list. DFS from each cell on the
        # board, walking the Trie. When you reach end_of_word, add to results.
        # Prune Trie branches as you find words to optimize.
        pass
