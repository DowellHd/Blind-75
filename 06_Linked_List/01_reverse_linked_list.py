"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy

Given the head of a singly linked list, reverse the list, and return the
reversed list.

Examples:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Input: head = [1,2]
    Output: [2,1]

Constraints:
    - The number of nodes is in the range [0, 5000].
    - -5000 <= Node.val <= 5000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Hint: Iterative - use prev and curr pointers. At each step:
        # save curr.next, point curr.next to prev, advance prev and curr.
        pass
