"""
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
Difficulty: Hard

Design a data structure that supports:
    - addNum(num)      Adds an integer from the data stream.
    - findMedian()     Returns the median of all elements so far.

Examples:
    Input: ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
           [[],[1],[2],[],[3],[]]
    Output: [null,null,null,1.5,null,2.0]

Constraints:
    - -10^5 <= num <= 10^5
    - findMedian will only be called after at least one addNum.
"""


class MedianFinder:
    # Hint: Use two heaps:
    # - max-heap (negate values in Python) for the lower half
    # - min-heap for the upper half
    # Keep them balanced (sizes differ by at most 1).
    # Median is top of larger heap, or average of both tops.

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass
