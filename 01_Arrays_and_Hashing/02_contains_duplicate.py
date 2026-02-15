"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Examples:
    Input: nums = [1,2,3,1]
    Output: true

    Input: nums = [1,2,3,4]
    Output: false

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hint: Use a set to track seen numbers. If a number is already in the
        # set, return True. Or simply compare len(nums) vs len(set(nums)).
        pass
