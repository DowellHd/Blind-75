"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/
Difficulty: Medium

Given a set of non-overlapping intervals sorted by start time, insert a new
interval, merging if necessary.

Examples:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]

Constraints:
    - 0 <= intervals.length <= 10^4
    - intervals[i].length == 2
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Hint: Three phases: add all intervals that end before newInterval,
        # merge all overlapping intervals with newInterval,
        # add all remaining intervals.
        pass
