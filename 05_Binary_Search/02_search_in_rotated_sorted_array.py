"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium

Given a rotated sorted array with unique values, search for target in O(log n).

Examples:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - All values are unique.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Hint: Binary search. Determine which half is sorted. If target is in
        # the sorted half's range, search there. Otherwise search the other half.
        pass
