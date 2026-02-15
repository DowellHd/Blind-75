"""
15. 3Sum
https://leetcode.com/problems/3sum/
Difficulty: Medium

Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
No duplicate triplets.

Examples:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = [0,1,1]
    Output: []

Constraints:
    - 3 <= nums.length <= 3000
    - -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hint: Sort the array. For each element, use two pointers on the
        # remaining subarray to find pairs that sum to -nums[i].
        # Skip duplicates to avoid duplicate triplets.
        pass
