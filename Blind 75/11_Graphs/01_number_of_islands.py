"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
Difficulty: Medium

Given an m x n 2D grid of '1's (land) and '0's (water), return the number
of islands. An island is surrounded by water and formed by connecting
adjacent lands horizontally or vertically.

Examples:
    Input: grid = [["1","1","0","0","0"],
                   ["1","1","0","0","0"],
                   ["0","0","1","0","0"],
                   ["0","0","0","1","1"]]
    Output: 3

Constraints:
    - m == grid.length, n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Hint: Iterate through cells. When you find a '1', increment count
        # and DFS/BFS to mark all connected '1's as visited (set to '0').
        pass
