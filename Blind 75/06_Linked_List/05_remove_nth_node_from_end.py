"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium

Given the head, remove the nth node from the end and return the head.

Examples:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    Input: head = [1], n = 1
    Output: []

Constraints:
    - The number of nodes is sz, 1 <= sz <= 30.
    - 0 <= Node.val <= 100
    - 1 <= n <= sz
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Hint: Use two pointers with an n-node gap. Advance the fast pointer
        # n steps ahead. Then move both until fast reaches the end.
        # The slow pointer will be just before the node to remove.
        # Use a dummy node to handle edge cases.
        pass
