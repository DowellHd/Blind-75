"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy

Given the root of a binary tree, return its maximum depth (number of nodes
along the longest path from root to farthest leaf).

Examples:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Input: root = [1,null,2]
    Output: 2

Constraints:
    - The number of nodes is in the range [0, 10^4].
    - -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Hint: Recursive DFS: return 1 + max(maxDepth(left), maxDepth(right)).
        # Base case: None returns 0.
        pass
