"""
435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
Difficulty: Medium

Given an array of intervals, return the minimum number of intervals you need
to remove to make the rest non-overlapping.

Examples:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1  (remove [1,3])

    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2

Constraints:
    - 1 <= intervals.length <= 10^5
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Hint: Greedy. Sort by end time. Keep the interval that ends earliest
        # (gives most room for future intervals). Count removals when overlap.
        pass
