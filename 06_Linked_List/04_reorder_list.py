"""
143. Reorder List
https://leetcode.com/problems/reorder-list/
Difficulty: Medium

Given L0 -> L1 -> ... -> Ln-1 -> Ln, reorder it to:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

Examples:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    - The number of nodes is in the range [1, 5 * 10^4].
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Hint: 3 steps:
        # 1. Find middle with slow/fast pointers
        # 2. Reverse the second half
        # 3. Merge the two halves alternately
        pass
