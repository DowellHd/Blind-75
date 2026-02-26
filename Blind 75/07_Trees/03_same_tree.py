"""
100. Same Tree
https://leetcode.com/problems/same-tree/
Difficulty: Easy

Given the roots of two binary trees p and q, check if they are the same.

Examples:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Input: p = [1,2], q = [1,null,2]
    Output: false

Constraints:
    - The number of nodes in both trees is in the range [0, 100].
    - -10^4 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Hint: Recursive comparison. Both None -> True. One None -> False.
        # Values differ -> False. Recurse on left and right subtrees.
        pass
