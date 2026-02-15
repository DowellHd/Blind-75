"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium

Given a sorted array rotated between 1 and n times, find the minimum element.
All elements are unique.

Examples:
    Input: nums = [3,4,5,1,2]
    Output: 1

    Input: nums = [4,5,6,7,0,1,2]
    Output: 0

Constraints:
    - n == nums.length
    - 1 <= n <= 5000
    - -5000 <= nums[i] <= 5000
    - All values are unique.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Hint: Binary search. If nums[mid] > nums[right], the min is in the
        # right half. Otherwise, it's in the left half (including mid).
        pass
