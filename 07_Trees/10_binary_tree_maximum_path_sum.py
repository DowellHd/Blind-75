"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
Difficulty: Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes has an edge. The path does not need to pass through the root.
Return the maximum path sum.

Examples:
    Input: root = [1,2,3]
    Output: 6  (path: 2 -> 1 -> 3)

    Input: root = [-10,9,20,null,null,15,7]
    Output: 42  (path: 15 -> 20 -> 7)

Constraints:
    - The number of nodes is in the range [1, 3 * 10^4].
    - -1000 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Hint: DFS returning max gain from each node (clamped to 0).
        # At each node, update global max with node.val + left_gain + right_gain.
        # Return node.val + max(left_gain, right_gain) as single-side gain.
        pass
