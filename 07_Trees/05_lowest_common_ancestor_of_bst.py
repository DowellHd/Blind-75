"""
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Difficulty: Medium

Given a BST, find the lowest common ancestor of two given nodes.

Examples:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2

Constraints:
    - The number of nodes is in the range [2, 10^5].
    - All Node.val are unique.
    - p != q, both exist in the BST.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Hint: Use BST property. If both p and q < root, go left.
        # If both > root, go right. Otherwise root is the split point (LCA).
        pass
