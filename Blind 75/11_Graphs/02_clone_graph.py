"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/
Difficulty: Medium

Given a reference of a node in a connected undirected graph, return a deep
copy of the graph. Each node has a val and a list of neighbors.

Examples:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]

Constraints:
    - The number of nodes is in the range [0, 100].
    - 1 <= Node.val <= 100
    - No repeated edges or self-loops.
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # Hint: BFS or DFS with a hash map {original_node: cloned_node}.
        # For each node, create a clone and recursively clone its neighbors.
        pass
