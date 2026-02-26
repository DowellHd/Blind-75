"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Difficulty: Medium

Given the root of a BST, and an integer k, return the kth smallest value
(1-indexed).

Examples:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

Constraints:
    - 1 <= k <= n <= 10^4
    - 0 <= Node.val <= 10^4
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Hint: Inorder traversal of BST visits nodes in ascending order.
        # Use iterative inorder with a stack. Decrement k each pop;
        # when k == 0, return that node's value.
        pass
