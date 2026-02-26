"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy

Merge two sorted linked lists and return as one sorted list.

Examples:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    - The number of nodes in both lists is in the range [0, 50].
    - -100 <= Node.val <= 100
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Hint: Use a dummy head node. Compare current nodes of both lists,
        # append the smaller one. Advance the pointer. Attach remaining nodes.
        pass
