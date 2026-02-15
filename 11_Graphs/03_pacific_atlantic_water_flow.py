"""
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/
Difficulty: Medium

Given an m x n matrix of heights, return a list of cells that can flow to
both the Pacific ocean (top/left edges) and Atlantic ocean (bottom/right edges).
Water flows from higher/equal cells to lower/equal adjacent cells.

Examples:
    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Constraints:
    - m == heights.length, n == heights[0].length
    - 1 <= m, n <= 200
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Hint: DFS/BFS from ocean borders *inward* (reverse flow direction).
        # Find cells reachable from Pacific and from Atlantic separately.
        # Return the intersection.
        pass
