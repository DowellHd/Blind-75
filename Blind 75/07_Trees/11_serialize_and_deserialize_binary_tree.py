"""
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Difficulty: Hard

Design an algorithm to serialize and deserialize a binary tree.

Examples:
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

Constraints:
    - The number of nodes is in the range [0, 10^4].
    - -1000 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Hint: Use preorder DFS with a null marker (e.g., "N").
    # Serialize: visit node, record val or "N", recurse left then right.
    # Deserialize: split string, use iterator, if "N" return None,
    # else create node and recurse for left and right children.

    def serialize(self, root: Optional[TreeNode]) -> str:
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass
