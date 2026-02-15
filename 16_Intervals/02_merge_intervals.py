"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
Difficulty: Medium

Given an array of intervals, merge all overlapping intervals.

Examples:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]

Constraints:
    - 1 <= intervals.length <= 10^4
    - intervals[i].length == 2
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Hint: Sort by start time. Iterate and compare current interval's
        # start with last merged interval's end. If overlap, merge by
        # extending end. Otherwise, add as new interval.
        pass
