"""
252. Meeting Rooms / 253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms/
https://leetcode.com/problems/meeting-rooms-ii/
Difficulty: Easy (#252) / Medium (#253)

Meeting Rooms I (#252):
    Given an array of meeting time intervals, determine if a person could
    attend all meetings (no overlaps).

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false

Meeting Rooms II (#253):
    Given an array of meeting time intervals, find the minimum number of
    conference rooms required.

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2

Constraints:
    - 0 <= intervals.length <= 10^4
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Hint: Sort by start time. Check if any meeting starts before
        # the previous one ends.
        pass

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Hint: Sort start and end times separately. Use two pointers.
        # When a meeting starts, add a room. When one ends, free a room.
        # Track the max rooms needed. Alternative: min-heap of end times.
        pass
