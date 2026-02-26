"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
Difficulty: Hard

Given an array of k linked-lists, each sorted in ascending order,
merge all into one sorted linked-list.

Examples:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

    Input: lists = []
    Output: []

Constraints:
    - k == lists.length
    - 0 <= k <= 10^4
    - 0 <= lists[i].length <= 500
    - -10^4 <= lists[i][j] <= 10^4
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Hint: Use a min-heap. Push (val, index, node) for each list head.
        # Pop the smallest, add to result, push its next node.
        # Alternative: divide and conquer, merge pairs of lists.
        pass
