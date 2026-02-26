"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Difficulty: Medium

Given two integer arrays preorder and inorder, construct and return the binary tree.

Examples:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

Constraints:
    - 1 <= preorder.length <= 3000
    - preorder and inorder consist of unique values.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hint: First element of preorder is the root. Find its index in
        # inorder to split into left and right subtrees. Use a hashmap
        # for O(1) lookups. Recurse on left and right subarrays.
        pass
