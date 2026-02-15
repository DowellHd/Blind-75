"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium

Given the root of a binary tree, determine if it is a valid BST.

Examples:
    Input: root = [2,1,3]
    Output: true

    Input: root = [5,1,4,null,null,3,6]
    Output: false

Constraints:
    - The number of nodes is in the range [1, 10^4].
    - -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Hint: Recursive helper with min/max bounds (start: -inf, +inf).
        # At each node, check value is within bounds. Recurse left (update
        # max to node.val) and right (update min to node.val).
        pass
