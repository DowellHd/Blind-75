"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium

Given the root of a binary tree, return the level order traversal of its
nodes' values (left to right, level by level).

Examples:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Input: root = [1]
    Output: [[1]]

Constraints:
    - The number of nodes is in the range [0, 2000].
    - -1000 <= Node.val <= 1000
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Hint: BFS with a queue. For each level, record queue size, then
        # pop that many nodes, collecting values and enqueuing children.
        pass
