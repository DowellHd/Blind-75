"""
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
Difficulty: Medium

Given n nodes (0 to n-1) and a list of undirected edges, return the number
of connected components.

Examples:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1

Constraints:
    - 1 <= n <= 2000
    - 1 <= edges.length <= 5000
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Hint: Union-Find (Disjoint Set Union). Initialize n components.
        # For each edge, union the two nodes. Count remaining components.
        # Alternative: DFS/BFS counting connected components.
        pass
