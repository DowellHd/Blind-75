"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy

Given head, determine if the linked list has a cycle in it.

Examples:
    Input: head = [3,2,0,-4], pos = 1
    Output: true

    Input: head = [1], pos = -1
    Output: false

Constraints:
    - The number of nodes is in the range [0, 10^4].
    - -10^5 <= Node.val <= 10^5
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Hint: Floyd's tortoise and hare. Use slow (1 step) and fast (2 steps)
        # pointers. If they meet, there's a cycle. If fast reaches None, no cycle.
        pass
