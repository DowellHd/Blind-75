"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/
Difficulty: Easy

Given the roots of two binary trees root and subRoot, return true if there
is a subtree of root with the same structure and node values of subRoot.

Examples:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

Constraints:
    - The number of nodes in root is in the range [1, 2000].
    - The number of nodes in subRoot is in the range [1, 1000].
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Hint: For each node in root, check if the subtree rooted there
        # matches subRoot using a isSameTree helper. Recurse on left and right.
        pass
