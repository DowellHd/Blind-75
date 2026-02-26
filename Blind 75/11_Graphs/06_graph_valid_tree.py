"""
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/
Difficulty: Medium

Given n nodes (0 to n-1) and a list of undirected edges, check whether
these edges make up a valid tree (connected, no cycles).

Examples:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false

Constraints:
    - 1 <= n <= 2000
    - 0 <= edges.length <= 5000
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Hint: A valid tree has exactly n-1 edges and is fully connected.
        # Union-Find: if unioning two already-connected nodes -> cycle.
        # After processing, check that there's exactly 1 component.
        pass
